#!/usr/bin/python3
"""
sdadsd sadsad asdsa
"""
import json
import requests
from sys import argv


def employee_progress(employee_id):
    """ sadsdsadsd sd sd"""
    URL = "https://jsonplaceholder.typicode.com"
    user = requests.get(f'{URL}/users/{employee_id}').json()
    username = user["username"]
    todo_list = requests.get(f'{URL}/users/{employee_id}/todos').json()

    filename = f"{employee_id}.json"
    with open(filename, "w") as f:
        progress = {f"{employee_id}": []}
        for task in todo_list:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = username
            progress[f"{employee_id}"].append(task_dict)

        f.write(json.dumps(progress))


if __name__ == "__main__":
    employee_progress(argv[1])
