#!/usr/bin/python3
"""sdjasjkdh skjdh askhdsaj khasjkd hsajkhd askjh"""
import requests
import sys
import csv


if __name__ == '__main__':
    URL = "https://jsonplaceholder.typicode.com"

    user = requests.get(f'{URL}/users/{sys.argv[1]}').json()
    todo_list = requests.get(f'{URL}/users/{sys.argv[1]}/todos').json()

    filename = f"{user['id']}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writer.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])
