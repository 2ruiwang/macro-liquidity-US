# 📊 Macro Liquidity Dashboard

A real-time Streamlit dashboard for tracking and scoring U.S. macro liquidity conditions using publicly available data from the Federal Reserve and financial markets.

This project provides a tiered, structured view of systemic liquidity through six key indicators, with weighted scoring and commentary to support financial analysis, macro trading, and economic monitoring.

---

## 🔍 What It Does

The dashboard monitors:
- 🧱 **Tier 1 – Base Liquidity**  
  - **WALCL**: Federal Reserve total assets (balance sheet size)  
  - **TGA**: U.S. Treasury General Account balance at the Fed  

- 💧 **Tier 2 – Market Liquidity**  
  - **WRESBAL**: Bank reserves held at the Fed  
  - **RRPONTSYD**: Reverse repurchase agreements (used by MMFs)  

- 💲 **Tier 3 – Cost & Sentiment**  
  - **SOFR**: Secured Overnight Financing Rate  
  - **HYG ETF**: Proxy for high-yield credit stress (OAS unavailable freely)

Each metric is scored from 0 (tight/stress) to 3 (loose/easy), with commentary and trendlines. Weighted scores are aggregated into a daily liquidity health index out of 30.

---

## 🚀 Features

- 📈 Inline sparklines for recent trends
- 🧠 Tiered structure for intuitive interpretation
- 🎯 Weighted scoring model (customizable)
- 💬 Commentary for each metric, updated daily
- 🌐 Deployed on Streamlit Cloud

---

## 📦 Requirements

- Python 3.9+
- `streamlit`
- `pandas`
- `yfinance`
- `requests`
- `plotly` or `matplotlib` (optional for trends)

Install via:

```bash
pip install -r requirements.txt
