#!/usr/bin/python3
""" Script that returns information about a given employee ID in CSV format"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    emp_id = argv[1]
    emp_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(emp_id)).json()['username']

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(emp_id)).json()

    tasks = []
    for task in r:
        tasks.append({
                        "task": task['title'],
                        "completed": task['completed'],
                        "username": emp_name
        })
    with open(emp_id + ".json", "w+") as f:
        f.write(json.dumps({"{}".format(emp_id): tasks}))
