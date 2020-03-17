from urllib.parse import urlparse
import requests
import difflib
import functools
import random
import re


def parserUrl(kb):
    parse = urlparse(kb.rawUrl)
    randomStr = str(random.randint(1000, 9999))
    query = parse.query
    if "*" in parse.query:
        rex = r"=(.*\*)&"
        query = re.sub(rex, "=" + randomStr + "&", parse.query)
    baseUrl = parse.scheme + "://" + parse.netloc + parse.path
    url = baseUrl + "?" + query
    return {"baseUrl": baseUrl, "query": query, "url": url}


def getPage(url):
    r = requests.get(url)
    return r.text, r.headers, r.status_code


def getContent(url):
    return requests.get(url).content


def quickRatio(u1, u2):
    rawRequest = getContent(u1)
    checkWafRequest = getContent(u2)
    retVal = difflib.SequenceMatcher(None, rawRequest, checkWafRequest).quick_ratio()
    return retVal



