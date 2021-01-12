#coding:utf8
from wsgiref.simple_server import make_server
def application(env,start_response):
    start_response('200 ok',['Content-Type','text/html'])
    return 'success'
# def article():
#     with open('aritcle.html','r') as f:
#         html=f.read()
#         return html
# def article_list():
#     return 'article list page ok'
if __name__=='__main__':
    http_server=make_server('127.0.0.1',6000,application)
    http_server.serve_forever()