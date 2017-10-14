<?php

if ($_GET['source'] == "striptease") { readfile(__FILE__); die; }

function rsa_decrypt($data){
    openssl_private_decrypt(base64_decode($data), $decrypted, PRIVATE_KEY,OPENSSL_NO_PADDING );
    return ltrim($decrypted);
}

function secure_mysql_variable($var){
        if( preg_match('/([\\\\\s\-\'"#]|benchmark|sleep|into|regexp|inter|union|select|from|join|limit|offset|like|where|concat|group|order|having|case|between)/i', $var)) {
                $_SESSION['hacker'] = True;
                exit('Hey !!!! Attack detected ! How do you do it ?? This incident will be reported !');
            }
        return mysql_real_escape_string($var);
}

function getPages(){
    $res = mysql_query("SELECT * FROM page INNER JOIN user USING (user_id) WHERE page_enabled=1 ORDER BY page_date DESC");
    $array = array();
    while($row = mysql_fetch_array($res, MYSQL_ASSOC)){
        $array[] = array(
            "page_id"       => $row['page_id'],
            "user_name"     => $row['user_name'],
            "page_title"    => $row['page_title'],
            "page_date"     => $row['page_date'],
            "page_minicontent" => $row['page_minicontent'],
            "page_url"      => $row['page_url'],
            "page_content"  => $row['page_content'],
            "page_enabled"  => $row['page_enabled'],
            );
    }
    return $array;
}
