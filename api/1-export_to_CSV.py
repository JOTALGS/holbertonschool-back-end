#!/usr/bin/python3
"""sdjasjkdh skjdh askhdsaj khasjkd hsajkhd askjh"""
import csv
import requests
import sys


if __name__ == '__main__':
    URL = "https://jsonplaceholder.typicode.com"

    user = requests.get(f'{URL}/users/{sys.argv[1]}').json()
    todo_list = requests.get(f'{URL}/users/{sys.argv[1]}/todos').json()

    fn = f"{user['id']}.csv"
    with open(fn, 'w', encoding='utf-8') as f:
            for task in todo_list:
                f.write(f"{task['userId']}, {user['name']}, {task['completed']}, {task['title']}\n")