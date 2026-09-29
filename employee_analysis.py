
import pandas as pd

# Load employee data
data = pd.read_csv("employees.csv")

# Display employee data
print("Employee Data:")
print(data)

# Calculate average salary
average_salary = data["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Count employees in each department
department_count = data["Department"].value_counts()
print("\nEmployees in Each Department:")
print(department_count)

# Set salary threshold
salary_threshold = 50000

# Find employees above the salary threshold
high_salary = data[data["Salary"] > salary_threshold]

print("\nEmployees with Salary Above", salary_threshold, ":")
print(high_salary)

# Save filtered employees to a new CSV file
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered data saved to high_salary_employees.csv") 