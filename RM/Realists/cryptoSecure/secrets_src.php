<?php

if ($_GET['source'] == "striptease") { readfile(__FILE__); die; }

define('SQL_HOST',      ':/var/run/mysqld/mysqld2-realiste-ch10.sock');
define('SQL_DB',        'c_realiste_10');
define('SQL_LOGIN',     'c_realiste_10');
define('SQL_P',         'voD5mf2iOFeGycz');

define('PRIVATE_KEY',   'file://keys/private_key.pem');
define('PUBLIC_KEY',    'file://keys/public_key.pem');
