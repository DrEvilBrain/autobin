from time import sleep
from picamera import PiCamera

def takePicture():
	camera = PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	# camera warm-up time
	sleep(2)
	camera.capture("image.jpg")