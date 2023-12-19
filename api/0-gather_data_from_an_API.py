#!/usr/bin/python3
"""sdjasjkdh skjdh askhdsaj khasjkd hsajkhd askjh"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # API endpoint for employee information
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    # API endpoint for employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Fetch employee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Extract relevant information
        employee_name = employee_data['name']
        done_tasks = [task['title'] for task in todo_data if task['completed']]
        number_of_done_tasks = len(done_tasks)
        total_number_of_tasks = len(todo_data)

        # Display the output
        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
        for task_title in done_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
