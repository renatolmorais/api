<?php

/*
This script verify if the request is valid!
*/

if ( array_key_exists('REQUEST_METHOD',$_SERVER) )
{
	$uri = substr($_SERVER['REQUEST_URI'],1);
	$resources = explode("/",$uri);
	if( count($resources) == 2) list($action,$id) = $resources;
	else
	{
		echo json_encode(
			array(
				"status" => "ERROR",
				"message" => "not a valid url",
				"response" => array()
			)
		);
		exit(1);
	}
	$method = $_SERVER['REQUEST_METHOD'];
	$input = json_decode(file_get_contents('php://input'),true);
}
else
{
	echo json_encode(
		array(
			"status" => "ERROR",
			"msg" => "",
			"response" => array()
		)
	);
	exit(1);
}
?>