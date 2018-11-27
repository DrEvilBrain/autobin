import os

def sortImage(imageTags):
	# grabs current file directory
	curr_dir = os.path.dirname(__file__)

	# open text files storing image tags and split them into words
	with open(curr_dir + "/recyclables.txt", "r+") as f:
		recycable = f.readlines()
		recycable = [x.lower() for x in recycable]
		recycable = [x.strip() for x in recycable]

	with open(curr_dir + "/landfill.txt", "r+") as f:
		landfill = f.readlines()
		landfill = [x.lower() for x in landfill]
		landfill = [x.strip() for x in landfill]

	# check tags to see which bin the item should go to
	for i in range(len(imageTags)):
		if imageTags[i] in recycable:
			return("THIS ITEM GOES TO THE RECYCLING BIN.")
		elif imageTags[i] in landfill:
			return("THIS ITEM GOES TO THE LANDFILL BIN.")
		if i == len(imageTags)-1:
			return("THIS ITEM GOES TO THE LANDFILL BIN.")