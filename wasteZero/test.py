import requests
from configparser import ConfigParser
from pprint import pprint
import os

# grabs current file directory
curr_dir = os.path.dirname(__file__)

# grabs API key from config.ini
config = ConfigParser()
config.read(curr_dir + "/config.ini")
API_KEY = config.get("API", "key")

# open text files storing image tags and split them into words
with open(curr_dir + "/compost.txt", "r+") as f:
	compost = f.readlines()
	compost = [x.lower() for x in compost]
	compost = [x.strip() for x in compost]

with open(curr_dir + "/recyclables.txt", "r+") as f:
	recycable = f.readlines()
	recycable = [x.lower() for x in recycable]
	recycable = [x.strip() for x in recycable]

with open(curr_dir + "/landfill.txt", "r+") as f:
	landfill = f.readlines()
	landfill = [x.lower() for x in landfill]
	landfill = [x.strip() for x in landfill]

# url to do image recognition on (input as string)
url = "https://upload.wikimedia.org/wikipedia/commons/e/eb/Box.agr.jpg"

# calls Microsoft Computer Vision API from mashape
response = requests.post("https://microsoft-azure-microsoft-computer-vision-v1.p.mashape.com/describe",
	headers={
		"X-Mashape-Key": API_KEY,
		"Content-Type": "application/json",
		"Accept": "application/json"
	},
	json=(
		{'url': url}
	)
)

status_code = response.status_code
json = response.json()
tags = json["description"]["tags"]
caption = json["description"]["captions"][0]["text"]
confidence = json["description"]["captions"][0]["confidence"]

# output the response status code. 200 is the correct response
print("Status Code: ", status_code)

# output the image's tags and keywords
print("Tags: ", tags)

# output a phrase to describe/caption the image
print("Captions: ", caption)

# output a number describing how accurate the phase is
print("Confidence: ", confidence)

# check tags to see which bin the item should go to
for i in range(len(tags)):
	if tags[i] in recycable:
		print("THIS ITEM GOES TO THE RECYCLING BIN.")
		break
	elif tags[i] in compost:
		print("THIS ITEM GOES TO THE COMPOST BIN.")
		break
	elif tags[i] in landfill:
		print("THIS ITEM GOES TO THE LANDFILL BIN.")
		break
	if i == len(tags)-1:
		print("THIS ITEM GOES TO THE LANDFILL BIN.")