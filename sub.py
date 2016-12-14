import paho.mqtt.client as mqtt

import RPi.GPIO as gpio
import time
import threading
import os
from subject import subject
save1=0
save2=0
from sub2 import LED, Mp3

class dataCenter(subject) :
	def __init__(self):
		print('datacenterstart')
		self.observers=[]
		self.save1=0
		self.save2=0

	def setdatasource(self,save1,save2):
		
		self.save1=save1
		self.save2=save2
		self.setnotice()
		
	def getdata1(self):
		return self.save1
	def getdata2(self):
		return self.save2
	def setnotice(self):
	
		for observer in self.observers:
	
			observer.update(self.save2,self.save1)
	def addObserver(self,observer):
		self.observers.append(observer)
		print('add observer')

def main():
	
	data=dataCenter()
	task1=LED()
	task2=Mp3()
	data.addObserver(task1)
	data.addObserver(task2)
	while True:
		data.setdatasource(save1,save2)




def on_connect(client,userdata,rc) :
        client.subscribe("environment/temperature")
        client.subscribe("environment/ultrasonic")
def on_message(client,userdata,msg) :
        global save2
        global save1

        if(msg.topic =="environment/temperature") :
                save2= float(msg.payload)
        if(msg.topic=="environment/ultrasonic") :
                save1= float(msg.payload)



save3=threading.Thread(target = main)
client=mqtt.Client("pub client")
client=mqtt.Client("pub2 client")
client.on_connect=on_connect
client.on_message=on_message
client.connect("127.0.0.1",1883,60)

save3.start()
client.loop_forever()





