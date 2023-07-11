import pandas as pd
import logging

# DataProcessor class for processing data from the database and csv file
class DataProcessor:
    def __init__(self, db_connector, dept_file):
        # Initialize with a db connector, a path to departments file, and an empty DataFrame for results
        self.db_connector = db_connector
        self.dept_file = dept_file
        self.second_highest_salaries = pd.DataFrame()

    def process_data(self):
        try:
            # Retrieve employee data from the database and department data from csv
            df = self.db_connector.execute_query("SELECT emp_id, name, salary, dept_id FROM employee;")
            dept_df = pd.read_csv(self.dept_file)

            # Merge employee and department data, then sort by salary
            merged_df = pd.merge(df, dept_df, how='left', on='dept_id').sort_values('salary', ascending=False)

            # Get second highest salary employees for each department
            highest_salaries = merged_df.drop_duplicates(['dept_name'])
            second_highest_df = merged_df.loc[~merged_df.index.isin(highest_salaries.index)]
            self.second_highest_salaries = second_highest_df.drop_duplicates(['dept_name'])

            # Make a copy of DataFrame before renaming column to avoid pandas warning
            self.second_highest_salaries = self.second_highest_salaries.copy()
            
            # Rename the 'name' column to 'empName'
            self.second_highest_salaries.rename(columns={"name": "empName"}, inplace=True)
        except Exception as e:
            # Log and re-raise exceptions
            logging.error(f"Data processing error: {str(e)}")
            raise

    def get_second_highest_salaries(self):
        # Return the result DataFrame
        return self.second_highest_salaries
