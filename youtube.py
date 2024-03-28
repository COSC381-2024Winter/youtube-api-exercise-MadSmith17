import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results, page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=query_term, part="id,snippet", maxResults=max_results, type="video", pageToken=page_token).execute()
    
    next_page_token = search_response['nextPageToken']
    search_list = []
    for item in search_response['items']:
        search_list.append(item)
    
    if len(search_list) == 0:
        print("No results")
    elif len(search_list) < int(max_results):
        print("No more results")

    return search_list, next_page_token

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    # Loop to generate 5 pages of search results
    for _ in range(5):
        video_list, next_page_token = youtube_search(query_term, max_results)
        if len(video_list) != 0:
            print(video_list)
        
        if next_page_token:
            print("Next page--------------------------------")
            video_list, next_page_token = youtube_search(query_term, max_results, page_token=next_page_token)
            if len(video_list) != 0:
                print(video_list)
        else:
            break  # No more pages available, exit the loop

    