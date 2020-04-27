import json

from granola.libs.request_handler import RequestHandler


class QuerystringHandler(RequestHandler):

    def initialize(self):
        print(self.params)
        print(self.get_query_string("foo"))
        print(self.get_query_string("bar"))

    def get(self):
        self.set_contents_type('application/json')
        self.set_status_code(200)
        self.set_content_length()

        return json.dumps({"foo": "bar"})
