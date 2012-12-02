#!/usr/bin/env python
#title           :pic.py
#description     :This will convert an image into a string consisting of 0s and 1s.
#author          :smikey
#date            :20121201
#version         :0.1
#usage           :python pic.py
#notes           :
#python_version  :2.6.5  
#==============================================================================

import os, sys
import Image
from optparse import OptionParser

# Command line options
# Filename is required
# -y 0-100 is optional. It's the brightness value wether the pixel will be a 0 or a 1
parser=OptionParser()
parser.add_option("-y", "--luma", dest="brightness", default=70, help="Helligkeitswert")
(options, args)=parser.parse_args()
if len(args)!=1:
	parser.error("Es wird mindestens ein Argument erwartet")

# Open the image and convert it to RGB to remove the possible alpha channel
image=Image.open(args[0])
image = image.convert("RGB")
pix=image.load()

# Look for the size of the image
width,height=image.size

# Create the empty string
imagestring=""


# Go through every pixel and get the rgb color. Then calculate the brightness and add a 0 or a 1 to the imagestring wether the brightness is beyond or over the brightness value
for i in range(height):
	for j in range(width):
		r,g,b=pix[j,i]
		color=0.29*(float(r)/255)+0.587*(float(g)/255)+0.114*(float(b)/255)
		if int(100*color)<options.brightness:
			imagestring=imagestring+"1"
		else:
			imagestring=imagestring+"0"
	imagestring=imagestring+"\n"

# Print the complete image to the console
print imagestring
