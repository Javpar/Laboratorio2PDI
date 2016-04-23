#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import pylab as plt

c = Camera()
img = c.getImage()
img.save("PDI-image-n.png")
img.show()
imgGray = img.grayscale()  %transforma la imagen a escala de grises
imgGray.save("grayImage.jpg") %guarda la nueva imagen
imgGray.show() %muestra la nueva imagen
hist = imgGray.histogram() %hace un histograma con los valores de intensidad por pixel de la imagen recien generada
plt.plot(hist) %%muestra la imagen del histograma


