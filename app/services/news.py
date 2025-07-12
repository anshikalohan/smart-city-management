import os
import requests

def get_public_safety_news(place_name="India"):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        print("Warning: NEWS_API_KEY not found. Skipping news fetch.")
        return []
    
    short_place = place_name.split(",")[0] if place_name else ""
    query = f"{short_place} public safety"

    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": api_key,
        "q": query,
        "language": "en",
        "country": "in",
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "results" in data and data["results"]:
            articles = [{
                "title": article["title"],
                "link": article["link"],
                "pubDate": article["pubDate"]
            } for article in data["results"] if article.get("title") and article.get("link")]
            return articles
        else:
            return []

    except Exception as e:
        print(f"Error fetching public safety news: {e}")
        return []
