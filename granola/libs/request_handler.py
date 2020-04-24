from urllib.parse import parse_qs

HTTP_STATUS = {
    200: '200 OK',
    400: '400 Bad Request',
    404: '404 NotFound',
    405: '405 Method Not Allowed'
}


class RequestHandler(object):

    @property
    def status_code(self):
        return self,__status_code

    @status_code.setter
    def status_code(self, v):
        self.__status_code = v

    @property
    def params(self):
        _params = self.environ['QUERY_STRING']
        _params = parse_qs(_params)
        return _params

    @property
    def body(self):
        _length = int(self.__environ.get('CONTENT_LENGTH', '0'))
        _body = self.__environ.get('wsgi.input').read(_length).decode('utf-8')
        return _body

    @property
    def remote_ip(self):
        return self.__remote_ip

    def __init__(self):
        self.__environ = None
        self.__remote_ip = None

        self.__contents_type = 'text/plain'
        self.__status_code = 200

    def set_contents_type(self, val):
        self.__contents_type = val

    def entry(self, environ, start_response):

        self.__environ = environ

        _remote_ip = environ.get('REMOTE_ADDR', None)
        self.__remote_ip = environ.get('X-Forwarded-For', _remote_ip)

        _http_method = environ['REQUEST_METHOD']
        if _http_method == 'GET' and hasattr(self, 'get'):
            _contents = self.get()

        elif _http_method == 'POST' and hasattr(self, 'post'):
            _contents = self.post()

        else:
            self.__status_code = 405
            _contents = HTTP_STATUS[405]

        # ('Content-Length', str(len(bcontent)))
        
        bcontent = bytes(_contents, encoding='UTF-8')
        headers = [
            ('Content-Type', self.__contents_type)
        ]
        start_response(
            HTTP_STATUS.get(self.__status_code, 'UNKNOWN STATUS'),
            headers
        )
        return [bcontent]
