import RPi.GPIO as IoPort
import datetime
import time
import MySQLdb
import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
from GmailWarning import Gmail
from template import sensor 

class temperature(sensor):
	def __init__(self,dout):
		self.dout=dout
		self.db=MySQLdb.connect("localhost","root","1234","dht11")
		self.curs=self.db.cursor()
		self.gmail=Gmail()
		self.mqttc=mqtt.Client("python_pub")
		self.mqttc.connect("127.0.0.1",1883)

		print('start')
	def execute(self):
         	 self.h,self.t=dht.read_retry(dht.DHT11,4)
	         self.a=self.t
		 self.insert= (
                        "INSERT INTO temperature (date,temperature,humidty) VALUES(%s,%s,%s)"
                                )
                 self.data=(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),self.t,self.h)

                 self.curs.execute(self.insert,self.data)
      

                 self.db.commit()
		 print('end db')

	def sendmessage(self):
       		 self.mqttc.publish("environment/temperature",self.a)
	def printmessage(self):
     	   	 print('temperature',self.t)
       		 print('humindty',self.h)
	def judgement(self):
       		 
       		 if self.t >=28 :
               		 self.gmail.sendmail()
       	
		
try :

	temp=temperature(4)

	while True:

        	temp.execute()
		temp.sendmessage()
		temp.printmessage()
		temp.judgement()
		time.sleep(2)

except:
	gpio.cleanup()

	
	

mqttc.loop_forevr()
