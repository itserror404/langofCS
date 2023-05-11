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
	<TITLE> Login Website</title>

	<link rel="stylesheet" type="text/css" href="style.css">
	</title>

	</head>
	<body>

	''')


def getvalues():


	username = data['username'].value
	password = data['password'].value

	print("Username:", username)
	print("password:", password)


	file = open("db.txt", "r")
	match=0

	for i in file:
		line=line.rstrip("\n")
		list=line.split(":")

		if (list[0]==username) and (list[l]==password):
			match=1
			print('you are signed in!  <a href="index.html"> go to your page </a> ')
	if match==0:
		print('Incorrect password, go back and try again!  <a href="index.html"> go to your page </a> ')

def endHtml():

	print("</body> </html>")

headHtml()
getvalues()
endHtml()