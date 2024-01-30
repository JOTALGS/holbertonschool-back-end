#!/usr/bin/python3
"""
oiuyiugjkygjhguyfbg jhv
"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    USER = sys.argv[1]
    COMPLETED = TOTAL_TASK = 0
    TODOS_URL = f'https://jsonplaceholder.typicode.com/todos?userId={USER}'
    EMPLOYEE_URL = f'https://jsonplaceholder.typicode.com/users/{USER}'

    # Request for the taks
    with urllib.request.urlopen(TODOS_URL) as response:
        todos_data = response.read().decode()

    # Request for the employee info
    with urllib.request.urlopen(EMPLOYEE_URL) as response:
        employee_data = response.read().decode()

    employee_info = {}
    try:
        employee_taks = json.loads(todos_data)
        employee_info = json.loads(employee_data)
    except json.JSONDecodeError:
        print('Response could not be serialized')

    # Get all the taks name in order and how many are complete.
    tasks_list = []
    for task in employee_taks:
        tasks_list.append({
            'task': task['title'],
            "completed": task['completed'],
            "username": employee_info['name']}
        )

    with open(f'{USER}.json', 'w', encoding='utf8') as f:
        f.write(json.dumps({str(USER): tasks_list}, indent=4))
