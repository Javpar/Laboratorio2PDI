#! /usr/bin/env python

from SimpleCV import Camera, Display, Image

cam = Camera()
img = cam.getImage()
img.save("PDI-image-n.png")
img.show()
imgGray = img.greyscale()
img.save("grayImage.jpg")
img.show()
hist = imgGray.histogram()
plot(histogram)
