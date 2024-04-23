# Employee Management Dashboard

This project is a comprehensive Employee Management Dashboard built with Python and Streamlit. It allows users to upload a CSV file of employee records and provides various visualizations and metrics related to the data.

## Features

- **Employee Record Upload**: Users can upload a CSV file containing employee records. The application checks if the uploaded file contains all the required columns and notifies the user if any are missing.

- **Employee Dashboard**: Displays key metrics such as total employees, new hires in the last year, average salary, median salary, and salary range. It also provides visualizations of employee distribution by country, department, position, employment type, employee status, gender, office, and performance reviews.

- **Hiring Performance Dashboard**: Visualizes the hiring rate trend over different time intervals.

- **Employee Retention Analysis**: Compares the leaving rate with the hiring and growth rate.

## Files

- `app.py`: The main application file. It handles file upload and calls the functions to display the different dashboards.

- `dashboard.py`: Contains the code for the Employee Dashboard.

- `hiring.py`: Contains the code for the Hiring Performance Dashboard.

- `retention.py`: Contains the code for the Employee Retention Analysis.

- `DataGen.py`: A script to generate mock employee data for testing purposes.

## Required Columns

The CSV file uploaded by the user should contain the following columns:

- Employee ID
- First Name
- Last Name
- Department
- Position
- Hire Date
- Office
- Country
- Employee Status
- Termination Date
- Reason for Leaving
- Employment Type
- Date of Birth
- Gender
- Annual Salary
- Performance Reviews

## Running the Application

To run the application, navigate to the project directory in your terminal and run the following command:

```bash
streamlit run app.py
```

## Dependencies

This project requires the following Python libraries:

- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Faker

You can install these dependencies using pip:

```bash
pip install streamlit pandas numpy matplotlib seaborn plotly faker
```

## Data Generation

You can generate mock employee data for testing purposes using the `DataGen.py` script. The generated data will be saved as a CSV file in the same directory.

## Note

This project is intended for demonstration purposes and should not be used to process sensitive employee data without proper data handling and privacy measures in place.