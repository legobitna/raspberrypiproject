from abc import ABCMeta, abstractmethod
from Light import Light


import RPi.GPIO as gpio

class Command:
	def __init__(self):
		self.light
		
	def execute(self):
		pass


