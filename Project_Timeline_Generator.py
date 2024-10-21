import streamlit as st
from datetime import datetime, timedelta

def generate_timeline(project_name, start_date, duration, sdgs):
    timeline = []
    current_date = start_date
    
    # Initial phase
    timeline.append({
        "phase": "Project Initiation",
        "start_date": current_date,
        "end_date": current_date + timedelta(weeks=4),
        "description": "Set up project team, define scope, and create detailed project plan.",
        "sdgs": sdgs
    })
    current_date += timedelta(weeks=4)
    
    # Implementation phases
    num_phases = max(1, duration // 3)  # At least one phase, then one phase per 3 months
    phase_duration = timedelta(days=duration * 30 // num_phases)
    
    for i in range(num_phases):
        timeline.append({
            "phase": f"Implementation Phase {i+1}",
            "start_date": current_date,
            "end_date": current_date + phase_duration,
            "description": f"Execute project activities related to {', '.join(sdgs[:2])}...",
            "sdgs": sdgs
        })
        current_date += phase_duration
    
    # Final phase
    timeline.append({
        "phase": "Project Closure",
        "start_date": current_date,
        "end_date": current_date + timedelta(weeks=4),
        "description": "Evaluate project outcomes, document lessons learned, and plan for sustainability.",
        "sdgs": sdgs
    })
    
    return timeline

def main():
    st.title("📅 Project Timeline Generator")
    st.write("Plan your SDG-aligned project with this simple timeline generator.")
    
    project_name = st.text_input("Project Name", "My SDG Project")
    start_date = st.date_input("Project Start Date", datetime.now())
    duration = st.slider("Project Duration (months)", 1, 36, 12)
    sdgs = st.multiselect("Select relevant SDGs", [
        "No Poverty", "Zero Hunger", "Good Health and Well-being", "Quality Education",
        "Gender Equality", "Clean Water and Sanitation", "Affordable and Clean Energy",
        "Decent Work and Economic Growth", "Industry, Innovation and Infrastructure",
        "Reduced Inequality", "Sustainable Cities and Communities",
        "Responsible Consumption and Production", "Climate Action", "Life Below Water",
        "Life on Land", "Peace, Justice and Strong Institutions", "Partnerships for the Goals"
    ])
    
    if st.button("Generate Timeline"):
        if not sdgs:
            st.warning("Please select at least one SDG.")
        else:
            timeline = generate_timeline(project_name, start_date, duration, sdgs)
            
            st.subheader(f"Timeline for {project_name}")
            for phase in timeline:
                with st.expander(f"{phase['phase']} ({phase['start_date'].strftime('%Y-%m-%d')} to {phase['end_date'].strftime('%Y-%m-%d')})"):
                    st.write(f"**Description:** {phase['description']}")
                    st.write(f"**Relevant SDGs:** {', '.join(phase['sdgs'])}")
                    
                    # Suggest a milestone
                    milestone = st.text_input("Add a milestone for this phase:", key=phase['phase'])
                    if milestone:
                        st.success(f"Milestone added: {milestone}")
    
    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool helps you create a basic timeline for your SDG-aligned project.")
        st.write("It generates phases based on your project duration and allows you to add milestones.")
        st.write("Remember to adjust the timeline according to your specific project needs and local context.")

if __name__ == "__main__":
    main()
