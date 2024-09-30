'''Project 5 integrates Python and SQL, focusing on database interactions using SQLite. 
This project introduces logging, a useful tool for debugging and monitoring projects, and 
involves creating and managing a database, building a schema, and performing various SQL operations,
including queries with joins, filters, and aggregations.

This file will create a database and fill it with data
'''

# Necessary imports from Python Standard Library 
import sqlite3
import pathlib
import logging

# Import the external packages
import pandas as pd

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths using pathlib
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql").joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")


def verify_and_create_folders(paths): 
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        # create folder if it doesn't exist
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
            logging.info("Folder" + path + "created")
        else:
            logging.debug(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
        logging.info("Database created successfully")
    except sqlite3.Error as e:
        logging.exception(f"Error creating the databse: {e}")
        
def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables. db_path is where database should be created, sql_file_path is where the SQL file is located."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
            logging.info("Tables created successfully")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables. db_path is where database should be created, author_data_path is where the author data is located, book_data_path is where the book data is located."""
    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
            logging.info("Data inserted successfully")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")


def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)   

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()