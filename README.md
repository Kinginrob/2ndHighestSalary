# Employee Salary Report Generator

## Description

The application utilizes two data sources:

1. Employee data from a Postgres database.
2. Department names from a CSV file.

The goal is to amalgamate these data sources, process the data, and output a list of employees who earn the second highest salary within their respective departments.

## Features

* Extracts employee data (including ID, name, salary, and department ID) from a PostgreSQL database.
* Imports department names from a CSV file.
* Merges and processes the data using the powerful data manipulation library, Pandas.
* Outputs a clear and concise report showcasing the employees with the second highest salary in each department.

## How to Use

* Ensure that your PostgreSQL database and CSV file are correctly set up and accessible.
* Configure the config.ini file with your PostgreSQL user, password, host, and database information, as well as the path to your CSV file.
* Run the main.py file to execute the application.

## Validation

The output can be validated by running SQL queries directly in your PostgreSQL database and manually inspecting the CSV file. Alternatively, you can compare the application output with another trusted data source or method.

![image](https://github.com/Kinginrob/2ndHighestSalary/assets/89039139/c4800151-ab70-4304-a1e6-7b996f55ac48)
