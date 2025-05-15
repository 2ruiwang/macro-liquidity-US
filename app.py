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

# Extract latest values
metrics = {}

if fred_data and hyg_series is not None:
    try:
        # WALCL
        walcl_val = fred_data["WALCL"].iloc[-1].value / 1e6  # Convert to Trillions
        score, comment = score_walcl(walcl_val)
        metrics["WALCL"] = (f"{walcl_val:.1f}T", score, comment)

        # TGA
        tga_val = fred_data["TGA"].iloc[-1].value / 1e3  # Convert to Billions
        score, comment = score_tga(tga_val)
        metrics["TGA"] = (f"{tga_val:.0f}B", score, comment)

        # WRESBAL
        wresbal_val = fred_data["WRESBAL"].iloc[-1].value / 1e6
        score, comment = score_wresbal(wresbal_val)
        metrics["WRESBAL"] = (f"{wresbal_val:.1f}T", score, comment)

        # RRPONTSYD
        rrp_val = fred_data["RRPONTSYD"].iloc[-1].value / 1e3
        score, comment = score_rrp(rrp_val)
        metrics["RRPONTSYD"] = (f"{rrp_val:.0f}B", score, comment)

        # SOFR
        sofr_val = fred_data["SOFR"].iloc[-1].value
        score, comment = score_sofr(sofr_val)
        metrics["SOFR"] = (f"{sofr_val:.2f}%", score, comment)

        # HYG Trend
        hyg_change_5d = (hyg_series.iloc[-1] - hyg_series.iloc[-6]) / hyg_series.iloc[-6] * 100
        score, comment = score_hyg_trend(hyg_change_5d)
        metrics["HYG"] = (f"{hyg_series.iloc[-1]:.2f} ({hyg_change_5d:+.1f}%)", score, comment)
    except Exception as e:
        st.error(f"Error processing data: {e}")
else:
    st.warning("Waiting for data to load...")

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
