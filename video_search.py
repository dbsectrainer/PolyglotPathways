from googleapiclient.discovery import build
import json
import os
import time
import re

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def init_youtube():
    """Initialize YouTube API client"""
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_topic(identifier, language_code="en"):
    """Get search topics based on content type and language"""
    # Language-specific search terms
    language_terms = {
        'en': {'name': 'English', 'term': 'english lesson tutorial'},
        'es': {'name': 'Spanish', 'term': 'español lección tutorial'},
        'pt': {'name': 'Portuguese', 'term': 'português aula tutorial'},
        'fr': {'name': 'French', 'term': 'français leçon tutoriel'},
        'de': {'name': 'German', 'term': 'deutsch unterricht tutorial'}
    }

    # Base topics for each day
    topics = {
        # Basic Vocabulary (Days 1-7)
        1: "pronunciation basics",
        2: "numbers counting",
        3: "time expressions",
        4: "basic verbs actions",
        5: "basic adjectives",
        6: "question words",
        7: "basic grammar",

        # Advanced Communication (Days 8-15)
        8: "shopping transportation phrases",
        9: "dining restaurant phrases",
        10: "directions navigation",
        11: "basic grammar patterns",
        12: "travel survival phrases",
        13: "public transport phrases",
        14: "daily communication",
        15: "family relationships vocabulary",

        # Global Living (Days 16-26)
        16: "social interactions phrases",
        17: "cultural etiquette",
        18: "festivals traditions",
        19: "home life vocabulary",
        20: "public places vocabulary",
        21: "cultural customs",
        22: "social norms",
        23: "workplace vocabulary",
        24: "business etiquette",
        25: "online meetings phrases",
        26: "remote work vocabulary",

        # Tech Professional (Days 27-31)
        27: "email writing phrases",
        28: "presentations phrases",
        29: "technical terms vocabulary",
        30: "professional conduct",
        31: "formal expressions",

        # Advanced Professional (Days 32-50)
        32: "idioms expressions",
        33: "formal expressions",
        34: "casual slang",
        35: "debate discussion phrases",
        36: "storytelling phrases",
        37: "persuasive speech",
        38: "advanced dialogue",
        39: "role play scenarios",
        40: "complex conversations",
        41: "business negotiations",
        42: "academic presentations",
        43: "professional writing",
        44: "advanced grammar",
        45: "cultural differences",
        46: "business meetings",
        47: "job interviews",
        48: "professional networking",
        49: "public speaking",
        50: "advanced communication"
    }

    base_topic = topics.get(identifier, "language lesson")
    lang_info = language_terms.get(language_code, language_terms['en'])
    # Ensure every search includes "lesson tutorial" while maintaining language-specific terms
    return f"learn {base_topic} lesson tutorial {lang_info['term']}"

# List of preferred educational channels for each language
PREFERRED_CHANNELS = {
    'en': [
        "BBC Learning English",
        "English with Lucy",
        "engVid",
        "JamesESL English Lessons"
    ],
    'es': [
        "Why Not Spanish?",
        "SpanishPod101",
        "Butterfly Spanish",
        "Why Not Spanish?"
    ],
    'pt': [
        "Portuguese With Carla",
        "Speaking Brazilian",
        "Portuguese Lab",
        "Learn Portuguese With Brazilian Portuguese"
    ],
    'fr': [
        "French With Alexa",
        "FrenchPod101",
        "Easy French",
        "French Truly"
    ],
    'de': [
        "Learn German with Anja",
        "GermanPod101",
        "Easy German",
        "Deutsch für Euch"
    ]
}

def search_youtube_video(youtube, query, language_code="en", max_results=10, retry_count=0):
    """Search for a language learning video matching criteria"""
    try:
        print(f"Searching for: {query}")
        
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            videoDefinition='high',
            videoEmbeddable='true',
            maxResults=max_results
        )
        response = request.execute()
        
        video_ids = [item['id']['videoId'] for item in response['items']]
        if not video_ids:
            print("No videos found in search results")
            return None
            
        duration_request = youtube.videos().list(
            part='contentDetails,statistics,snippet',
            id=','.join(video_ids)
        )
        duration_response = duration_request.execute()
        
        preferred_videos = []
        other_videos = []
        
        for video in duration_response['items']:
            duration = parse_duration(video['contentDetails']['duration'])
            views = int(video['statistics']['viewCount'])
            channel_title = video['snippet']['channelTitle']
            
            # Check if video is from a preferred channel for the language
            is_preferred = any(
                re.search(channel, channel_title, re.IGNORECASE) 
                for channel in PREFERRED_CHANNELS.get(language_code, [])
            )
            
            # Videos between 3-15 minutes
            if 180 <= duration <= 900:
                if is_preferred:
                    preferred_videos.append((video['id'], views, channel_title))
                else:
                    other_videos.append((video['id'], views, channel_title))
        
        # Sort by views
        preferred_videos.sort(key=lambda x: x[1], reverse=True)
        other_videos.sort(key=lambda x: x[1], reverse=True)
        
        if preferred_videos:
            print(f"Found {len(preferred_videos)} videos from preferred channels")
            return preferred_videos[0][0]
        elif other_videos:
            print("Using video from non-preferred channel")
            return other_videos[0][0]
        else:
            print("No suitable videos found")
            return video_ids[0] if video_ids else None
        
    except Exception as e:
        if "quota" in str(e).lower() and retry_count < 3:
            # Exponential backoff for quota errors
            wait_time = (2 ** retry_count) * 60  # 1min, 2min, 4min
            print(f"Quota exceeded. Waiting {wait_time} seconds before retry...")
            time.sleep(wait_time)
            return search_youtube_video(youtube, query, language_code, max_results, retry_count + 1)
        print(f"Error searching YouTube: {e}")
        return None

def parse_duration(duration):
    """Convert YouTube duration format to seconds"""
    match = re.match(r'PT(\d+H)?(\d+M)?(\d+S)?', duration)
    if not match:
        return 0
    
    hours = int(match.group(1)[:-1]) if match.group(1) else 0
    minutes = int(match.group(2)[:-1]) if match.group(2) else 0
    seconds = int(match.group(3)[:-1]) if match.group(3) else 0
    
    return hours * 3600 + minutes * 60 + seconds

def update_videos_json(videos):
    """Update videos.json with new video IDs"""
    try:
        with open('videos.json', 'w') as f:
            json.dump(videos, f, indent=2)
        print("Successfully updated videos.json")
        return True
    except Exception as e:
        print(f"Error updating videos.json: {e}")
        return False

def main():
    if not YOUTUBE_API_KEY:
        print("Error: YOUTUBE_API_KEY environment variable not set")
        return
    
    youtube = init_youtube()
    languages = ['en', 'es', 'pt', 'fr', 'de']
    
    try:
        # Initialize videos dictionary with consistent nested structure
        videos = {}
        if os.path.exists('videos.json'):
            with open('videos.json', 'r') as f:
                old_videos = json.load(f)
                # Convert flat structure to nested if needed
                for key, value in old_videos.items():
                    if '_' in key:  # Handle flat keys like "day1_en"
                        day, lang = key.rsplit('_', 1)
                        if day not in videos:
                            videos[day] = {}
                        videos[day][lang] = value
                    elif isinstance(value, dict):  # Already nested structure
                        videos[key] = value
                    else:  # Handle any other format
                        day_num = key.replace('day', '')
                        if f'day{day_num}' not in videos:
                            videos[f'day{day_num}'] = {'en': '', 'es': '', 'pt': '', 'fr': '', 'de': ''}
        
        # Process one day at a time for all languages
        for day in range(1, 51):
            print(f"\nProcessing Day {day} for all languages")
            day_key = f"day{day}"
            if day_key not in videos:
                videos[day_key] = {'en': '', 'es': '', 'pt': '', 'fr': '', 'de': ''}
            
            # Process each language for this day
            for lang in languages:
                print(f"\nProcessing language: {lang} for Day {day}")
                
                # Skip if we already have this video
                if videos[day_key][lang]:
                    print(f"Already have video for day {day} in {lang}")
                    continue
                
                topic = get_topic(day, lang)
                print(f"Searching for videos...")
                video_id = search_youtube_video(youtube, topic, lang)
                
                if video_id:
                    videos[day_key][lang] = video_id
                    print(f"Found video: https://youtube.com/watch?v={video_id}")
                    # Save progress after each video
                    update_videos_json(videos)
                else:
                    print("No suitable video found")
                
                # Respect YouTube API quotas
                time.sleep(1)
                
    except Exception as e:
        print(f"Error processing videos: {e}")

if __name__ == "__main__":
    main()
