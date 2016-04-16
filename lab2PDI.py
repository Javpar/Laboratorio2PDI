from SimpleCV import Camera, Display, Image

cam = Camera()
img = cam.getImage()
img.save("PDI-image-n.jpg")
img.show()
imgGray = img.grayscale()
hist = imgGray.histogram()
plot(hist)
