#!/usr/bin/python3
"""
This script fetches the employee todo and converts it into json
"""

import json
import requests


def get_all_employees_todo_progress():
    # Fetch all users data
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch all TODO list data
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare the data for JSON export
    data = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        data[user_id] = [{
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed')
        } for todo in todos_data if todo.get('userId') == user_id]

    # Create the JSON file and write the data
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    get_all_employees_todo_progress()
