# Filename: sdg_calculator.py
import streamlit as st

# Define SDG keywords
sdg_keywords = {
    "No Poverty": ["poverty", "hunger", "economic growth", "inequality"],
    "Zero Hunger": ["hunger", "nutrition", "agriculture", "food security"],
    "Good Health and Well-being": ["health", "well-being", "medical", "disease", "mental health"],
    # Add more SDG mappings as necessary
}

# Streamlit App
st.title("SDG Alignment Calculator")
st.write("Enter your project description, and we'll help you align it with relevant Sustainable Development Goals (SDGs).")

# Text input for project description
project_desc = st.text_area("Describe your project:", height=150)

# Button to calculate SDG alignment
if st.button("Find Relevant SDGs"):
    matched_sdgs = []
    for sdg, keywords in sdg_keywords.items():
        if any(keyword.lower() in project_desc.lower() for keyword in keywords):
            matched_sdgs.append(sdg)
    
    if matched_sdgs:
        st.success(f"Your project aligns with the following SDGs: {', '.join(matched_sdgs)}")
    else:
        st.warning("No SDG matches found. Please refine your description.")
