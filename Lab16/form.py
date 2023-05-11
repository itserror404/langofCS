#!/usr/bin/env python
import cgi



form = cgi.FieldStorage()
name = form['name'].value
age = form['age'].value




print("""Content-type: text/html /n 
    <html> 
    <head> 
    <title>Form Response</title> 
    <link rel="stylesheet" href="style.css"></head><body>""")

print("""<h1>Form Response</h1>""")
print ("<p><b>Name:</b>" + name +"</p>")
print("<p><b>Age:</b>"+age"</p>")
print("</body>")
print("</html>")
