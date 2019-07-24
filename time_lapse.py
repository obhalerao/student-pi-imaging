import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time


# Enter the path where the raspberry pi will store its file
RASPI_PATH = "images_{}".format(time.asctime().replace(" ","_"))

os.mkdir(RASPI_PATH)

INTERVAL = 2# the time interval (in seconds) between pictures
SESSION_LENGTH = 600# the duration of the script
START_TIME = 30 #the time that we have to get the code running before it starts taking pictures

time.sleep(START_TIME)

camera = PiCamera()
camera.start_preview()


# Have the camera take pictures at the specified interval until the session is over using camera.capture(image.filename)
for i in range(SESSION_LENGTH//INTERVAL):
	camera.capture(RASPI_PATH+"/IMG_{}.jpg".format(i))
	time.sleep(INTERVAL)

camera.stop_preview()

#random test
