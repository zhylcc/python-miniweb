import re

URL_FUNC_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
    return set_func


@route(r'/dynamic.html')
def stock(ret):
    content = "<h1>Hello, MiniWeb!</h1>"
    return content

def application(env, start_response):
    source, mimetype = env.get('PATH_INFO', ''), env.get('MIMETYPE', 'text/plain;charset=utf-8')
    for url, func in URL_FUNC_DICT.items():
        ret = re.match(url, source)
        if ret:
            start_response('200 OK', [('Content-Type', mimetype)])
            print('200 OK!')
            return func(ret)
    else:
        print('404!')
        start_response('404', [('Content-Type', mimetype)])
        return '<h1>No page!</h1>'
