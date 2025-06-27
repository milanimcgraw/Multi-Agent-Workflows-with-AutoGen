import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load API key from .env file in root or above
load_dotenv(find_dotenv())
api_key = os.getenv("NEWSAPI_KEY")

def fetch_nvidia_news():
    url = (
        "https://newsapi.org/v2/everything?"
        "q=Nvidia&"
        "from=2025-05-24&"
        "to=2025-06-23&"
        "sortBy=publishedAt&"
        f"apiKey={api_key}"
    )

    response = requests.get(url)
    news_data = response.json()

    if news_data.get("status") == "ok":
        articles = news_data.get("articles", [])
        if articles:
            for article in articles:
                print(f"Title: {article.get('title')}")
                print(f"Published At: {article.get('publishedAt')}")
                print(f"Source: {article.get('source', {}).get('name')}")
                print(f"Description: {article.get('description')}\n")
        else:
            print("No news articles found for the specified date range.")
    else:
        print("Failed to fetch news articles. Please check the API key or network connection.")

if __name__ == "__main__":
    fetch_nvidia_news()