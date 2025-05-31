import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not defined in .env")

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

# Search for Veritasium channel
search_response = youtube.search().list(
    part='snippet',
    q='Veritasium',
    type='channel',
    maxResults=1
).execute()
channel_id = search_response['items'][0]['id']['channelId']

# Get recent videos from the channel
video_response = youtube.search().list(
    part='snippet',
    channelId=channel_id,
    maxResults=50,
    order='date',
    type='video'
).execute()

# Store rows for each comment
rows = []

for video in video_response['items']:
    video_id = video['id']['videoId']
    video_title = video['snippet']['title']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    published_at = video['snippet']['publishedAt']
    channel_title = video['snippet']['channelTitle']

    # Get top-level comments for the video
    try:
        comments_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=50,
            textFormat='plainText'
        ).execute()

        for item in comments_response.get('items', []):
            comment_data = item['snippet']['topLevelComment']['snippet']
            comment_text = comment_data['textDisplay'].replace('\n', ' ')
            author = comment_data['authorDisplayName']
            comment_date = comment_data['publishedAt']
            like_count = comment_data['likeCount']

            rows.append({
                "Video Title": video_title,
                "Video URL": video_url,
                "Published Date": published_at,
                "Channel Title": channel_title,
                "Comment": comment_text,
                "Comment Author": author,
                "Comment Published": comment_date,
                "Like Count (Comment)": like_count
            })

    except Exception as e:
        # Add placeholder row in case of failure
        rows.append({
            "Video Title": video_title,
            "Video URL": video_url,
            "Published Date": published_at,
            "Channel Title": channel_title,
            "Comment": "Comments not available",
            "Comment Author": None,
            "Comment Published": None,
            "Like Count (Comment)": None
        })

# Create DataFrame
df = pd.DataFrame(rows)
df.to_csv("../data/Veritasium_comments.csv")
#Excel for visualization
#df.to_excel("../data/veritasium_comments_detailed.xlsx")



