#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Script that gathers data from API for a given employee id.
"""

import requests
import sys


def gather_data(employee_id):
    """
    Fetch user and todo data from JSONPlaceholder API
    and display the user name and number of completed tasks.
    """
    user_url = (
        "https://jsonplaceholder.typicode.com/users/"
        f"{employee_id}"
    )
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos?userId="
        f"{employee_id}"
    )

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error fetching data")
        return

    user_data = user_response.json()
    todos = todo_response.json()

    name = user_data.get('name')
    total_tasks = len(todos)
    completed_tasks = sum(1 for task in todos if task.get('completed') is True)

    print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")

    for task in todos:
        if task.get('completed') is True:
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    gather_data(employee_id)

