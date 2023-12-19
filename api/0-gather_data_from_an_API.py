#!/usr/bin/python3
"""sdjasjkdh skjdh askhdsaj khasjkd hsajkhd askjh"""
import requests
import sys


task_data = requests.get('https://jsonplaceholder.typicode.com/todos')
empl_data = requests.get('https://jsonplaceholder.typicode.com/users')

task_str = task_data.text.replace('true', 'True').replace('false', 'False')
empl_str = empl_data.text.replace('true', 'True').replace('false', 'False')

task_list = eval(task_str)
empl_list = eval(empl_str)

total_tasks = {}
done_tasks = {}
empl_dict = {}

for tasks in task_list:
    user_id = tasks['userId']
    total_tasks[user_id] = total_tasks.get(user_id, 0) + 1
    if tasks['completed']:
        done_tasks[user_id] = done_tasks.get(user_id, 0) + 1

for employee in empl_list:
    empl_dict[employee['id']] = employee['name']

if len(sys.argv) > 1:
    key = int(sys.argv[1])
    str1 = f'Employee {empl_dict[key]} is done with '
    str2 = f'({done_tasks[key]}/{total_tasks[key]}) tasks:'
    str_fin = str1 + str2 + '\n'
    for task in task_list:
        if task['completed'] and task['userId'] == key:
            str_fin += '\t ' + task['title'] + '\n'
    str_fin = str_fin[:-1]
    print(str_fin)
else:
    for key in done_tasks.keys():
        str1 = f'Employee {empl_dict[key]} is done with '
        str2 = f'({done_tasks[key]}/{total_tasks[key]}) tasks:'
        str_fin = str1 + str2 + '\n'
        for task in task_list:
            if task['completed'] and task['userId'] == key:
                str_fin += '\t ' + task['title'] + '\n'
        str_fin = str_fin[:-1]
        print(str_fin)
