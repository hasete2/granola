import json

from granola.libs.request_handler import RequestHandler


class JsonHandler(RequestHandler):

    def initialize(self):
        pass

    def get(self):
        self.set_contents_type('application/json')
        self.set_status_code(200)
        return json.dumps({"foo": "bar"})
