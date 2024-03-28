import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=query_term, part="id,snippet", maxResults=max_results, type="video").execute()
    
    search_list = []
    for item in search_response['items']:
        search_list.append(item)
    
    return search_list

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    reponse = youtube_search(query_term, max_results)
    print(reponse)