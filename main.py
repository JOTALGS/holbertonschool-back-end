import subprocess
import sys
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    task = None
    filename = 'student_output'
    count = 0
    with open(filename, 'r') as f:
        output = f.read()
        for i in resp:
            if (i['completed'] and i['userId'] == id):
                task = i['title']
                count += 1
                if output.find(task) is not -1:
                    print("Task {} in output: OK".format(count))
                else:
                    print("Task {} not in output".format(count))

def run_your_script(script_path, script_argument):
    try:
        with open('student_output', 'w') as file:
            subprocess.run(['python3', script_path, script_argument], stdout=file, text=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error running the script: {e}")

if __name__ == "__main__":
    # Replace 'your_script.py' with the actual path to your script
    script_path = 'api/0-gather_data_from_an_API.py'

    # Replace 'your_argument' with the actual argument you want to pass
    script_argument = '1'

    run_your_script(script_path, script_argument)
    check_tasks(int(sys.argv[1]))
