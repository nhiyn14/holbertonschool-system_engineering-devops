#!/usr/bin/python3
"""
for a given employee ID (USER_ID)
returns his/her TODO list progress
export data in the CSV format
File name must be: USER_ID.csv
"""

import csv
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

    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([employee_id, employee.get('username'),
                             task['completed'], task.get('title')])
