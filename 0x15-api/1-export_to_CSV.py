#!/usr/bin/python3
""" Script that returns information about a given employee ID in CSV format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    emp_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(emp_id)).json()['username']

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(emp_id)).json()

    with open(emp_id + ".csv", "w+") as f:
        for task in r:
            title = task['title']
            completed = task['completed']
            line = '"{}","{}","{}","{}"\n'.format(emp_id,
                                                  emp_name,
                                                  completed,
                                                  title)
            f.write(line)
