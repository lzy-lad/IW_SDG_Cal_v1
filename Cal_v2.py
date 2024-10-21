import streamlit as st

# Function to define SDGs and their keywords
def get_sdg_data():
    return {
        "No Poverty": {
            "keywords": ["poverty", "hunger", "economic growth", "inequality"],
            "description": "End poverty in all its forms everywhere."
        },
        "Zero Hunger": {
            "keywords": ["hunger", "nutrition", "agriculture", "food security"],
            "description": "End hunger, achieve food security and improved nutrition, and promote sustainable agriculture."
        },
        "Good Health and Well-being": {
            "keywords": ["health", "well-being", "medical", "disease", "mental health"],
            "description": "Ensure healthy lives and promote well-being for all at all ages."
        }
        # Add more SDGs here...
    }

# Function to match project description to SDGs
def match_sdgs(project_desc, sdg_data):
    matched_sdgs = []
    for sdg, data in sdg_data.items():
        if any(keyword.lower() in project_desc.lower() for keyword in data['keywords']):
            matched_sdgs.append(sdg)
    return matched_sdgs

# Function to display matched SDGs and their descriptions
def display_results(matched_sdgs, sdg_data):
    st.subheader("Relevant SDGs for Your Project")
    if matched_sdgs:
        for sdg in matched_sdgs:
            st.success(f"**{sdg}**: {sdg_data[sdg]['description']}")
    else:
        st.warning("No SDG matches found. You might want to refine your project description.")
        st.info("Tip: Try using keywords related to social impact, poverty, hunger, health, education, and more.")

# Main UI
def main():
    st.title("🌍 SDG Alignment Calculator")
    st.write("Describe your project, and we'll help you align it with the United Nations Sustainable Development Goals (SDGs).")
    
    # Input area for project description
    project_desc = st.text_area("Enter your project description:", height=150, placeholder="E.g., a program to improve local nutrition and food security in rural areas.")
    
    if st.button("Find Relevant SDGs"):
        sdg_data = get_sdg_data()
        matched_sdgs = match_sdgs(project_desc, sdg_data)
        display_results(matched_sdgs, sdg_data)
    
    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool helps NGOs and social organizations align their projects with the UN's SDGs.")
        st.write("Simply describe your project, and we'll find relevant SDGs based on keywords that match the goals.")

# Run the app
if __name__ == "__main__":
    main()
