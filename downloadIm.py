#Gabi Tessier, 7/19/2019
#this program asks usr for directory path and will insert image and name into database
import RemoteSensingDB as dmain
from PIL import Image
import glob
import os
import pathlib

if "__name__" == __main__:

	# select a path for accessing all of the images
	# can be a string or an os Path object
	pathname = ""

	# return a list of all the JPEG files in the directory
	file_list = []

	# place all photos into the database
	# first checking that you are not overwriting data
