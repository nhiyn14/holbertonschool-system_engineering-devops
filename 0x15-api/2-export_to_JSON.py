#!/usr/bin/python3
"""
for a given employee ID (USER_ID)
returns his/her TODO list progress
export data in the JSON format
File name must be: USER_ID.json
"""

import json
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

    # Make inner dict for the given employee's id
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = employee.get('username')
        tasks.append(task_dict)

    # Turn the inner dict into the value for the key = user_id
    json_file = {}
    json_file[employee_id] = tasks
    with open("{}.json".format(employee_id), 'w') as f:
        json.dump(json_file, f)
