from mitmproxy import http

class CookieBlocker:
    def request(self, flow: http.HTTPFlow) -> None:
        blocked_sites = ["deriv.com"]

        if any(site in flow.request.pretty_host for site in blocked_sites):
            
            flow.request.headers.pop('cookie', None)

addons = [
    CookieBlocker()
]
