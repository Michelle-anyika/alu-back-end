#!/usr/bin/python3
import requests
import sys
import json

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
        print("Failed to get todos")
        sys.exit(1)
    todos = todos_resp.json()

    output = {
        str(employee_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            } for task in todos
        ]
    }

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump(output, json_file)

