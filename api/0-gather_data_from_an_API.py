#!/usr/bin/python3
"""sdjasjkdh skjdh askhdsaj khasjkd hsajkhd askjh"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    USER = sys.argv[1]
    COMPLETED = TOTAL_TASK = 0
    TASK_LIST = ""
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
    for task in employee_taks:
        if task['completed'] is True:
            COMPLETED += 1
            TASK_LIST += f"\t {task['title']}\n"
        TOTAL_TASK += 1

    employee_name = employee_info['name']

    # Format the all print for the employee taks
    t_info = f"is done with tasks({COMPLETED}/{TOTAL_TASK}):\n{TASK_LIST[:-1]}"
    print_employee = f"Employee {employee_name} " + t_info

    print(print_employee)
