import RPi.GPIO as GPIO, feedparser
USERNAME="tallshe1008@gmail.com"
PASSWORD="tallshe108"
GPIO_PIN=8
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])


if newmails > 0: 
	GPIO.output(GPIO_PIN, True)
	print ('unread message:', newmails)
	
else: 
	GPIO.output(GPIO_PIN, False)
