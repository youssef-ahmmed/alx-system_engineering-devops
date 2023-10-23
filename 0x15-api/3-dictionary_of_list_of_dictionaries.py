#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json

import requests

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users/").json()

    dict_format = {}
    for user in users:
        todos = requests.get(url + "todos",
                             params={"userId": user.get('id')}).json()

        dict_format.update({
            user.get('id'): [
                {"username": user.get('username'),
                 "task": task.get('title'),
                 "completed": task.get('completed')}
                for task in todos
            ]
        })

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(dict_format, f)
