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

camera = PiCamera()
camera.start_preview()


# Have the camera take pictures at the specified interval until the session is over using camera.capture(image.filename)
for i in range(SESSION_LENGTH//INTERVAL):
	camera.capture(RASPI_PATH+"/IMG_{}.jpg".format(i))
	time.sleep(INTERVAL)

camera.stop_preview()

#random test
