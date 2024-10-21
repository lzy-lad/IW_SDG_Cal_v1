# Filename: sdg_calculator.py
import streamlit as st

# Define SDG keywords
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
