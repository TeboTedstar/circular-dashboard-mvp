# circular-dashboard-mvp# Minimal Viable Product - Streamlit Dashboard

try:
    import streamlit as st
    import pandas as pd
except ModuleNotFoundError as e:
    print("\n[ERROR] Required modules not found.\n")
    print("Please install the required packages with:")
    print("pip install streamlit pandas\n")
    raise SystemExit(e)

kpi_data = {
    "Circular Jobs Created": 42,
    "% Waste Reused by Community": "65%",
    "SMMEs Engaged": 18,
    "Innovation Pilots": 5
}

waste_data = pd.DataFrame({
    "Waste Type": ["Scrap Metal", "Pallets", "Plastic Waste"],
    "Quantity (tons)": [12.5, 7.8, 3.2],
    "Reuse Application": ["Artisanal Furniture", "Brick Making", "Eco Bricks"]
})

innovation_timeline = [
    {"title": "Slag Brick Pilot", "partner": "BrickCo", "status": "Scaling"},
    {"title": "Plastic to Pavers", "partner": "EcoBlock", "status": "Testing"},
    {"title": "Scrap Sculpture", "partner": "YouthForge", "status": "Completed"}
]

stories = [
    {"name": "Sipho M.", "story": "We turned waste pallets into school desks.", "project": "Wood4Change"},
    {"name": "Lindiwe K.", "story": "Plastic waste now powers our co-op with eco bricks.", "project": "GreenMakers"}
]

def main():
    st.set_page_config(page_title="Circular Innovation Dashboard", layout="wide")
    st.title("🌍 Community & Circular Innovation Dashboard")

    st.subheader("Key Impact Metrics")
    kpi_cols = st.columns(len(kpi_data))
    for i, (label, value) in enumerate(kpi_data.items()):
        kpi_cols[i].metric(label=label, value=value)

    st.subheader("♻️ Reuse Streams")
    st.dataframe(waste_data, use_container_width=True)

    st.subheader("🚀 Innovation Pilots")
    for item in innovation_timeline:
        st.markdown(f"**{item['title']}** by *{item['partner']}* — `{item['status']}`")

    st.subheader("🧑🏽‍🤝‍🧑🏿 Community Stories")
    for s in stories:
        st.info(f"**{s['name']}** from *{s['project']}*: {s['story']}")

if __name__ == "__main__":
    main()
