#!/usr/bin/python3
"""Gather data from an API"""

from sys import argv

import requests

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = [task.get('title') for task in todos if task.get('completed')]
    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
        user.get('name'), len(completed), len(todos)
    ))

    [print("\t {:s}".format(task)) for task in completed]
