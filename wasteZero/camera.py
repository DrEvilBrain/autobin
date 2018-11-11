from time import sleep
from picamera import PiCamera

def takePicture():
	# Explicitly open a new file called my_image.jpg
	pic = open('my_image.jpg', 'wb')
	camera = PiCamera()
	camera.start_preview()
	sleep(2)
	camera.capture(my_file)
	# At this point my_file.flush() has been called, but the file has
	# not yet been closed
	pic.close()