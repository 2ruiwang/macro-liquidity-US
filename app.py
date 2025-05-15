
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Macro Liquidity Dashboard", layout="wide")

# Placeholder values for MVP
scores = {
    "WALCL": (6.9, 1, "Fed QT ongoing, liquidity contracting."),
    "TGA": (583, 1, "Treasury holding cash near upper bound."),
    "WRESBAL": (2.5, 2, "Neutral zone, but watch for declines."),
    "RRPONTSYD": (144, 1, "Excess liquidity mostly deployed."),
    "SOFR": (5.0, 2, "Stable overnight rate."),
    "HYG": (74.3, 2, "Credit markets appear stable."),
}

tier_map = {
    "Tier 1 – Base Liquidity": ["WALCL", "TGA"],
    "Tier 2 – Market Liquidity": ["WRESBAL", "RRPONTSYD"],
    "Tier 3 – Cost & Sentiment": ["SOFR", "HYG"]
}

st.title("📊 Macro Liquidity Dashboard (MVP)")
st.markdown(f"**Last Updated:** {datetime.today().strftime('%B %d, %Y')}")

for tier, metrics in tier_map.items():
    st.subheader(tier)
    cols = st.columns(len(metrics))
    for i, m in enumerate(metrics):
        value, score, comment = scores[m]
        color = "🟢" if score == 3 else "🟡" if score == 2 else "🔴"
        with cols[i]:
            st.metric(label=f"{m}", value=f"{value}", delta=f"Score: {score} {color}")
            st.caption(comment)

st.markdown("---")
st.info("This MVP uses placeholder values. Full version will connect to live APIs and include trends.")
    