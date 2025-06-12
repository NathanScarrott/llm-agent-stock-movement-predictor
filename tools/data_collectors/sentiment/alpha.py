import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_alpha_sentiment(ticker="AAPL", limit=20):
    """
    Get sentiment data from Alpha Vantage
    
    Args:
        ticker: Stock symbol (e.g., "AAPL") 
        limit: Max number of articles
    
    Returns:
        List of articles with sentiment scores
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        print("ALPHA_VANTAGE_API_KEY not found in .env file")
        return []
    
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&limit={limit}&apikey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "Error Message" in data:
            print(f"API Error: {data['Error Message']}")
            return []
        
        if "Note" in data:
            print(f"API Limit: {data['Note']}")
            return []
        
        articles = []
        if "feed" in data:
            for item in data["feed"]:
                # Find sentiment for our ticker
                ticker_sentiment = "Neutral"
                ticker_score = 0
                
                if "ticker_sentiment" in item:
                    for ts in item["ticker_sentiment"]:
                        if ts.get("ticker") == ticker:
                            ticker_sentiment = ts.get("ticker_sentiment_label", "Neutral")
                            ticker_score = float(ts.get("ticker_sentiment_score", 0))
                            break
                
                article = {
                    "title": item.get("title", ""),
                    "summary": item.get("summary", ""),
                    "overall_sentiment": item.get("overall_sentiment_label", "Neutral"),
                    "overall_score": float(item.get("overall_sentiment_score", 0)),
                    "ticker_sentiment": ticker_sentiment,
                }
                articles.append(article)
        
        return articles
        
    except Exception as e:
        print(f"Error: {e}")
        return []