<?php
session_start();

if ($_SESSION['hacker']) die("No no no no no !! You try to hack me ! Goodbye !");
// show source (highlight_file is disabled)
if ($_GET['source'] == "striptease") { readfile(__FILE__); die; }

require("includes/rain.tpl.class.php");
require("includes/secrets.inc.php");
require("includes/functions.inc.php");

mysql_connect(SQL_HOST, SQL_LOGIN, SQL_P) or exit('MySQL connection error !');
mysql_select_db(SQL_DB) or die("Database selection error !");

raintpl::configure("base_url", null );
raintpl::configure("tpl_dir", "templates/" );
raintpl::configure("cache_dir", "tmp/" );

$tpl = new RainTPL;

if (isset($_POST['authentication'])){
    $_SESSION = array();
    $login = strtolower(secure_mysql_variable($_POST['login']));
    $password = mysql_query("SELECT user_password FROM user WHERE user_name='$login'");
    $password = mysql_fetch_array($password);
    $password = $password['user_password'];
    if (!empty($_POST['password']) && $_POST['password'] == rsa_decrypt($password)){
        $_SESSION['auth'] = $login;
        $tpl->assign('authsuccess', True);
    }
    else {
        $tpl->assign('authfailed', True);
    }
}


if(isset($_SESSION['auth']))
    $tpl->assign('isauth', True);

if (!empty($_GET['page'])){
    // show article
    $result = mysql_query("SELECT * FROM page INNER JOIN user USING (user_id) WHERE page_id=".secure_mysql_variable($_GET['page']));
    if (!@mysql_num_rows($result)){
        $tpl->assign('notfound', True);
    }
    $result = @mysql_fetch_array($result, MYSQL_ASSOC);
    $tpl->assign($result);
    $tpl->draw('article');
}
else {
    // list pages
    $tpl->assign("pages", getPages());
    $tpl->draw('index');
}

mysql_close();
