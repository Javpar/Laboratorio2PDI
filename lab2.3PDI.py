#! /usr/bin/env python

from SimpleCV import Camera, Display, Image, matplotlib
import pylab as plt
import numpy as np
import cv2

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()
img = cv2.imread('PDI-image-n.png')
color = ('b','g','r')
for i,col in enumerate(color):
histr = cv2.calcHist([img],[i],None,[256],[0,256])
plt.plot(histr,color = col)
plt.xlim([0,256])
plt.show()
