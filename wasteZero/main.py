from api import apiCall
from sortImage import sortImage
import os

# locally saved image file to do image recongition on
curr_dir = os.path.dirname(__file__)
image = curr_dir + "/image.jpg"

# image url to do image recognition on (input as string)
# image = ""

# makes apiCall and fetches formated data from it
status_code, json, tags, caption, confidence = apiCall(image)

# checks if API response status code is 200 (valid response)
if(status_code == 200):
	# output the response status code. 200 is the correct response
	print("Status Code: ", status_code)

	# output the image's tags and keywords
	print("Tags: ", tags)

	# output a phrase to describe/caption the image
	print("Captions: ", caption)

	# output a number describing how accurate the phrase is
	print("Confidence: ", confidence)

	# sort image by the image's tags given from the API
	print(sortImage(tags))
else:
	# output response status code for debugging purposes
	print("Response Status Code: ", status_code)