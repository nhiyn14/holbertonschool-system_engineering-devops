#!/usr/bin/python3
""" for a given employee ID, returns his/her TODO list progress"""

import requests
from sys import argv


if __name__ == "__main__":
    """function to get employees todo list"""
    # Retrieve the employee infor + todo lists. Then convert to json
    employee_id = int(argv[1])
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(employee_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee_id)).json()

    # Make a list of done tasks
    done_task = []
    for task in todo:
        if task['completed'] is True:
            done_task.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".
          format(employee.get('name'), len(done_task), len(todo)))
    for task in done_task:
        print("\t {}".format(task))
