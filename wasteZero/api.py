import requests
from configparser import ConfigParser
import os

'''
Performs a Microsoft Computer Vision API call

Keyword argument:
image -- URL or file to perform image recognition on
'''
def apiCall(image=None):
	# grabs current file directory
	curr_dir = os.path.dirname(__file__)

	# grabs API key from config.ini
	config = ConfigParser()
	config.read(curr_dir + "/config.ini")
	API_KEY = config.get("API", "key")
	
	# checks to use URL or locally stored image as determined by config file
	imageIsURL = config.getboolean("DEBUG", "use_url")
	
	# perform API call by passing a URL
	if(imageIsURL):
		# use image URL to call Microsoft Computer Vision API from mashape
		response = requests.post("https://microsoft-azure-microsoft-computer-vision-v1.p.mashape.com/describe",
			headers={
				"X-Mashape-Key": API_KEY,
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			json=(
				{"url": image}
			)
		)
	# perform API call by passing an image
	else:
		# open image to do image recognition on
		with open(image, mode="rb") as f:
			img_data = f.read()
	
		# use stored image to call Microsoft Computer Vision API from mashape
		response = requests.post("https://microsoft-azure-microsoft-computer-vision-v1.p.mashape.com/describe",
			headers={
				"X-Mashape-Key": API_KEY,
				"Content-Type": "application/octet-stream",
				"Accept": "application/json"
			},
			data=img_data
		)
	
	status_code = response.status_code
	json = response.json()
	tags = json["description"]["tags"]
	caption = json["description"]["captions"][0]["text"]
	confidence = json["description"]["captions"][0]["confidence"]
	
	return status_code, json, tags, caption, confidence