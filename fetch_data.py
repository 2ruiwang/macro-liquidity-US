import os
import requests
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import streamlit as st

FRED_API_KEY = st.secrets["FRED_API_KEY"]

FRED_SERIES = {
    "WALCL": "WALCL",
    "TGA": "WDTGAL",
    "WRESBAL": "WRESBAL",
    "RRPONTSYD": "RRPONTSYD",
    "SOFR": "SOFR"
}

def fetch_fred_series(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    data = response.json()["observations"]
    df = pd.DataFrame(data)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["value"]).set_index("date").sort_index()
    return df

def fetch_all_fred():
    return {key: fetch_fred_series(sid) for key, sid in FRED_SERIES.items()}

def fetch_hyg_price():
    end = datetime.today()
    start = end - timedelta(days=30)
    df = yf.download("HYG", start=start, end=end)
    if df.empty:
        return None
    return df["Close"]
