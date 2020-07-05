from logging import StreamHandler, getLogger, DEBUG

from granola.application import WSGIApplication
from granola.libs.request_handler import RequestHandler

from handlers.json_handler import JsonHandler
from handlers.querystring_handler import QuerystringHandler


class HomeHandler(RequestHandler):

    def get(self):
        return "OK"

logger = getLogger('granola')
logger.setLevel(DEBUG)

handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)

_urls = {
    '/': HomeHandler(),
    '/json': JsonHandler(),
    '/querystring': QuerystringHandler()
}

application = WSGIApplication(
    _urls,
    logger
)
