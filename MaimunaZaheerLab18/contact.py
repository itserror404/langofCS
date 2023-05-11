#!/usr/bin/env python
import cgi



form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
compalin = form.getvalue('complain')
accept = form.getvalue('accept')


print("""Content-type: text/html /n 
    <html> 
    <head> 
    <title>Contact Form Response</title> 
    <link rel="stylesheet" href="style.css"></head><body>""")

print("""<h1>Contact Form Response</h1>""")
print ("<p><b>Name:</b>" + name +"</p>")
print("<p><b>Email:</b>"+email"</p>")

print("<p><b>Message:</b>"+ message+ "</p>")

if subscribe:
    print("<p><b>Accepted terms and condtions</b>Yes</p>")
else:
    print("<p><b>Accepted terms and condtions</b> No</p>")
print("</body>")
print("</html>")
