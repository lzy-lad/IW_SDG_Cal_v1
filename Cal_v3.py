import streamlit as st

# Function to define SDGs and their keywords (unchanged)
def get_sdg_data():
    return {
        "No Poverty": {
            "keywords": ["poverty", "inequality", "economic growth", "income", "unemployment", "social protection", "vulnerable", "access to resources"],
            "description": "End poverty in all its forms everywhere."
        },
        "Zero Hunger": {
            "keywords": ["hunger", "nutrition", "food security", "agriculture", "farming", "sustainable agriculture", "malnutrition", "crop production"],
            "description": "End hunger, achieve food security and improved nutrition, and promote sustainable agriculture."
        },
        "Good Health and Well-being": {
            "keywords": ["health", "well-being", "disease", "mental health", "medical care", "vaccines", "hygiene", "pandemic", "sanitation", "healthcare access"],
            "description": "Ensure healthy lives and promote well-being for all at all ages."
        },
        "Quality Education": {
            "keywords": ["education", "learning", "schooling", "literacy", "early childhood", "teacher training", "inclusive education", "vocational training", "skills development"],
            "description": "Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all."
        },
        "Gender Equality": {
            "keywords": ["gender", "women", "girls", "discrimination", "violence against women", "female empowerment", "gender equality", "equal pay", "access to education"],
            "description": "Achieve gender equality and empower all women and girls."
        },
        "Clean Water and Sanitation": {
            "keywords": ["water", "sanitation", "hygiene", "clean water", "water resources", "wastewater", "pollution", "access to water", "sustainable water management"],
            "description": "Ensure availability and sustainable management of water and sanitation for all."
        },
        "Affordable and Clean Energy": {
            "keywords": ["energy", "renewable energy", "clean energy", "solar power", "wind energy", "energy efficiency", "affordable energy", "sustainable energy", "access to electricity"],
            "description": "Ensure access to affordable, reliable, sustainable, and modern energy for all."
        },
        "Decent Work and Economic Growth": {
            "keywords": ["economic growth", "employment", "jobs", "labor market", "decent work", "unemployment", "entrepreneurship", "economic productivity", "equal pay"],
            "description": "Promote sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all."
        },
        "Industry, Innovation and Infrastructure": {
            "keywords": ["infrastructure", "innovation", "industrialization", "technology", "research", "development", "sustainable industries", "manufacturing", "resilient infrastructure"],
            "description": "Build resilient infrastructure, promote inclusive and sustainable industrialization, and foster innovation."
        },
        "Reduced Inequality": {
            "keywords": ["inequality", "social inequality", "discrimination", "income inequality", "social inclusion", "disparities", "disabilities", "economic disparity"],
            "description": "Reduce inequality within and among countries."
        },
        "Sustainable Cities and Communities": {
            "keywords": ["urbanization", "cities", "sustainable cities", "housing", "slums", "urban planning", "public transport", "sustainability", "community development"],
            "description": "Make cities and human settlements inclusive, safe, resilient, and sustainable."
        },
        "Responsible Consumption and Production": {
            "keywords": ["sustainable consumption", "sustainable production", "waste", "resource efficiency", "recycling", "food waste", "environmental impact", "eco-friendly"],
            "description": "Ensure sustainable consumption and production patterns."
        },
        "Climate Action": {
            "keywords": ["climate change", "global warming", "carbon emissions", "climate resilience", "environmental protection", "disaster risk", "climate policies", "renewable energy"],
            "description": "Take urgent action to combat climate change and its impacts."
        },
        "Life Below Water": {
            "keywords": ["oceans", "marine life", "fisheries", "water pollution", "marine conservation", "sustainable fishing", "coral reefs", "plastic waste", "ocean health"],
            "description": "Conserve and sustainably use the oceans, seas, and marine resources for sustainable development."
        },
        "Life on Land": {
            "keywords": ["forests", "biodiversity", "deforestation", "land degradation", "ecosystems", "wildlife", "desertification", "land conservation", "sustainable land use"],
            "description": "Protect, restore, and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt biodiversity loss."
        },
        "Peace, Justice and Strong Institutions": {
            "keywords": ["peace", "justice", "institutions", "governance", "rule of law", "human rights", "violence prevention", "corruption", "inclusive societies"],
            "description": "Promote peaceful and inclusive societies, provide access to justice for all, and build effective, accountable institutions."
        },
        "Partnerships for the Goals": {
            "keywords": ["partnerships", "collaboration", "international cooperation", "public-private partnerships", "global goals", "resource mobilization", "capacity building", "shared responsibility"],
            "description": "Strengthen the means of implementation and revitalize the global partnership for sustainable development."
        }
    }

# Function to match project description to SDGs (improved with relevance score)
def match_sdgs(project_desc, sdg_data):
    matched_sdgs = []
    for sdg, data in sdg_data.items():
        relevance_score = sum(project_desc.lower().count(keyword.lower()) for keyword in data['keywords'])
        if relevance_score > 0:
            matched_sdgs.append((sdg, relevance_score))
    return sorted(matched_sdgs, key=lambda x: x[1], reverse=True)

# Function to display matched SDGs and their descriptions (improved with relevance score)
def display_results(matched_sdgs, sdg_data):
    st.subheader("Relevant SDGs for Your Project")
    if matched_sdgs:
        for sdg, score in matched_sdgs:
            with st.expander(f"{sdg} (Relevance Score: {score})"):
                st.write(f"**Description:** {sdg_data[sdg]['description']}")
                st.write("**Key Words:** " + ", ".join(sdg_data[sdg]['keywords']))
                st.write(f"**Suggested Actions:**")
                st.write("1. Review the SDG targets and indicators")
                st.write("2. Align your project goals with specific SDG targets")
                st.write("3. Consider partnerships with organizations working on this SDG")
    else:
        st.warning("No SDG matches found. You might want to refine your project description.")
        st.info("Tip: Try using keywords related to social impact, poverty, hunger, health, education, and more.")

# Function to provide real-time feedback
def provide_feedback(project_desc, sdg_data):
    all_keywords = set()
    for data in sdg_data.values():
        all_keywords.update(data['keywords'])
    
    found_keywords = [keyword for keyword in all_keywords if keyword.lower() in project_desc.lower()]
    
    if found_keywords:
        st.success(f"Great! Your description includes SDG-related keywords: {', '.join(found_keywords)}")
    else:
        st.info("Tip: Try including keywords related to specific SDGs to improve matching.")

# Main UI
def main():
    st.title("🌍 SDG Alignment Calculator")
    st.write("Describe your project, and we'll help you align it with the United Nations Sustainable Development Goals (SDGs).")
    
    # Input area for project description
    project_desc = st.text_area("Enter your project description:", height=150, placeholder="E.g., a program to improve local nutrition and food security in rural areas.")
    
    sdg_data = get_sdg_data()
    
    # Real-time feedback
    if project_desc:
        provide_feedback(project_desc, sdg_data)
    
    if st.button("Find Relevant SDGs"):
        matched_sdgs = match_sdgs(project_desc, sdg_data)
        display_results(matched_sdgs, sdg_data)
    
    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool helps NGOs and social organizations align their projects with the UN's SDGs.")
        st.write("Simply describe your project, and we'll find relevant SDGs based on keywords that match the goals.")
        st.write("The relevance score indicates how closely your project aligns with each SDG based on keyword matches.")

# Run the app
if __name__ == "__main__":
    main()
