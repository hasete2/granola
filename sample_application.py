from granola.application import WSGIApplication
from granola.libs.request_handler import RequestHandler

from handlers.json_handler import JsonHandler
from handlers.querystring_handler import QuerystringHandler


class HomeHandler(RequestHandler):

    def __init__(self):
        pass

    def get(self):
        return "OK"

_urls = {
    '/': HomeHandler(),
    '/json': JsonHandler(),
    '/querystring': QuerystringHandler()
}

application = WSGIApplication(
    _urls
)
