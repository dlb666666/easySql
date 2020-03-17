import re
from lib.setting import WAF_ATTACK_VECTORS

__product__ = "360 Web Application Firewall (360)"


def detect(get_page, kb):
    retval = False
    for vector in WAF_ATTACK_VECTORS:
        page, headers, code = get_page(kb.url['url'] + "&" + vector)
        retval = re.search(r"wangzhan\.360\.cn", headers.get("X-Powered-By-360wzb", ""), re.I) is not None
        retval |= code == 493 and "/wzws-waf-cgi/" in (page or "")
        if retval:
            break

    return retval
