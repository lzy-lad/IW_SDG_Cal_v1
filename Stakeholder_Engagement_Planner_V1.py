import streamlit as st
import pandas as pd

def get_stakeholder_categories():
    return [
        "Government agencies",
        "Local communities",
        "NGOs and civil society organizations",
        "Donors and funders",
        "Private sector companies",
        "Academic institutions",
        "Media",
        "Beneficiaries",
        "Project team members",
        "Other"
    ]

def get_engagement_strategies():
    return [
        "Regular meetings",
        "Workshops and seminars",
        "Surveys and feedback forms",
        "Newsletters and reports",
        "Social media engagement",
        "Community events",
        "Focus group discussions",
        "Advisory committees",
        "Partnerships and collaborations",
        "Other"
    ]

def create_stakeholder_df():
    return pd.DataFrame(columns=["Stakeholder", "Category", "Interest/Influence", "Engagement Strategy"])

def add_stakeholder(df, stakeholder, category, interest_influence, strategy):
    new_row = pd.DataFrame({
        "Stakeholder": [stakeholder],
        "Category": [category],
        "Interest/Influence": [interest_influence],
        "Engagement Strategy": [strategy]
    })
    return pd.concat([df, new_row], ignore_index=True)

def main():
    st.title("🤝 Stakeholder Engagement Planner")
    st.write("Identify and plan engagement with key stakeholders for your SDG-aligned project.")

    if 'stakeholder_df' not in st.session_state:
        st.session_state.stakeholder_df = create_stakeholder_df()

    # Input form for adding a stakeholder
    with st.form("add_stakeholder_form"):
        st.subheader("Add a Stakeholder")
        stakeholder = st.text_input("Stakeholder Name/Group")
        category = st.selectbox("Stakeholder Category", get_stakeholder_categories())
        interest_influence = st.slider("Interest/Influence Level", 1, 10, 5)
        strategy = st.multiselect("Engagement Strategy", get_engagement_strategies())

        submit_button = st.form_submit_button("Add Stakeholder")

        if submit_button:
            if stakeholder and category and strategy:
                st.session_state.stakeholder_df = add_stakeholder(
                    st.session_state.stakeholder_df,
                    stakeholder,
                    category,
                    interest_influence,
                    ", ".join(strategy)
                )
                st.success(f"Added {stakeholder} to the stakeholder list.")
            else:
                st.warning("Please fill in all fields.")

    # Display stakeholder table
    if not st.session_state.stakeholder_df.empty:
        st.subheader("Stakeholder Engagement Plan")
        st.dataframe(st.session_state.stakeholder_df)

        # Option to download as CSV
        csv = st.session_state.stakeholder_df.to_csv(index=False)
        st.download_button(
            label="Download Stakeholder Plan as CSV",
            data=csv,
            file_name="stakeholder_engagement_plan.csv",
            mime="text/csv",
        )
    else:
        st.info("No stakeholders added yet. Use the form above to add stakeholders to your plan.")

    # Stakeholder analysis tips
    with st.expander("📊 Stakeholder Analysis Tips"):
        st.write("""
        1. **Identify all potential stakeholders**: Cast a wide net initially to ensure no important groups are missed.
        2. **Assess interest and influence**: Consider how much each stakeholder is affected by or can affect your project.
        3. **Prioritize stakeholders**: Focus more resources on high-interest, high-influence stakeholders.
        4. **Tailor engagement strategies**: Different stakeholders may require different approaches.
        5. **Regular review**: Stakeholder dynamics can change over time, so review and update your plan periodically.
        6. **Be inclusive**: Ensure marginalized or less visible groups are not overlooked.
        7. **Document interactions**: Keep records of stakeholder engagements and feedback for future reference.
        """)

    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool helps you identify and plan engagement with key stakeholders for your SDG-aligned project.")
        st.write("Use it to map out stakeholders, their level of interest/influence, and strategies to engage them effectively.")
        st.write("Remember to adapt your engagement approach based on the specific context of your project and stakeholders.")

if __name__ == "__main__":
    main()
