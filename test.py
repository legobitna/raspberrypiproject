import RPi.GPIO as GPIO
import time
import sys
import signal
import os
import dhtreader
DHT_GPIO = 4
GPIO.setmode(GPIO.BCM)

while True:
	while True:
		try :
			TEMP,HUMID =dhtreader.read(DHT11,DHT_GPIO)
		        break
		except TypeError :
			time.sleep(5)
                print("tem",TEMP)
		print("hum",HUMID)



