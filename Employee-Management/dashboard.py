import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def load_data():
    return pd.DataFrame(st.session_state['data'])

def preprocess_data(df):
    df['Hire Date'] = pd.to_datetime(df['Hire Date'], errors='coerce')
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce')
    df['Age'] = ((pd.Timestamp.now() - df['Date of Birth']) / np.timedelta64(1, 'Y')).astype(int)
    return df

def plot_distribution(data, title, xlabel, ylabel='Percentage'):
    fig, ax = plt.subplots()
    sns.barplot(x=data.values, y=data.index, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def display_metrics(df):
    st.title("Employee Dashboard")
    st.write("### Key Metrics Overview")

    total_employees = len(df)
    df['Hire Date'] = pd.to_datetime(df['Hire Date'], errors='coerce')  # Convert and coerce errors to NaT
    new_hires = df[df['Hire Date'] >= pd.Timestamp.now() - pd.DateOffset(years=1)].shape[0]
    avg_salary = df['Annual Salary'].mean()
    median_salary = df['Annual Salary'].median()
    min_salary = df['Annual Salary'].min()
    max_salary = df['Annual Salary'].max()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Employees", total_employees)
        st.metric("New Hires (Last Year)", new_hires)
    with col2:
        st.metric("Average Salary", f"${avg_salary:.2f}")
        st.metric("Median Salary", f"${median_salary:.2f}")
    with col3:
        st.metric("Salary Range", f"${min_salary:.2f} - ${max_salary:.2f}")

    st.write("### Employee Distribution")
    col1, col2 = st.columns(2)
    with col1:
        fig = plot_distribution(df['Country'].value_counts(normalize=True) * 100, "Employee Distribution by Country", "Percentage")
        st.pyplot(fig)
    with col2:
        fig = plot_distribution(df['Department'].value_counts(normalize=True) * 100, "Department Distribution", "Percentage")
        st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        fig = plot_distribution(df['Position'].value_counts(normalize=True) * 100, "Position Categories", "Percentage")
        st.pyplot(fig)
    with col2:
        fig = plot_distribution(df['Employment Type'].value_counts(normalize=True) * 100, "Employment Types", "Percentage")
        st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        fig = plot_distribution(df['Employee Status'].value_counts(normalize=True) * 100, "Employee Status", "Percentage")
        st.pyplot(fig)
    with col2:
        fig = plot_distribution(df['Gender'].value_counts(normalize=True) * 100, "Gender Distribution", "Percentage")
        st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        fig = plot_distribution(df['Office'].value_counts(normalize=True) * 100, "Distribution by Office", "Percentage")
        st.pyplot(fig)
    with col2:
        fig = plot_distribution(df['Performance Reviews'].value_counts(normalize=True) * 100, "Performance Review Ratings", "Percentage")
        st.pyplot(fig)

def main():
    if 'data' not in st.session_state:
        st.error("No employee data found. Please upload data from the homepage.")
        st.button("Go to Upload Page", on_click=lambda: st.session_state.update(page="upload"))
    else:
        df = preprocess_data(pd.DataFrame(st.session_state['data']))
        display_metrics(df)

if __name__ == "__main__":
    main()