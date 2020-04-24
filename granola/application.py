from granola.libs.error_handler import NotFoundHandler


class WSGIApplication(object):

    def __init__(self, urls, **kwargs):
        self.__urls = urls

    def __call__(self, environ, start_response):

        _path = environ['PATH_INFO']
        _h = self.__urls.get(_path, NotFoundHandler())
        return _h.entry(environ, start_response)
