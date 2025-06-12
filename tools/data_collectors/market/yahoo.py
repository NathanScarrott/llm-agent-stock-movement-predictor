import yfinance as yf
from datetime import datetime
import json
import os
from typing import Dict, List, Optional

def get_yahoo_market_data(ticker: str, timeframe: str = "1d", interval: str = "1m"):
    """
    Get Yahoo Finance market data for a ticker with proper error handling
    
    Args:
        ticker: Stock symbol (e.g., "AAPL")
        timeframe: Timeframe (e.g., "1d", "1h", "1m")
        interval: Interval (e.g., "1m", "5m", "15m", "30m", "60m", "90m", "1h", "1d")
    
    Returns:
        Tuple of (open, high, low, close, volume)
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=timeframe, interval=interval)
        
        if data.empty:
            print(f"No data found for {ticker} in {timeframe} timeframe")
            return None
        else:
            print(f"Data found for {ticker} in {timeframe} timeframe")
            return data
        
    except Exception as e:
        print(f"Error getting market data for {ticker}: {e}")
        return None
    
    
    



            
