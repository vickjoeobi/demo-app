import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Setting a seed for reproducibility
np.random.seed(42)

# Generating mock data for 50 employees
data = {
    "Employee ID": [f"{i:03}" for i in range(1, 51)],
    "First Name": [fake.first_name() for _ in range(50)],
    "Last Name": [fake.last_name() for _ in range(50)],
    "Department": np.random.choice(["Sales", "Marketing", "HR", "Finance"], 50),
    "Position": np.random.choice(["Manager", "Executive", "Analyst"], 50),
    "Hire Date": [fake.date_between(start_date='-5y', end_date='today') for _ in range(50)],
    "Office": np.random.choice(["DE", "HU", "KR", "JP"], 50),
    "Country": np.random.choice(["Germany", "Hungary", "South Korea", "Japan"], 50),
    "Employee Status": np.random.choice(["Active", "Terminated"], 50, p=[0.8, 0.2]),
    "Termination Date": [fake.date_between(start_date='-2y', end_date='today') if np.random.rand() > 0.8 else None for _ in range(50)],
    "Reason for Leaving": [fake.sentence() if np.random.rand() > 0.8 else None for _ in range(50)],
    "Employment Type": np.random.choice(["Full-time", "Part-time", "Contractor"], 50),
    "Date of Birth": [fake.date_of_birth(minimum_age=18, maximum_age=65) for _ in range(50)],
    "Gender": np.random.choice(["Male", "Female", "Other"], 50),
    "Annual Salary": np.random.randint(30000, 100000, 50),
    "Performance Reviews": np.random.choice(["Excellent", "Good", "Average", "Poor"], 50)
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving DataFrame as a CSV file
file_path = './data/Employee_Record.csv'
df.to_csv(file_path, index=False)

file_path
