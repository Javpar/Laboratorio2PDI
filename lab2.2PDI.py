#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import pylab as plt

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()

imgGray = img.grayscale()
imgGray.save("grayImage.jpg")
imgGray.show()
hist = imgGray.histogram()
plt.plot(hist)

