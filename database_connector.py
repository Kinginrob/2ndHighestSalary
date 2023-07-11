import pandas as pd
from sqlalchemy import create_engine
import logging

class DatabaseConnector:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)

    def execute_query(self, query):
        try:
            return pd.read_sql_query(query, self.engine)
        except Exception as e:
            logging.error(f"An error occurred during query execution: {str(e)}")
            raise
