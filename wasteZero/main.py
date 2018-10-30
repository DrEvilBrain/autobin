from api import apiCall
from sortImage import sortImage
		
# url to do image recognition on (input as string)
url = "https://upload.wikimedia.org/wikipedia/commons/e/eb/Box.agr.jpg"

# makes apiCall and fetches formated data from it
status_code, json, tags, caption, confidence = apiCall(url)
 
# output the response status code. 200 is the correct response
print("Status Code: ", status_code)

# output the image's tags and keywords
print("Tags: ", tags)

# output a phrase to describe/caption the image
print("Captions: ", caption)

# output a number describing how accurate the phase is
print("Confidence: ", confidence)

sortImage(tags)