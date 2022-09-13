#!/usr/bin/python3
"""
export TODO list of all employee
in the JSON format
File name must be: todo_all_employees.json
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """function to get todo list of all employee"""
    # Retrieve all employee info + todo lists. Then convert to json
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    employees = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    # Make a dict where keys are employee_id
    id_dict = {}
    username_dict = {}
    for employee in employees:
        employee_id = employee.get('id')
        id_dict[employee_id] = []
        username_dict[employee_id] = employee.get('username')

    # Make inner dict for the given employee's id
    for task in todos:
        task_dict = {}
        employee_id = task.get("userId")
        task_dict['username'] = username_dict.get(employee_id)
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        id_dict.get(employee_id).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(id_dict, jsfile)
