from lib.setting import HTTP_HEADER, WAF_ATTACK_VECTORS
import re


__product__ = "Yunsuo Web Application Firewall (Yunsuo)"


def detect(get_page, kb):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, code = get_page(kb.url['url'] + "&" + vector)
        retval = re.search(r"<img class=\"yunsuologo\"", page, re.I) is not None
        retval |= re.search(r"yunsuo_session", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
        if retval:
            break

    return retval
