from glob import glob
from lib import init
from lib.datatype import AttribDict
from lib.setting import *
from lib.util import quickRatio, getPage, parserUrl
from lib.ColorPrint import Logger, ColorPrint
import inspect
import sys
import os


def checkConnection():
    logger.info(" target url: " + kb.rawUrl)
    logger.info(" testing connection to the target URL")
    page, headers, code = getPage(kb.rawUrl)
    retVal = True
    if code != 200:
        retVal = False
    return retVal


def checkHasWaf():
    rawUrl = kb.rawUrl
    logger.info(" checking if the target is protected by some kind of WAF/IPS")
    checkUrl = rawUrl + CHECK_WAF_PALOAD
    ratioVal = quickRatio(rawUrl, checkUrl)
    logger.success(" ratio为: " + str(ratioVal))
    reqVal = True if ratioVal < CHECK_WAF_Ratio_Value else False
    if reqVal:
        logger.error(" target is protected by some kind of WAF/IPS/IDS")
    else:
        logger.success(" target is not protected by some WAF/IPS/IDS")


def setWafFunctions():
    wafs = glob("waf/*.py")
    for found in wafs:
        dirname, filename = os.path.split(found)
        # 自定义搜索优先级
        if dirname not in sys.path:
            sys.path.insert(0, dirname)
        try:
            if filename[:-3] in sys.modules:
                del sys.modules[filename[:-3]]
            module = __import__(filename[:-3])
        except ImportError as msg:
            raise ImportError("cannot import WAF script '%s' (%s)" % (filename[:-3], msg))
        _ = dict(inspect.getmembers(module))
        kb.wafFunctions.append((_["detect"], _.get("__product__", filename[:-3])))


def checkWaf():
    setWafFunctions()
    for function, product in kb.wafFunctions:
        try:
            print.green("[+] checking for WAF/IPS/IDS product '%s'" % product)
            found = function(getPage, kb)
        except Exception as e:
            errMsg = "[-] exception occurred while running "
            errMsg += "WAF script for '%s' ('%s')" % (product, e)
            print.red(errMsg)
            found = False
        if found:
            msg = "[*] WAF/IPS/IDS identified as '%s'" % product
            print.red(msg)
            break


def initKb():
    kb.rawUrl = options.url
    kb.wafFunctions = []
    kb.url = parserUrl(kb)


def regGlobal():
    global kb
    global options
    global logger
    global print
    kb = AttribDict()
    options = init()
    logger = Logger()
    print = ColorPrint()


def start():
    regGlobal()
    initKb()
    if not checkConnection():
        print.red("[-] 目标连接失败")
        sys.exit()
    print.white(options)
    checkHasWaf()
    checkWaf()


if __name__ == '__main__':
    start()
