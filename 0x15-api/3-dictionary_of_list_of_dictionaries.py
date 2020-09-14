#!/usr/bin/python3
""" Script that returns information about a given employee ID in CSV format"""
import json
import requests

if __name__ == "__main__":

    total_dict = {}
    for emp_id in range(1, 11):
        emp_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(emp_id)).json()['username']

        r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()

        tasks = []
        for task in r:
            tasks.append({
                            "task": task['title'],
                            "completed": task['completed'],
                            "username": emp_name
            })
        total_dict["{}".format(emp_id)] = tasks

    with open("todo_all_employees.json", "w+") as f:
        f.write(json.dumps(total_dict))
