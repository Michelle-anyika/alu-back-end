#!/usr/bin/python3
"""
Exports employee TODO list data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_resp.json()
    username = user_data.get("username")

    todos_resp = requests.get(todos_url)
    if todos_resp.status_code != 200:
        print("Failed to retrieve tasks")
        sys.exit(1)

    todos = todos_resp.json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(data, json_file)

