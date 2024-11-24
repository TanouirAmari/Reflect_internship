#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:26:18 2024

@author: tanouiramari
"""

import requests
import pandas as pd
import json


def fetch_and_save_users(api_key, url, output_file):
    """
    Fetches user data from the API, formats it, and saves it to a CSV file.

    Args:
        api_key (str): Your API key for authentication.
        url (str): The API endpoint URL.
        output_file (str): The name of the output CSV file.
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
                    "rolePrincipal.ID": element.get("rolePrincipal", {}).get("id"),
                    "manager.ID": element.get("manager", {}).get("id"),
                    "department.ID": element.get("department", {}).get("id"),
                }
                formatted_items.append(formatted_item)
            
            # Convert the data into a DataFrame
            df = pd.DataFrame(formatted_items)
            
            # Save the DataFrame to a CSV file
            df.to_csv(output_file, index=False)
            print(f"The data has been saved to {output_file}")
        else:
            print(f"Request failed. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
        
def fetch_and_save_departments(api_key, url, output_file):
    """
    Fetches department data from the API, formats it, and saves it to a CSV file.

    Args:
        api_key (str): Your API key for authentication.
        url (str): The API endpoint URL.
        output_file (str): The name of the output CSV file.
    """
    headers = {
        "Authorization": f"lucca application={api_key}",
        "Accept": "application/json"
    }
    url = url + "/api/v3/departments?fields=id,name,code,hierarchy,parentID,level,sortOrder,headID,currentUsers.ID"
    try:
        # Effectuer la requête GET
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("Requête réussie.")
            
            # Extraire les données
            items = response.json().get('data', {}).get('items', [])
            formatted_items = []
            
            # Formater les éléments
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
                    "currentUsers": [user["id"] for user in element.get("currentUsers", [])]
                }
                formatted_items.append(formatted_item)
            
            # Convertir les données en DataFrame
            df = pd.DataFrame(formatted_items)
            
            # Sauvegarder le DataFrame dans un fichier CSV
            df.to_csv(output_file, index=False)
            print(f"Les données ont été sauvegardées dans {output_file}")
        else:
            print(f"Échec de la requête. Code : {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
# url = "https://reflect2-sandbox.ilucca-demo.net"
# API_KEY = "caf8058b-b7ec-4df2-85e3-a673b5466e97"
# output_file_departments = "Departments.csv"
# output_file_users = "Users.csv"

# fetch_and_save_departments(API_KEY, url, output_file_departments)
# fetch_and_save_users(API_KEY, url, output_file_users)
        

def fetch_data_daily(config_path):
    """
    Fetches data from multiple endpoints based on the configuration file.

    Args:
        config_path (str): Path to the JSON configuration file.
    """
    try:
        # Load configuration
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        api_key = config.get("api_key")
        endpoints = config.get("endpoints", [])
        
        for endpoint in endpoints:
            endpoint_type = endpoint.get("type")
            base_url = endpoint.get("base_url")
            output_file = endpoint.get("output_file")
            
            if endpoint_type == "users":
                fetch_and_save_users(api_key, base_url, output_file)
            elif endpoint_type == "departments":
                fetch_and_save_departments(api_key, base_url, output_file)
            else:
                print(f"Unknown endpoint type: {endpoint_type}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the script to run daily 
config_path = "config.json"
fetch_data_daily(config_path)

    
    
    
    
    
    
    
    
    
