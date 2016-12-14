from Light import Light


import RPi.GPIO as gpio




class On(Light):
	def __init__(self,num):
		self.output=num
                		
	def turnOff(self) :
		
		gpio.output(self.output,False)
		return Off(self.output)
	def turnOn(self):
	        
		return On(self.output)

class Off(Light):
	 def __init__(self,num):
                self.output=num
                
         def turnOn(self) :
                
                gpio.output(self.output,True)
                return On(self.output)
	 def turnOff(self):
		
		return Off(self.output)
		
class MyLight:
	def __init__(self,num):
		
		self.output=num

                gpio.setmode(gpio.BCM)
                gpio.setup(num,gpio.OUT)
                gpio.output(self.output,False)
		
		self.light=Off(self.output)
	def turnOn(self):
	
		
		

		self.light=self.light.turnOn()
	def turnOff(self):
	

		self.light=self.light.turnOff()
                

	

		


