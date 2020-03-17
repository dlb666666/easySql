CHECK_WAF_PALOAD = '\'AND 1=1 UNION ALL SELECT 1,NULL,\'<script>alert("XSS")</script>\',table_name FROM information_schema.tables WHERE 2>1--/**/; EXEC xp_cmdshell(\'cat ../../../etc/passwd\')#'
CHECK_WAF_Ratio_Value = 0.5
WAF_ATTACK_VECTORS = (
    "",  # NIL
    "search=<script>alert(1)</script>",
    "file=../../../../etc/passwd",
    "q=<invalid>foobar",
    "id=1 %s" % CHECK_WAF_PALOAD
)


class HTTP_HEADER:
    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    AUTHORIZATION = "Authorization"
    CACHE_CONTROL = "Cache-Control"
    CONNECTION = "Connection"
    CONTENT_ENCODING = "Content-Encoding"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_RANGE = "Content-Range"
    CONTENT_TYPE = "Content-Type"
    COOKIE = "Cookie"
    EXPIRES = "Expires"
    HOST = "Host"
    IF_MODIFIED_SINCE = "If-Modified-Since"
    LAST_MODIFIED = "Last-Modified"
    LOCATION = "Location"
    PRAGMA = "Pragma"
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    PROXY_CONNECTION = "Proxy-Connection"
    RANGE = "Range"
    REFERER = "Referer"
    SERVER = "Server"
    SET_COOKIE = "Set-Cookie"
    TRANSFER_ENCODING = "Transfer-Encoding"
    URI = "URI"
    USER_AGENT = "User-Agent"
    VIA = "Via"
    X_POWERED_BY = "X-Powered-By"

DEFAULT_HEADERS = {
    "User-Agent": "easySql-0.1",
}