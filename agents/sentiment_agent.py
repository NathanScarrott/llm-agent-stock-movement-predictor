import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from openrouter import call_openrouter
from tools.data_collectors.sentiment.reddit import get_reddit_posts
from tools.data_collectors.sentiment.yahoo import get_yahoo_news
from tools.data_collectors.sentiment.alpha import get_alpha_sentiment


def get_sentiment_news(ticker: str, service: str):
    """
    Sentiment agent that uses the Yahoo Finance market data to get the sentiment of the ticker
    """
    if service == "yahoo":
        yahoo_news = get_yahoo_news(ticker)
        return yahoo_news
    elif service == "alpha":
        alpha_sentiment = get_alpha_sentiment(ticker)
        return alpha_sentiment
    elif service == "reddit":
        subreddits = ["stocks", "investing", "wallstreetbets"]
        terms = [ticker, ticker.lower(), f"${ticker}"]
        reddit_sentiment = get_reddit_posts(subreddits, terms, time_filter="month", limit=7)
        return reddit_sentiment
    else:
        raise ValueError(f"Invalid service: {service}")

def analyze_sentiment_batch(
    ticker: str,
    source: str,  
    model: str = "gpt-4o-mini",
    temperature: float = 0.5,
) -> str:
    raw_news = get_sentiment_news(ticker, source)

    # -------- format readable text -----------------------------------------
    if isinstance(raw_news, list):
        formatted_items = []
        idx = 1
        for item in raw_news:
            # PRAW Submission objects
            if hasattr(item, "title"):
                title = item.title
                body  = getattr(item, "selftext", "")
                # fetch top comment if available
                top_comment_text = ""
                try:
                    item.comments.replace_more(limit=0)
                    if len(item.comments) > 0:
                        top_comment_text = item.comments[0].body
                except Exception:
                    pass
                formatted_items.append(
                    f"POST {idx}\nTITLE: {title}\nBODY: {body}\nTOP_COMMENT: {top_comment_text}\n---"
                )
            # Alpha / Yahoo dict structure
            elif isinstance(item, dict) and "title" in item:
                title = item.get("title", "")
                summary = item.get("summary", "")
                formatted_items.append(f"POST {idx}: {title}\n{summary}")
            else:
                formatted_items.append(f"POST {idx}: {str(item)}")
            idx += 1
        news_block = "\n\n".join(formatted_items)
    else:
        news_block = str(raw_news)

    if source == "yahoo":
        intro = "news articles about a market from Yahoo Finance"
    elif source == "alpha":
        intro = "news articles about a market from Alpha Vantage"
    elif source == "reddit":
        intro = "Reddit posts about a market from Reddit"
    else:
        intro = f"items about {ticker} from {source}"

    prompt = f"""
    You are a financial sentiment analyst. You will be given a list of {intro}. Your aim is to analyze the sentiment of the {source} data.

    Here is the news:
    {news_block}

    First analyze the sentiment of each news article. Give a score between 0 and 10 for the sentiment of the news article. Do this in <sentiment_score> tags.

    Next, analyze the importace of each news article. Give a score between 0 and 10 for the importance of the news article. Do this in <importance_score> tags.

    Then, give a score between 0 and 10 for the overall sentiment of the news articles considering the sentiment of each news and the importance of each news article.

    Afterwards, summarise your findings ensuring to include all relevant and important information.

    Return the sentiment score for each news article and the overall sentiment score between <answer> tags in the following JSON format:

    <answer>
    {{
        "summary": "summary of the news articles",
        "overall_sentiment_score": "score between 0 and 10"
    }}
    </answer>
    """
    print("--------------------------------")
    print(prompt)
    print("--------------------------------")

    response = call_openrouter(
        prompt,
        system_prompt=f"You are a financial sentiment analyst. You will be given a list of {intro}. Your aim is to analyze the sentiment of the {source} data.",
        model=model,
        temperature=temperature
    )
    return response

if __name__ == "__main__":
    response = analyze_sentiment_batch("AAPL", "reddit")
    print(response)