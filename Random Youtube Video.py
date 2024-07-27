import random
import requests
import webbrowser

prefixStringsList = ["DSC_", "DSC0", "IMG_", "PI_CT", "MOV_", "100_", "P000"]
randomSearch = random.choice(prefixStringsList) + str(random.randrange(1000, 9999))
print(randomSearch)

# https://developers.google.com/youtube/v3/docs/search/list
search_url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "id",
    "type": "video",
    "key": "", # insert your api key here
    "q": randomSearch
}

response = requests.get(search_url, params=params)
data = response.json()

# get a random item from the search results
video_id = data["items"][random.randrange(len(data["items"]))]['id']['videoId']
# get the video details
video_info_url = "https://www.googleapis.com/youtube/v3/videos"

params = {
    "part": "snippet",
    "id": video_id,
    "key": ""
}

response = requests.get(video_info_url, params=params)
data = response.json()

# print the video title
print(data["items"][0]['snippet']['title'])

# print the video link
webbrowser.open("https://www.youtube.com/watch?v=" + video_id)
