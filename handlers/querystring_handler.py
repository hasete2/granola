import json

from granola.libs.request_handler import RequestHandler


class QuerystringHandler(RequestHandler):

    def __init__(self):
        pass

    def get(self):
        self.set_contents_type('application/json')
        self.set_status_code(200)
        return json.dumps({"foo": "bar"})
