import streamlit as st
from datetime import datetime
from fetch_data import fetch_all_fred, fetch_hyg_price
from score_metrics import (
    score_walcl, score_tga, score_wresbal,
    score_rrp, score_sofr, score_hyg_trend
)

st.set_page_config(page_title="Macro Liquidity Dashboard", layout="wide")

st.title("📊 Macro Liquidity Dashboard (Live Data)")
st.markdown(f"**Last Updated:** {datetime.today().strftime('%B %d, %Y')}")

# Fetch data
fred_data = fetch_all_fred()
hyg_series = fetch_hyg_price()

metrics = {}

try:
    def safe_last(series, divide_by=1):
        if series is not None and not series.empty:
            return float(series["value"].astype(float).iloc[-1]) / divide_by
        return None

    walcl_val = safe_last(fred_data["WALCL"], 1e6)
    tga_val = safe_last(fred_data["TGA"], 1e3)
    wresbal_val = safe_last(fred_data["WRESBAL"], 1e6)
    rrp_val = safe_last(fred_data["RRPONTSYD"], 1e3)
    sofr_val = safe_last(fred_data["SOFR"], 1)

    # Score and format each
    if walcl_val is not None:
        s, c = score_walcl(walcl_val)
        metrics["WALCL"] = (f"{walcl_val:.1f}T", s, c)

    if tga_val is not None:
        s, c = score_tga(tga_val)
        metrics["TGA"] = (f"{tga_val:.0f}B", s, c)

    if wresbal_val is not None:
        s, c = score_wresbal(wresbal_val)
        metrics["WRESBAL"] = (f"{wresbal_val:.1f}T", s, c)

    if rrp_val is not None:
        s, c = score_rrp(rrp_val)
        metrics["RRPONTSYD"] = (f"{rrp_val:.0f}B", s, c)

    if sofr_val is not None:
        s, c = score_sofr(sofr_val)
        metrics["SOFR"] = (f"{sofr_val:.2f}%", s, c)

    if hyg_series is not None and len(hyg_series) >= 6:
        hyg_change = (hyg_series.iloc[-1] - hyg_series.iloc[-6]) / hyg_series.iloc[-6] * 100
        s, c = score_hyg_trend(hyg_change)
        metrics["HYG"] = (f"{hyg_series.iloc[-1]:.2f} ({hyg_change:+.1f}%)", s, c)
    else:
        metrics["HYG"] = ("N/A", 0, "Not enough data for HYG trend.")

except Exception as e:
    st.error(f"Error processing data: {e}")


# Tier layout
tier_map = {
    "Tier 1 – Base Liquidity": ["WALCL", "TGA"],
    "Tier 2 – Market Liquidity": ["WRESBAL", "RRPONTSYD"],
    "Tier 3 – Cost & Sentiment": ["SOFR", "HYG"]
}

score_icons = {3: "🟢", 2: "🟡", 1: "🔴", 0: "🔴"}

# Display results
for tier, keys in tier_map.items():
    st.subheader(tier)
    cols = st.columns(len(keys))
    for i, key in enumerate(keys):
        if key in metrics:
            val, score, comment = metrics[key]
            with cols[i]:
                st.metric(label=key, value=val, delta=f"Score: {score} {score_icons.get(score, '')}")
                st.caption(comment)
