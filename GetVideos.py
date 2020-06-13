import csv
from apiclient.discovery import build

f = open("konpeki_no_sora.csv", "w")
writer = csv.writer(f)

YOUTUBE_API_KEY = "access_token"

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

search_request = youtube.search().list(
    part = "id",
    q = "紺碧の空",
    order = "viewCount",
    type = "video",
    videoDuration = "short",
    maxResults = 50
)

header = ["no.", "url"]
writer.writerow(header)
index = 1

for i in range(4):
    search_response = search_request.execute()
    length = len(search_response["items"])

    for j in range(length):
        video = search_response['items'][j]
        video_id = video["id"]["videoId"]
        row = [index, "https://www.youtube.com/watch?v={0}".format(video_id)]
        writer.writerow(row)
        index += 1

    search_request = youtube.search().list_next(search_request, search_response)
    
f.close()
