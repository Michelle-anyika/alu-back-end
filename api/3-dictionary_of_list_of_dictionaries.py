#!/usr/bin/python3
"""
Exports all employee tasks to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[user_id] = []

        for task in todos:
            if task.get("userId") == user_id:
                task_data = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                all_tasks[user_id].append(task_data)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)

