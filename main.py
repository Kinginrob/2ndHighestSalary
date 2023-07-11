import configparser
from database_connector import DatabaseConnector
from data_processor import DataProcessor
import logging

# Main function
def main():
    try:
        # Read database and file configs
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Extract database details from config
        user = config.get('database', 'user')
        password = config.get('database', 'password')
        host = config.get('database', 'host')
        database = config.get('database', 'database')
        connection_string = f'postgresql://{user}:{password}@{host}/{database}'

        # Extract file details from config
        dept_file = config.get('files', 'departments')

        # Set up database connection and data processing
        db_connector = DatabaseConnector(connection_string)
        processor = DataProcessor(db_connector, dept_file)
        
        # Process data
        processor.process_data()

        # Display final result
        print('Final Data:')
        print(processor.get_second_highest_salaries().to_string(index=False))
    except Exception as e:
        # Log errors
        logging.error(f"An error occurred in main: {str(e)}")
        raise

# Execute main function
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    main()
