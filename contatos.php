<?php

include_once('include.php');

switch($method)
{
	case 'GET':
		$msg = "you want to get information about contact $id";
		$status = "OK";
		break;
	case 'POST':
		$msg = "you want to update information about contact $id";
		$status = "OK";
		break;
	case 'PUT':
		$msg = "you want to create contact $id";
		$status = "OK";
		break;
	case 'DELETE':
		$msg = "you want to delete contact $id";
		$status = "OK";
		break;
	case 'HEAD':
		$msg = "you want nothing";
		$status = "OK";
		break;
	default:
		break;
}

echo json_encode(
	array(
		"status" => $status,
		"message" => $msg,
		"response" => array(
						"id" => $id,
						"name" => ( array_key_exists('name',$input) ? $input['name'] : "" ),
						"age" => ( array_key_exists('age',$input) ? $input['age'] : "" )
					)
	)
);
?>