import RPi.GPIO as gpio
import time
import threading
import os
from observer import observer
from LightState import MyLight
class LED(observer):
	def __init__(self):
		print('led start')
		self.green=MyLight(7)

	def update(self,save2,save1):
		 print("temperature:%d c" % int(save2))
                 print("ultrasonic: %.2f cm"% float(save1))

                 if save2>27 :
                                if save1<=5 :
                                     self.green.turnOn()          
                                              
                                else:
                                        self.green.turnOff()
                 else:
                                self.green.turnOff()
                 time.sleep(1)

class Mp3(observer):
	def __init__(self):
		os.system('amixer cset numid=3 1')
	def update(self,save2,save1):
		if save2>27 :
			if save1 <=5 :
				os.system('mpg123 -vC careful.mp3')
                





	
