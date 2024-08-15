#!/usr/bin/python3
"""
This script uses a rest api and returns information about an employee
"""

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

    # Filter completed tasks and calculate progress
    completed_tasks = [todo.get('title')for todo in
                       todos_data if todo.get('completed')]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Display the TODO list progress
    print(f"Employee {emp_name} is done with "
          f"tasks({done_tasks}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./todo.py <employee_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    get_employee_todo(emp_id)
