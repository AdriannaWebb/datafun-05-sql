# Project 5: Adrianna Webb SQL project
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Overview
This project integrates Python and SQL using SQLite. It involves creating and managing a database, defining a schema, and performing various SQL operations such as joins, filters, and aggregations. Additionally, logging is implemented to track program execution and assist in debugging and monitoring.

## Installation and Setup


## Requirements
- **Database:** SQLite
- **Programming Language:** Python
- **External Packages:** 
  - `pandas`
  - `pyarrow`
- **Logging:** Python's built-in logging module to track program execution.

### Create a GitHub Repository

Create a new repository on GitHub, including a README file.
Clone the repository to your local machine

### Add a .gitignore File

Ensure the following entries are added to your .gitignore file to exclude unnecessary files from being committed:

.vscode/

#### Ignore macOS specific files
.DS_Store

# Python virtual environment
.venv/

### Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows


## External Dependencies:
To work on this project, install the necessary external packages. It is recommended to use a virtual
environment to keep your project dependencies isolated.



## Project Structure
```bash
datafun-05-sql/
│
├── db_initialize_awebb.py         # Script for initializing the database
├── db_operations_awebb.py         # Script for executing SQL operations
├── log.txt                        # Log file for recording events
├── README.md                      # Project documentation (this file)
├── sql/                           # Folder containing SQL scripts
│   ├── create_tables.sql          # SQL script for creating tables
│   ├── insert_records.sql         # SQL script for inserting records
│   ├── update_records.sql         # SQL script for updating records
│   ├── delete_records.sql         # SQL script for deleting records
│   ├── query_aggregation.sql      # SQL script for running aggregation queries
│   ├── query_filter.sql           # SQL script for filtering data
│   ├── query_sorting.sql          # SQL script for sorting data
│   ├── query_group_by.sql         # SQL script for running GROUP BY queries
│   ├── query_join.sql             # SQL script for joining tables
└── project.db                     # SQLite database file (created by script)

```
# Setup Instructions
## Clone the Repository:

```
git clone <repository-url>
cd project-directory
```

## Create a Virtual Environment:

```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

## Install Dependencies:


```
pip install pandas
```

## Run the Initialization:


```
python db_initialize_awebb.py
```

## Run SQL Operations:

```
python db_operations_awebb.py
```

## SQL Operations
- **create_tables.sql:** Creates authors and books tables.
- **insert_records.sql:** Inserts records into both tables.
- **query_aggregation.sql:** Uses aggregation functions (COUNT, SUM, AVG).
- **query_filter.sql:** Filters data with WHERE.
- **query_join.sql:** Performs table joins.

# Logging
All steps are logged in log.txt. Check the log for any errors or completion messages.

# Verification
Inspect the project.db using an SQLite viewer (e.g., SQLite Viewer in VS Code).




## Stage and Push Files to GitHub
I used the following Git commands to stage and commit changes:

```
git add .
git commit -m "message: commit message"
git push origin main
```
