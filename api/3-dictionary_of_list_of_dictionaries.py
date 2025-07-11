#!/usr/bin/python3
import requests
import json

if __name__ == "__main__":
    # Get all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        exit(1)

    users = users_response.json()
    todos = todos_response.json()

    # Create a dict mapping user id to username for easy access
    user_id_to_username = {user['id']: user['username'] for user in users}

    # Build the main dictionary
    all_tasks = {}

    for task in todos:
        user_id = str(task['userId'])
        task_dict = {
            "username": user_id_to_username.get(task['userId']),
            "task": task['title'],
            "completed": task['completed']
        }
        all_tasks.setdefault(user_id, []).append(task_dict)

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
