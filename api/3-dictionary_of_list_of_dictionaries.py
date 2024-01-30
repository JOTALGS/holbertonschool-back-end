#!/usr/bin/python3
"""
    Using what from Task #0, extend the
    python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


def employee_progress():
    """ Show employee progres """
    URL = "https://jsonplaceholder.typicode.com"
    users = requests.get(f'{URL}/users').json()
    todo_list = requests.get(f'{URL}/todos').json()

    filename = f"todo_all_employees.json"

    with open(filename, "w") as f:

        progress = {}
        for user in users:
            progress[user["id"]] = []

            todo_id = requests.get(f'{URL}/users/{user["id"]}/todos').json()

            for task in todo_id:
                task_dict = {}
                task_dict["username"] = user["username"]
                task_dict["task"] = task["title"]
                task_dict["completed"] = task["completed"]
                progress[user["id"]].append(task_dict)

        f.write(json.dumps(progress))
        

if __name__ == "__main__":
    employee_progress()
