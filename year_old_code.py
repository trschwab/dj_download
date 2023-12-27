import requests
from bs4 import BeautifulSoup
import os

example_link = "https://open.spotify.com/playlist/79LgcBHXvPIGCwqK9pZZS5?si=19caa06952044359"

print(example_link)

x = requests.get(example_link)

#print(x.content)
soup = BeautifulSoup(x.content, "html.parser")

results = soup.find_all("button", class_="EntityRowV2__PlayPauseButton-sc-ayafop-1 lbeQuE")


track_search = []
songs = []
for result in results:
	track = result.find_all("a")#, class_="EntityRowV2__AnchorLink-sc-ayafop-8 hfgfpQ").text
	for element in track:
		track_search += [element.text]
	songs += [track_search]
	#print(track_search)
	track_search = []
	#print(track)
	#print("\n")

#print(len(results))


query_strings = []
for item in songs:
	query = " ".join(item).replace(" ", "+")
	query_strings += [query]

URL = "https://www.youtube.com/results?search_query="

for item in query_strings:
	print(URL + item)
	yt_query = URL + item
	response = requests.get(yt_query)
	print(response.content)
	break





def download(link="NONE"):
	''' download link with youtube-dl
	'''
	if link == "NONE":
		#link = "https://www.youtube.com/watch?v=i_EhZIhY8c0" 
		link = "https://www.youtube.com/watch?v=eGfJ4shG4ak"
	os.system(f"youtube-dl \"{link}\"")
	print("done")


#download()
