from  wsgiref.simple_server import make_server
def user(environ,start_response):
    print('user page')
    start_response("200 ok", [('Content_type', 'text/html;charset=utf-8')])
    return [bytes('<h2>user page</h2>', encoding=utf - 8)]
def addres(environ,start_response):
    print('addres page')
    start_response("200 ok", [('Content_type', 'text/html;charset=utf-8')])
    return [bytes('<h2>addres page</h2>', encoding=utf - 8)]
def url_dispacher(environ,start_response):
    urls={
        '/user':uesr,
        'addres':addres
    }
def run_server(environ,start_response):
    print('hahhahah',environ)
    url_list=url_dispacher()
    request_url=environ.get("PATH_INFO")
    print('request url',request_url)
    if request_url in url_list:
        func_data=url_list[request_url](environ,start_response)
        return func_data
    else:
        start_response("404", [('Content_type', 'text/html;charset=utf-8')])
        return [bytes('<h1>404,page not found</h1>', encoding=utf - 8)]
s=make_server('127.0.0.1',6000,run_server)
s.serve_forever()
