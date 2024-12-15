import pandas as pd

# Define the function to find the second highest salary
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Extract unique salary values and sort in descending order
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there are less than 2 unique salaries
    if len(salaries) < 2:
        # Return a DataFrame with 'SecondHighestSalary' as None
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    # Calculate the second highest salary
    second_highest = salaries.iloc[1]
    
    # Create a DataFrame to store the result
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})
    
    # Return the DataFrame with the calculated second highest salary
    return result_df