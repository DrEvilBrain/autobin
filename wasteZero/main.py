from api import apiCall
from sortImage import sortImage

# image url to do image recognition on (input as string)
url = "https://upload.wikimedia.org/wikipedia/commons/e/eb/Box.agr.jpg"

# checks if the image url is a valid string
if(url == None or url == ""):
	print("URL is empty")
elif not(isinstance(url, str)):
	print("URL is not a string")
else:
	# makes apiCall and fetches formated data from it
	status_code, json, tags, caption, confidence = apiCall(url)

	# checks if API response status code is 200 (valid response)
	if(status_code == 200):
		# output the response status code. 200 is the correct response
		print("Status Code: ", status_code)

		# output the image's tags and keywords
		print("Tags: ", tags)

		# output a phrase to describe/caption the image
		print("Captions: ", caption)

		# output a number describing how accurate the phase is
		print("Confidence: ", confidence)

		# sort image by the image's tags given from the API
		sortImage(tags)
	else:
		# output response status code for debugging purposes
		print("Response Status Code: ", status_code)