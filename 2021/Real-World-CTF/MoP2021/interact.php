<?php

$descriptors = array(
    0 => array("pipe", "r"),  // STDIN
    1 => array("pipe", "w"),  // STDOUT
    2 => array("pipe", "w")   // STDERR
);
$process = proc_open('/readflag', $descriptors, $pipes);

print(fgets($pipes[1]));

$e = fgets($pipes[1]);
print($e);
print(fread($pipes[1], 19));

$r = eval("return " . $e . ";");
print($r);
fwrite($pipes[0], $r . "\n");

print(fgets($pipes[1]));
print(fgets($pipes[1]));
print(fgets($pipes[1]));
