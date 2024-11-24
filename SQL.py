#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:42:49 2024

@author: tanouiramari
"""

import requests
import pandas as pd
import sqlite3


def fetch_and_save_users_to_sql(api_key, url, db_path):
    """
    Fetches user data from the API, formats it, and saves it to an SQL database.

    Args:
        api_key (str): Your API key for authentication.
        url (str): The API endpoint URL.
        db_path (str): Path to the SQLite database file.
    """
    url = url + "/api/v3/users?fields=id,firstName,lastName,birthDate,mail,dtContractStart,dtContractEnd,rolePrincipal.name,rolePrincipal.id,manager.id,department.id"
    headers = {
        "Authorization": f"lucca application={api_key}",
        "Accept": "application/json"
    }
    
    try:
        # Perform the GET request
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("Request successful.")
            
            # Extract the data
            items = response.json().get('data', {}).get('items', [])
            formatted_items = []
            
            # Format the items
            for element in items:
                formatted_item = {
                    "id": element.get("id"),
                    "firstName": element.get("firstName"),
                    "lastName": element.get("lastName"),
                    "birthDate": element.get("birthDate"),
                    "mail": element.get("mail"),
                    "dtContractStart": element.get("dtContractStart"),
                    "dtContractEnd": element.get("dtContractEnd"),
                    "rolePrincipal": element.get("rolePrincipal", {}).get("name"),
                    "rolePrincipal_ID": element.get("rolePrincipal", {}).get("id"),
                    "manager_ID": element.get("manager", {}).get("id"),
                    "department_ID": element.get("department", {}).get("id"),
                }
                formatted_items.append(formatted_item)
            
            # Convert the data into a DataFrame
            df = pd.DataFrame(formatted_items)
            
            # Save the DataFrame to an SQL database
            conn = sqlite3.connect(db_path)
            df.to_sql('users', conn, if_exists='replace', index=False)
            conn.close()
            print("User data has been saved to the database.")
        else:
            print(f"Request failed. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


def fetch_and_save_departments_to_sql(api_key, url, db_path):
    """
    Fetches department data from the API, formats it, and saves it to an SQL database.

    Args:
        api_key (str): Your API key for authentication.
        url (str): The API endpoint URL.
        db_path (str): Path to the SQLite database file.
    """
    url = url + "/api/v3/departments?fields=id,name,code,hierarchy,parentID,level,sortOrder,headID,currentUsers.ID"
    headers = {
        "Authorization": f"lucca application={api_key}",
        "Accept": "application/json"
    }
    
    try:
        # Perform the GET request
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("Request successful.")
            
            # Extract the data
            items = response.json().get('data', {}).get('items', [])
            formatted_items = []
            
            # Format the items
            for element in items:
                formatted_item = {
                    "id": element.get("id"),
                    "name": element.get("name"),
                    "code": element.get("code"),
                    "hierarchy": element.get("hierarchy"),
                    "parentId": element.get("parentId"),
                    "level": element.get("level"),
                    "sortOrder": element.get("sortOrder"),
                    "headID": element.get("headID"),
                    "currentUsers": ", ".join(str(user["id"]) for user in element.get("currentUsers", []))
                }
                formatted_items.append(formatted_item)
            
            # Convert the data into a DataFrame
            df = pd.DataFrame(formatted_items)
            
            # Save the DataFrame to an SQL database
            conn = sqlite3.connect(db_path)
            df.to_sql('departments', conn, if_exists='replace', index=False)
            conn.close()
            print("Department data has been saved to the database.")
        else:
            print(f"Request failed. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

API_KEY = "caf8058b-b7ec-4df2-85e3-a673b5466e97"
BASE_URL = "https://reflect2-sandbox.ilucca-demo.net"
DB_PATH = "data_store.db"

fetch_and_save_users_to_sql(API_KEY, BASE_URL, DB_PATH)
fetch_and_save_departments_to_sql(API_KEY, BASE_URL, DB_PATH)



