from urllib.parse import parse_qs

HTTP_STATUS = {
    200: '200 OK',
}


class RequestHandler(object):

    def __init__(self, environ, start_response):
        super(RequestHandler, self).__init__()

        _params = environ['QUERY_STRING']
        self.__params = parse_qs(_params)

    def __initialize(self):
        self.__contents_type = 'text/plain'
        self.__status_code = 200

    def set_contents_type(self, val):
        self.__contents_type = val

    def set_status_code(self, val):
        self.__status_code = val

    def __call__(self, environ, start_response):

        self.__initialize()

        _http_method = environ['REQUEST_METHOD']
        if _http_method == 'GET':
            _contents = self.get()

        elif _http_method == 'POST':
            _contents = self.post()

        else:
            raise Exception()

        bcontent = bytes(_contents, encoding='UTF-8')
        headers = [
            ('Content-Type', self.__contents_type),
            ('Content-Length', str(len(bcontent)))
        ]
        start_response(
            HTTP_STATUS.get(self.__status_code, 'UNKNOWN STATUS'),
            headers
        )
        return [bcontent]

