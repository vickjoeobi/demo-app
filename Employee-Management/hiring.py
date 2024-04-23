import pandas as pd
import streamlit as st
import plotly.express as px

def plot_hiring_trends(df, time_freq):
    """Generate a plot to visualize hiring trends over time."""
    df['Hire Date'] = pd.to_datetime(df['Hire Date'])
    df.set_index('Hire Date', inplace=True)

    # Resampling data according to the selected frequency
    resampled_data = df.resample(time_freq).size()

    # Creating the figure using Plotly
    fig = px.line(resampled_data, title=f"Hiring Trends - {time_freq} view",
                  labels={'value': 'Number of Hires', 'Hire Date': 'Date'},
                  markers=True)

    return fig

def display_hiring_dashboard(df):
    """Display the hiring dashboard with options to select time intervals."""
    st.title("Employee Hiring Performance Dashboard")
    st.write("Visualize the hiring rate trend over different time intervals.")

    # Time frequency options
    time_options = {'Daily': 'D', 'Monthly': 'M', 'Quarterly': 'Q'}
    selected_time = st.selectbox("Select the time interval", list(time_options.keys()))

    # Generate and display the plot
    fig = plot_hiring_trends(df, time_options[selected_time])
    st.plotly_chart(fig)
