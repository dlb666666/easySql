import argparse


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required="True", help="target url for scan")
    # parser.add_argument("--check-waf", required="False", help="check target waf product")
    options = parser.parse_args()
    # 处理并解析url
    if options.url:
        if not options.url.startswith("http://") and not options.url.startswith("https://"):
            options.url = "http://" + options.url
        if options.url.endswith("/") or options.url.endswith("\\"):
            options.url = options.url[:-1]
        return options
