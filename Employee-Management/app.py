import streamlit as st
import pandas as pd
from dashboard import display_metrics
from hiring import display_hiring_dashboard
from retention import display_retention


required_columns = ['Employee ID', 'First Name', 'Last Name', 'Department', 'Position', 'Hire Date',
                    'Office', 'Country', 'Employee Status', 'Termination Date', 'Reason for Leaving',
                    'Employment Type', 'Date of Birth', 'Gender', 'Annual Salary', 'Performance Reviews']

def check_csv_columns(uploaded_file):
    """Check if uploaded CSV contains all required columns."""
    try:
        df = pd.read_csv(uploaded_file)
        uploaded_columns = df.columns.tolist()
        missing_columns = [col for col in required_columns if col not in uploaded_columns]
        return missing_columns, df
    except Exception as e:
        return str(e), None

def main():
    st.sidebar.title("Employee Record Upload")
    st.sidebar.write("Please upload your employee CSV file. Ensure it contains the following headers:")
    st.sidebar.write(", ".join(required_columns))

    uploaded_file = st.sidebar.file_uploader("Choose a file", type='csv')
    if uploaded_file is not None:
        missing_columns, df = check_csv_columns(uploaded_file)
        if not missing_columns:
            st.sidebar.success("Upload successful! Your file contains all the required columns.")
            st.session_state['data'] = df.to_dict('records')
            display_metrics(df)
            display_hiring_dashboard(df)
            display_retention(df)
        else:
            st.sidebar.error(f"Upload failed. Missing columns: {', '.join(missing_columns)}")

if __name__ == "__main__":
    main()
