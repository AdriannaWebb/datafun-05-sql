'''
Module 5 - This file will demonstrate basic usage of Python SQL integration.  
It will manipulate that data by calling sql queries sorted into distinct files
'''
#import modules
import logging
import sqlite3
from pathlib import Path
import pandas as pd

# Import execute_sql_file 
from db_initialize_awebb import execute_sql_from_file


# Define database path 
db_file_path = Path("project.db")

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

#Function to execute sql files
def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


def main():
    # Define the SQL folder path
    sql_folder_path = Path("sql")

    # Define the SQL files to execute
    sql_files = [
        sql_folder_path.joinpath("create_tables.sql"),
        sql_folder_path.joinpath("insert_records.sql"),
        sql_folder_path.joinpath("update_records.sql"),
        sql_folder_path.joinpath("delete_records.sql"),
        sql_folder_path.joinpath("query_aggregation.sql"),
        sql_folder_path.joinpath("query_filter.sql"),
        sql_folder_path.joinpath("query_sorting.sql"),
        sql_folder_path.joinpath("query_group_by.sql"),
        sql_folder_path.joinpath("query_join.sql")
    ]

    # Execute each SQL file
    for sql_file in sql_files:
        execute_sql_from_file(db_file_path, sql_file)
        
    logging.info("All SQL operations completed successfully")


# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()