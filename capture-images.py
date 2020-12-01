from time import sleep
from picamera import PiCamera
import datetime
import os

pin1 = 4
pin2 = 17

dir = 'data'
if not os.path.exists(dir):
	os.mkdir(dir)

camera = PiCamera()
while datetime.datetime.now() < datetime.datetime(2020, 12, 3, 12):
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(pin1,GPIO.OUT)
		GPIO.output(pin1,GPIO.HIGH)
		GPIO.setup(pin2, GPIO.OUT)
		GPIO.output(pin2, GPIO.HIGH)	
		dt = datetime.datetime.now()
		month, day, hour, minute = dt.month, dt.day, dt.hour, dt.minute

		filename = f"sourdough-date-{month}-{day}-time-{hour}-{minute}.jpg"
		filepath = f"{dir}/{filename}"
		camera.capture(filepath)
		print(f"Saved image at {filepath}...")
		sleep(300)
	except:
		camera.close()
camera.close()
 
