#!/usr/bin/python3
"""
Gather data from API for a given employee ID.
Usage: ./0-gather_data_from_an_API.py <employee_id>
"""

import json
import sys
import urllib.request


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    try:
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode('utf-8'))
        with urllib.request.urlopen(tasks_url) as response:
            tasks_data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print("Error fetching data:", e)
        sys.exit(1)

    name = user_data.get("name")
    total_tasks = len(tasks_data)
    done_tasks = [task for task in tasks_data if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(done_tasks),
                                                          total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()

