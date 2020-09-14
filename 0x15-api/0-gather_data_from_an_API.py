#!/usr/bin/python3
""" Script that returns information about a given employee ID """

import requests
from sys import argv
import json

if __name__ == "__main__":
    emp_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1])).json()['name']
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1])).json()
    completed_tasks = 0
    total_tasks = len(r)
    for task in r:
        if task['completed'] is True:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(emp_name,
                                                          completed_tasks,
                                                          total_tasks))
    for task in r:
        if task['completed'] is True:
            print("\t{}".format(task['title']))
