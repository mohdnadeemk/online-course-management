def sendMail(email,password,subject="",html="",purpose_url=""):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	
	me = "nadeemkhan19923108@gmail.com"
	you = email

	msg = MIMEMultipart('alternative')
	msg['From'] = me
	msg['To'] = you

	if subject=="":
		msg['Subject'] = "Registration Successfull"
	else:
		msg['Subject'] = subject

	if html=="":
		html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to Online Course Mgt.</h1>
    					<p>You have successfully registered on this site </p>
    					<h2>Username : """+email+"""</h2>
    					<h2>Password : """+str(password)+"""</h2>
  					</body>
				</html>
			"""
	else:
		html = html
	
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("nadeemkhan19923108@gmail.com", "lstv hwzi xdlt bwfo") 
	
	part2 = MIMEText(html, 'html')

	msg.attach(part2)
	
	s.sendmail(me,you, str(msg)) 
	s.quit() 
	print("mail send successfully....")
