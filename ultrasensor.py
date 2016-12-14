
import RPi.GPIO as gpio
import time
import os
import paho.mqtt.client as mqtt

mqttc=mqtt.Client("python_pub2")
mqttc.connect("127.0.0.1",1883)


trig=23
echo=24
print("start")
gpio.setmode(gpio.BCM)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
gpio.setup(25,gpio.OUT)
gpio.output(25,False)
gpio.setup(18,gpio.OUT)
gpio.output(18,False)

#os.system('amixer cset numid=3 1')


try:
	while True:
		gpio.output(trig,False)
		time.sleep(0.5)
		gpio.output(trig,True)
		time.sleep(0.00001)
		gpio.output(trig,False)
		while gpio.input(echo)==0:
			pulse_start=time.clock()
		while gpio.input(echo)==1:
			pulse_end=time.clock()
		pulse_duration=pulse_end-pulse_start
		distance=pulse_duration*17241
		distance=round(distance,2)
		mqttc.publish("environment/ultrasonic",distance)
        	print("Distance: ",distance,"cm")
 
		if distance<=10 :
			gpio.output(18,True)
			if distance<=5 :
				gpio.output(18,False)
				gpio.output(25,True)
			
				#os.system('mpg123 -vC  careful.mp3')
		
			else :
				gpio.output(25,False)
		else : 
			gpio.output(18,False)
			gpio.output(25,Fals)
		


except :
	gpio.cleanup()



mqttc.loop_forever()
