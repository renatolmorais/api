#!c:\python27\python.exe
#encoding: UTF-8

import sys,os
import cgi, cgitb
import sqlite3
cgitb.enable()
import json

'''	request 	=> { "function": "get", "object": "client", "name": "client name" }
	response	=> { "function": "get", "response": "response" }
'''

db = sqlite3.connect('..\\db\\database.db')
c = db.cursor()

client_select_st = 'select * from cliente where name = ?'

def get_element( name,form ):
	if name in form: return form[name].value
	else: return ''

print("Content-Type: text/html\n")

response = {}
form = cgi.FieldStorage()

if get_element( 'function', form ) == 'get':
	if get_element( 'object', form ) == 'client':
		result_set = c.execute( client_select_st, (get_element( 'name', form ),) )
		for row in result_set:		
			response = {	"function": get_element( 'function',	form ),
							"object":	get_element( 'object',		form ),
							"response": row[1],
						}

print json.dumps( response )