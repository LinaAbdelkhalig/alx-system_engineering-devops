#!/usr/bin/python3
"""
this script fetches the employee's todo data and converts it into json
"""

import json
import requests
import sys


def export_to_JSON(emp_id):
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list data
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee username
    employee_username = user_data.get('username')

    # Prepare the data for JSON export
    todo_list = []
    for todo in todos_data:
        todo_item = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee_username
        }
        todo_list.append(todo_item)

    data = {str(emp_id): todo_list}

    # Create the JSON file and write the data
    filename = f"{emp_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <emp_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    export_to_JSON(emp_id)
