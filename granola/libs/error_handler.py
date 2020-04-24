from granola.libs.request_handler import RequestHandler


class NotFoundHandler(RequestHandler):

    def get(self):
        return self.__request()

    def post(self):
        return self.__request()

    def __request(self):
        self.status_code = 404
        return '404 NotFound'
