#!/usr/bin/env python3
"""Yahoo Finance news collector - fixed version"""

import yfinance as yf
from datetime import datetime
import json
import os
from typing import Dict, List, Optional

def get_yahoo_news(ticker: str, max_results: int = 10):
    """
    Get Yahoo Finance news for a ticker with proper error handling
    
    Args:
        ticker: Stock symbol (e.g., "AAPL")
        max_results: Maximum number of articles to return
    
    Returns:
        Tuple of (news_titles, news_summaries, full_articles)
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        
        news_titles = []
        news_summaries = []
        full_articles = []
        
        for i, news_item in enumerate(news[:max_results]):
                if 'content' in news_item:
                    content = news_item['content']
                    title = content.get('title', 'No title')
                    summary = content.get('summary', 'No summary')
                    
                    # Additional metadata
                    article_data = {
                        'title': title,
                        'summary': summary,
                    }
                else:
                   print(f"Error processing article {i}: {news_item}")
                
                news_titles.append(title)
                news_summaries.append(summary)
                full_articles.append(article_data)
                
        return news_titles, news_summaries, full_articles
        
    except Exception as e:
        print(f"Error fetching news for {ticker}: {e}")
        return [], [], []


def main(ticker="AAPL"):
    titles, summaries, articles = get_yahoo_news(ticker, max_results=5)
    
    for i, article in enumerate(articles[:3]):
        print(f"\n{i+1}. {article['title']}")
        print(f"   Summary: {article['summary'][:100]}...")
