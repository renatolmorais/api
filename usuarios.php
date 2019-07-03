<?php

//var_dump($_SERVER);

$method = ( array_key_exists("REQUEST_METHOD",$_SERVER) ? $_SERVER["REQUEST_METHOD"] : "" );
$uri = ( array_key_exists("REQUEST_URI",$_SERVER) ? $_SERVER["REQUEST_URI"] : "" );

//echo $uri;
$resources = explode("/",$uri);

/*

API

http://api/document/id

documentos:
	usuarios

*/

switch( $method )
{
	case "GET":
		break;
	case "POST":
		var_dump($resources);
		break;
	case "PUT":
		break;
	case "HEAD":
		break;
	case "DELETE":
		break;
	default:
		break;
}
?>