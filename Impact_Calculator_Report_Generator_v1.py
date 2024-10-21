import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO
import base64
import docx2txt
import PyPDF2

def load_data(uploaded_file):
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        if file_extension in ['csv', 'txt']:
            df = pd.read_csv(uploaded_file)
        elif file_extension in ['xlsx', 'xls']:
            df = pd.read_excel(uploaded_file)
        elif file_extension == 'pdf':
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            df = pd.DataFrame([text.split('\n')])
        elif file_extension == 'docx':
            text = docx2txt.process(uploaded_file)
            df = pd.DataFrame([text.split('\n')])
        else:
            st.error(f"Unsupported file format: {file_extension}")
            return None
        
        return df
    return None

def calculate_impact(df):
    # This is a placeholder function. In a real-world scenario,
    # you would implement more sophisticated impact calculations here.
    impact_score = df.sum().sum()  # Simple sum of all numeric values
    return impact_score

def generate_visualizations(df):
    figs = []
    
    # Sample visualization 1: Bar chart of numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) > 0:
        fig = px.bar(df, y=numeric_cols, title="Impact Metrics")
        figs.append(fig)
    
    # Sample visualization 2: Scatter plot of two numeric columns
    if len(numeric_cols) >= 2:
        fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1], 
                         size=numeric_cols[0], color=numeric_cols[1],
                         hover_name=df.index, title="Correlation of Impact Metrics")
        figs.append(fig)
    
    # Sample visualization 3: Sunburst chart (assuming categorical columns exist)
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) >= 2:
        fig = px.sunburst(df, path=categorical_cols[:2], values=numeric_cols[0] if len(numeric_cols) > 0 else None,
                          title="Hierarchical View of Project Impact")
        figs.append(fig)
    
    # Sample visualization 4: 3D scatter plot
    if len(numeric_cols) >= 3:
        fig = px.scatter_3d(df, x=numeric_cols[0], y=numeric_cols[1], z=numeric_cols[2],
                            color=numeric_cols[2], size=numeric_cols[0],
                            title="3D View of Impact Metrics")
        figs.append(fig)
    
    return figs

def generate_report(df, impact_score, figs):
    report = f"""
    # Project Impact Report

    ## Overall Impact Score: {impact_score:.2f}

    ## Data Summary
    {df.describe().to_markdown()}

    ## Visualizations
    """
    
    for i, fig in enumerate(figs, 1):
        img_bytes = fig.to_image(format="png")
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        report += f"\n\n### Visualization {i}\n![Visualization {i}](data:image/png;base64,{img_base64})\n"
    
    return report

def main():
    st.title("🚀 Impact Calculator and Report Generator")
    st.write("Upload your project data file to calculate impact and generate a detailed report with futuristic visualizations.")

    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'txt', 'xlsx', 'xls', 'pdf', 'docx'])
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        if df is not None:
            st.subheader("Data Preview")
            st.dataframe(df.head())

            impact_score = calculate_impact(df)
            st.subheader(f"Overall Impact Score: {impact_score:.2f}")

            st.subheader("Impact Visualizations")
            figs = generate_visualizations(df)
            for fig in figs:
                st.plotly_chart(fig, use_container_width=True)

            report = generate_report(df, impact_score, figs)

            st.download_button(
                label="Download Full Report",
                data=report,
                file_name="impact_report.md",
                mime="text/markdown",
            )

    # About the tool
    with st.expander("ℹ️ About this tool"):
        st.write("This tool calculates project impact and generates a detailed report with futuristic visualizations.")
        st.write("Upload your project data in various formats (CSV, Excel, PDF, Word) to get started.")
        st.write("The tool will analyze your data, compute an overall impact score, and create interactive visualizations.")
        st.write("You can download a full report including all visualizations for further use or presentation.")

if __name__ == "__main__":
    main()
