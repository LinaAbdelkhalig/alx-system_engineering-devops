#!/usr/bin/python3
"""
This script uses a rest api and returns information about an employee
"""

import csv
import requests
import sys


def get_employee_todo(emp_id):
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list data
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    emp_name = user_data.get('name')

    # Creating the CSV file and writing the data
    filename = f"{emp_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([emp_id, emp_name, todo.get('completed'),
                             todo.get('title')])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    get_employee_todo(emp_id)
