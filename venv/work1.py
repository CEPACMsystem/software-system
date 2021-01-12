from wsgiref.simple_server import make_server
import jinja2
from controller import *
urls={
    '/':index,
    '/areticle':article,
    '/article_list':article_list
}
def application(env,start_response):
    start_response('200 ok',[('Content-Type','text/html')])#设置响应类型和状态码
    url=env['PATH_INFO']
    if url in urls.keys():
        fuc=urls.get(url,None)
        if fuc is not None:
            return fuc()
        else:
            return '404'
    else:
        return '404 page'
if _name_=='_main_':
    http_server=make_server('192.168.31.1',8888,application)
    http_server.serve_forever()