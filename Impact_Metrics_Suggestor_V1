import streamlit as st

# Define SDGs and their associated impact metrics
def get_sdg_metrics():
    return {
        "No Poverty": [
            "Number of individuals lifted above poverty line",
            "Percentage increase in household income",
            "Number of people provided with access to financial services"
        ],
        "Zero Hunger": [
            "Number of people provided with food assistance",
            "Increase in crop yield for small-scale farmers",
            "Reduction in malnutrition rates"
        ],
        "Good Health and Well-being": [
            "Number of people provided with essential healthcare services",
            "Reduction in maternal mortality rate",
            "Increase in vaccination rates"
        ],
        "Quality Education": [
            "Number of children enrolled in primary education",
            "Improvement in literacy rates",
            "Number of teachers trained"
        ],
        "Gender Equality": [
            "Percentage increase in women's workforce participation",
            "Reduction in gender-based violence cases",
            "Number of girls receiving secondary education"
        ],
        "Clean Water and Sanitation": [
            "Number of people provided with access to clean water",
            "Reduction in waterborne diseases",
            "Number of households with improved sanitation facilities"
        ],
        "Affordable and Clean Energy": [
            "Number of households provided with access to electricity",
            "Percentage increase in renewable energy usage",
            "Reduction in carbon emissions from energy production"
        ],
        "Decent Work and Economic Growth": [
            "Number of jobs created",
            "Increase in GDP per capita",
            "Reduction in youth unemployment rate"
        ],
        "Industry, Innovation and Infrastructure": [
            "Increase in R&D expenditure as a proportion of GDP",
            "Number of new patents filed",
            "Kilometers of new or improved roads/railways"
        ],
        "Reduced Inequality": [
            "Reduction in income inequality (Gini coefficient)",
            "Increase in social mobility index",
            "Percentage of population covered by social protection systems"
        ],
        "Sustainable Cities and Communities": [
            "Reduction in urban air pollution levels",
            "Increase in green spaces per capita",
            "Percentage of population with access to public transportation"
        ],
        "Responsible Consumption and Production": [
            "Reduction in food waste per capita",
            "Increase in recycling rates",
            "Number of companies adopting sustainable practices"
        ],
        "Climate Action": [
            "Reduction in greenhouse gas emissions",
            "Number of people benefiting from climate adaptation measures",
            "Increase in climate-resilient infrastructure"
        ],
        "Life Below Water": [
            "Increase in marine protected areas",
            "Reduction in ocean plastic pollution",
            "Improvement in fish stock levels"
        ],
        "Life on Land": [
            "Increase in forest cover",
            "Number of endangered species protected",
            "Reduction in land degradation"
        ],
        "Peace, Justice and Strong Institutions": [
            "Reduction in corruption perception index",
            "Increase in voter turnout",
            "Improvement in rule of law index"
        ],
        "Partnerships for the Goals": [
            "Increase in development assistance",
            "Number of multi-stakeholder partnerships formed",
            "Improvement in data availability for SDG monitoring"
        ]
    }

def suggest_metrics(selected_sdgs):
    sdg_metrics = get_sdg_metrics()
    suggested_metrics = {}
    for sdg in selected_sdgs:
        suggested_metrics[sdg] = sdg_metrics.get(sdg, [])
    return suggested_metrics

def main():
    st.title("🎯 Impact Metrics Suggester")
    st.write("Select the SDGs your project aligns with, and we'll suggest relevant impact metrics to track your progress.")

    sdg_metrics = get_sdg_metrics()
    selected_sdgs = st.multiselect("Select SDGs your project aligns with:", list(sdg_metrics.keys()))

    if st.button("Suggest Metrics"):
        if selected_sdgs:
            suggested_metrics = suggest_metrics(selected_sdgs)
            st.subheader("Suggested Impact Metrics:")
            for sdg, metrics in suggested_metrics.items():
                with st.expander(f"{sdg}"):
                    for metric in metrics:
                        st.write(f"• {metric}")
        else:
            st.warning("Please select at least one SDG to get metric suggestions.")

    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool helps organizations identify relevant impact metrics for their SDG-aligned projects.")
        st.write("By tracking these metrics, you can measure and communicate your project's impact more effectively.")
        st.write("Remember to adapt these suggestions to your specific project context and local conditions.")

if __name__ == "__main__":
    main()
