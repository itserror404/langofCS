#!/usr/bin/python3

print("Content-Type: text/html\n\n")
print()
import cgi

data = cgi.FieldStorage()

def headHtml():

	print('''
	<!DOCTYPE HTML>
	<HTML>
	<HEAD>
	<TITLE> Sign up program </title>

	<link rel="stylesheet" type="text/css" href="style.css">
	</title>

	</head>
	<body>

	''')
	print("<h1>Thank for your registration! </h1>")

def getvalues():


	username = data['username'].value
	password = data['password'].value
	line = username + ":" + password + "\n"

	#open file 

	file = open("db.txt", "a")
	file.write(line)



def endHtml():

	print("</body> </html>")

headHtml()
getvalues()
endHtml()