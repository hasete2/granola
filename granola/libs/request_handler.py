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
        return self.__status_code

    @status_code.setter
    def status_code(self, v):
        self.__status_code = v

    @property
    def params(self):
        return  self.__params

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

    def set_contents_type(self, val):
        self.__contents_type = val

    def set_status_code(self, val):
        self.__status_code = val
        
    def set_content_length(self):
        self.__set_content_length = True

    def initialize(self):
        pass

    def get_query_string(self, key):
        return self.__query_strings.get(key, None)

    def __params_init(self):
        _params = self.__environ['QUERY_STRING']
        self.__params = parse_qs(_params)

        for _k in self.__params:
            self.__query_strings[_k] = self.__params[_k][0]

    def get(self, *args, **kwargs):
        self.set_status_code(405)
        return "405 Method Not Allowed"

    def post(self, *args, **kwargs):
        self.set_status_code(405)
        return "405 Method Not Allowed"

    def entry(self, environ, start_response):

        self.__environ = environ

        _remote_ip = environ.get('REMOTE_ADDR', None)
        self.__remote_ip = environ.get('X-Forwarded-For', _remote_ip)

        self.__contents_type = 'text/plain'
        self.__status_code = 200
        self.__set_content_length = None

        self.__params = {}
        self.__query_strings = {}

        self.__params_init()
        self.initialize()

        _http_method = environ['REQUEST_METHOD']
        if _http_method == 'GET':
            _contents = self.get()

        elif _http_method == 'POST':
            _contents = self.post()

        else:
            self.__status_code = 405
            _contents = HTTP_STATUS[405]
        
        bcontent = bytes(_contents, encoding='UTF-8')
        headers = [
            ('Content-Type', self.__contents_type)
        ]

        if self.__set_content_length:
            headers.append(('Content-Length', str(len(bcontent))))
            
        start_response(
            HTTP_STATUS.get(self.__status_code, 'UNKNOWN STATUS'),
            headers
        )
        return [bcontent]
