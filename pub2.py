import RPi.GPIO as gpio
import time
import paho.mqtt.client as mqtt
from LightState import MyLight
from template import sensor

class ultrasensor(sensor):
	def __init__(self,trig,echo):
		self.trig=trig
		self.echo=echo

		self.mqttc=mqtt.Client("python_pub2")
		self.mqttc.connect("127.0.0.1",1883)
		self.red= MyLight(25)
		self.yellow=MyLight(18)
		print('start')
		gpio.setmode(gpio.BCM)
		gpio.setup(self.trig, gpio.OUT)
		gpio.setup(self.echo, gpio.IN)
	def exectue(self):
		gpio.output(self.trig,False)
                time.sleep(0.5)
                gpio.output(self.trig, True)
                time.sleep(0.00001)
                gpio.output(self.trig, False)
                while gpio.input(self.echo)==0 :
                        self.pulse_start= time.clock()
                while gpio.input(self.echo) ==1 :
                        self.pulse_end= time.clock()
                self.pulse_duration= self.pulse_end - self.pulse_start
                self.distance=self.pulse_duration* 17241
                self.distance=round(self.distance,2)
	def sendmessage(self):
                self.mqttc.publish("environment/ultrasonic",self.distance)
	def printmessage(self):
                print("Distance:",self.distance,"cm")
	def judgement(self):
                if self.distance <=5 :

                        self.yellow.turnOn()
                        if self.distance <=3 :
                                self.yellow.turnOff()
                                self.red.turnOn()
                        else :
                                self.red.turnOff()
                                self.yellow.turnOn()
                else :

                        self.yellow.turnOff()
                        self.red.turnOff()

		



try:
	ultra=ultrasensor(23,24)

        while True:
                ultra.exectue()
                ultra.sendmessage()	
	        ultra.printmessage()
		ultra.judgement()


except: 
	gpio.cleanup()
