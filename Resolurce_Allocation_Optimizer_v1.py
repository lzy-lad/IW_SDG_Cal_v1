import streamlit as st
import pandas as pd
import plotly.express as px

def create_resource_df():
    return pd.DataFrame(columns=["Activity", "SDG", "Budget", "Time", "Personnel", "Impact Score"])

def add_activity(df, activity, sdg, budget, time, personnel, impact):
    new_row = pd.DataFrame({
        "Activity": [activity],
        "SDG": [sdg],
        "Budget": [budget],
        "Time": [time],
        "Personnel": [personnel],
        "Impact Score": [impact]
    })
    return pd.concat([df, new_row], ignore_index=True)

def calculate_efficiency(row):
    return row['Impact Score'] / (row['Budget'] + row['Time'] + row['Personnel'])

def main():
    st.title("🎯 Resource Allocation Optimizer")
    st.write("Optimize your resource allocation for maximum impact across SDG-aligned project activities.")

    if 'resource_df' not in st.session_state:
        st.session_state.resource_df = create_resource_df()

    total_budget = st.sidebar.number_input("Total Budget Available", min_value=0, value=100000)
    total_time = st.sidebar.number_input("Total Time Available (person-months)", min_value=0, value=24)
    total_personnel = st.sidebar.number_input("Total Personnel Available", min_value=0, value=10)

    # Input form for adding an activity
    with st.form("add_activity_form"):
        st.subheader("Add a Project Activity")
        activity = st.text_input("Activity Name")
        sdg = st.selectbox("Related SDG", [f"SDG {i}" for i in range(1, 18)])
        budget = st.number_input("Budget Required", min_value=0, max_value=total_budget)
        time = st.number_input("Time Required (person-months)", min_value=0, max_value=total_time)
        personnel = st.number_input("Personnel Required", min_value=0, max_value=total_personnel)
        impact = st.slider("Expected Impact Score", 1, 10, 5)

        submit_button = st.form_submit_button("Add Activity")

        if submit_button:
            if activity and sdg and budget >= 0 and time >= 0 and personnel >= 0:
                st.session_state.resource_df = add_activity(
                    st.session_state.resource_df,
                    activity, sdg, budget, time, personnel, impact
                )
                st.success(f"Added {activity} to the project activities.")
            else:
                st.warning("Please fill in all fields with valid values.")

    # Display and analyze activities
    if not st.session_state.resource_df.empty:
        st.subheader("Project Activities and Resource Allocation")
        
        # Calculate efficiency scores
        st.session_state.resource_df['Efficiency'] = st.session_state.resource_df.apply(calculate_efficiency, axis=1)
        
        # Sort by efficiency
        sorted_df = st.session_state.resource_df.sort_values('Efficiency', ascending=False)
        
        st.dataframe(sorted_df)

        # Resource usage summary
        st.subheader("Resource Usage Summary")
        total_used_budget = sorted_df['Budget'].sum()
        total_used_time = sorted_df['Time'].sum()
        total_used_personnel = sorted_df['Personnel'].sum()

        col1, col2, col3 = st.columns(3)
        col1.metric("Budget Used", f"{total_used_budget:,.0f}", f"{total_used_budget/total_budget:.1%}")
        col2.metric("Time Used", f"{total_used_time:.1f} months", f"{total_used_time/total_time:.1%}")
        col3.metric("Personnel Used", total_used_personnel, f"{total_used_personnel/total_personnel:.1%}")

        # Visualizations
        st.subheader("Resource Allocation Visualizations")
        
        # Budget allocation by SDG
        fig_budget = px.pie(sorted_df, values='Budget', names='SDG', title='Budget Allocation by SDG')
        st.plotly_chart(fig_budget)

        # Impact vs Efficiency scatter plot
        fig_impact = px.scatter(sorted_df, x='Impact Score', y='Efficiency', size='Budget', 
                                color='SDG', hover_name='Activity', 
                                title='Impact vs Efficiency of Activities')
        st.plotly_chart(fig_impact)

        # Option to download as CSV
        csv = sorted_df.to_csv(index=False)
        st.download_button(
            label="Download Resource Allocation Plan as CSV",
            data=csv,
            file_name="resource_allocation_plan.csv",
            mime="text/csv",
        )
    else:
        st.info("No activities added yet. Use the form above to add activities to your project.")

    # Resource allocation tips
    with st.expander("💡 Resource Allocation Tips"):
        st.write("""
        1. **Prioritize high-impact activities**: Focus resources on activities with the highest potential impact.
        2. **Consider efficiency**: Look for activities that provide high impact relative to resource usage.
        3. **Balance across SDGs**: Ensure resources are distributed to address multiple SDGs if relevant to your project.
        4. **Be realistic**: Make sure your resource allocations are achievable within your constraints.
        5. **Allow for flexibility**: Keep some resources in reserve for unexpected needs or opportunities.
        6. **Regular review**: Periodically review and adjust your resource allocation based on project progress and changing circumstances.
        7. **Seek synergies**: Look for activities that can contribute to multiple SDGs simultaneously.
        """)

    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool helps you optimize resource allocation across different activities in your SDG-aligned project.")
        st.write("Use it to balance your budget, time, and personnel while maximizing potential impact.")
        st.write("The efficiency score is calculated as the ratio of impact to total resources used (budget + time + personnel).")
        st.write("Remember to adapt the allocations based on your specific project context and priorities.")

if __name__ == "__main__":
    main()
