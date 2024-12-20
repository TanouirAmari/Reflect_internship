# Reflect_internship


This document explains the functionality of two Python scripts for fetching data from an API and saving it 
either to a CSV file or an SQLite database, depending on the user's preference.

--- Script 1: Fetching Data to CSV Files ---

This script retrieves data from two API endpoints, processes it, and saves it in CSV format.
- **fetch_and_save_users**: Fetches user data, including details like name, email, contract dates, and roles, and saves it to a CSV file.
- **fetch_and_save_departments**: Fetches department data, including hierarchy, levels, and associated users, and saves it to a CSV file.

The user can specify an API key, a base URL, and the desired output file names for CSV storage. 
The script includes a configuration-based function (`fetch_data_daily`) for fetching data daily, 
allowing multiple endpoints to be processed from a JSON configuration file.

--- Script 2: Fetching Data to an SQLite Database ---

This script performs the same operations as the first one but stores the data in an SQLite database instead of CSV files.
- **fetch_and_save_users_to_sql**: Fetches user data and saves it to an SQL table named 'users'.
- **fetch_and_save_departments_to_sql**: Fetches department data and saves it to an SQL table named 'departments'.

For database storage, the user provides an API key, a base URL, and the path to the SQLite database file.

--- Key Features ---
1. **Choice of Storage Format**: Users can choose between saving data as CSV files or in an SQLite database.
2. **Configuration File Support**: The first script supports using a JSON configuration file to specify API endpoints and output files.
3. **Daily Automation**: The first script is designed to be scheduled for daily execution using a configuration file.
4. **Error Handling**: Both scripts include error handling for failed API requests or file/database operations.

--- How to Use ---
1. Provide your API key and base URL for the API.
2. Decide whether to use CSV files or an SQL database for data storage.
3. Adjust the configuration (e.g., JSON file for the first script) or directly call the relevant functions.
4. Run the script and verify the saved data in the specified files or database.

Example usage for Script 1:
```
fetch_and_save_users("API_KEY", "BASE_URL", "Users.csv")
fetch_and_save_departments("API_KEY", "BASE_URL", "Departments.csv")
```

Example usage for Script 2:
```
fetch_and_save_users_to_sql("API_KEY", "BASE_URL", "data_store.db")
fetch_and_save_departments_to_sql("API_KEY", "BASE_URL", "data_store.db")
```
