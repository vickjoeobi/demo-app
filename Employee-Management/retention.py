import pandas as pd
import streamlit as st
import plotly.express as px


def compute_rates(df):
    # Checking if essential columns are in the DataFrame
    required_columns = ['Hire Date', 'Termination Date', 'Employee Status']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if 'Hire Date' not in df.columns:
        df['Hire Date'] = pd.to_datetime('2023-01-01')  # Provide a default value for missing 'Hire Date'
    if 'Termination Date' not in df.columns:
        df['Termination Date'] = pd.NaT  # Provide a default value for missing 'Termination Date'

    try:
        # Convert date columns to datetime format
        df['Hire Date'] = pd.to_datetime(df['Hire Date'])
        df['Termination Date'] = pd.to_datetime(df['Termination Date'], errors='coerce')

        # Set current date for terminated employees
        df.loc[df['Employee Status'] != 'Active', 'Termination Date'] = df['Termination Date'].fillna(pd.Timestamp.now())

        # Generate the time range for rates
        time_range = pd.date_range(df['Hire Date'].min(), df['Termination Date'].max(), freq='D')

        # Calculate hiring and leaving counts
        hires = df.groupby(df['Hire Date'].dt.to_period("D"))['Employee ID'].count().reindex(time_range, fill_value=0)
        leaves = df[df['Employee Status'] != 'Active'].groupby(df['Termination Date'].dt.to_period("D"))['Employee ID'].count().reindex(time_range, fill_value=0)

        # Aggregate to the selected time period
        def aggregate_to_period(data, period):
            return data.resample(period).sum()

        return hires, leaves, aggregate_to_period
    except Exception as e:
        raise Exception(f"Error processing rates: {str(e)}")


def plot_retention(hires, leaves, aggregate_func, period='M'):
    # Aggregate data according to the selected period
    hires_agg = aggregate_func(hires, period)
    leaves_agg = aggregate_func(leaves, period)

    # Create a DataFrame for plotting
    retention_df = pd.DataFrame({'Hires': hires_agg, 'Leaves': leaves_agg})

    # Check if index is a PeriodIndex and convert to timestamp if it is
    if isinstance(retention_df.index, pd.PeriodIndex):
        retention_df['Time'] = retention_df.index.to_timestamp()
    else:
        retention_df['Time'] = retention_df.index

    # Plotting
    fig = px.line(retention_df, x='Time', y=['Hires', 'Leaves'], title='Employee Hiring vs Leaving Rates',
                  labels={'value': 'Number of Employees', 'variable': 'Metric'})
    st.plotly_chart(fig)



def display_retention(df):
    st.header("Employee Retention Analysis")
    st.write("Visualize the leaving rate in comparison to hiring and growth rate.")

    period_selection = st.selectbox("Select Time Interval", ['Daily', 'Monthly', 'Quarterly'], index=1)
    period_dict = {'Daily': 'D', 'Monthly': 'M', 'Quarterly': 'Q'}
    period = period_dict[period_selection]

    hires, leaves, aggregate_func = compute_rates(df)
    plot_retention(hires, leaves, aggregate_func, period)
