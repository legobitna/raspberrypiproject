import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import os

class Gmail:
	def __init__(self):
		
		self.to= "tallshe1008@gmail.com"
		self.gmail_user= "tallshe1008@gmail.com"
		self.gmail_password= "tallshe108"
	def sendmail(self):


		smtpserver=smtplib.SMTP('smtp.gmail.com',587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		smtpserver.login(self.gmail_user,self.gmail_password)
		self.today=datetime.date.today()
		self.arg="ip route list"
		self.proc=subprocess.Popen(self.arg,shell=True,stdout=subprocess.PIPE)
		self.data=self.proc.communicate()
		self.split_data=self.data[0].split()
		self.local_ip=self.split_data[self.split_data.index('src')+1]
		self.public_ip=os.system('wget http://ipecho.net/plain -O - -q > test.txt; echo')
		self.public_ip=open('test.txt','r').read()
		self.msg_content='Alarm detected public ip is %s:8081,local ip is %s'%(self.public_ip,self.local_ip)
		self.msg=MIMEText(self.msg_content)
		self.msg['Subject']='Raspberry Pi Alarm on %s' % self.today
		self.msg['From']=self.gmail_user
		self.msg['To']=self.to
		smtpserver.sendmail(self.gmail_user, [self.to], self.msg.as_string())
		smtpserver.quit()


