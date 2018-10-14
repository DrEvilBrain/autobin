import requests
from configparser import ConfigParser
import os

# grabs current file directory
curr_dir = os.path.dirname(__file__)

# grabs API key from config.ini
config = ConfigParser()
config.read(curr_dir + "/config.ini")
API_KEY = config.get("API", "key")

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

print(response)
print(response.json())