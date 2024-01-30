#!/usr/bin/python3
"""sdjasjkdh skjdh askhdsaj khasjkd hsajkhd askjh"""
import requests
import sys


if __name__ == '__main__':
    URL = "https://jsonplaceholder.typicode.com"

    user = requests.get(f'{URL}/users/{sys.argv[1]}').json()
    user_name = user["name"]

    todo_list = requests.get(f'{URL}/users/{sys.argv[1]}/todos').json()

    done_tasks, t_tasks = 0, 0
    for task in todo_list:
        if task["completed"] is True:
            done_tasks = done_tasks + 1
        t_tasks = t_tasks + 1

    print(f"Employee {user_name} is done with tasks({done_tasks}/{t_tasks}):")
    for task in todo_list:
        if task["completed"] is True:
            print(f"\t {task['title']}")