#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get('title') for task in todos if task.get('completed')]
    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
        user.get('name'), len(completed), len(todos)
    ))

    [print("\t {:s}".format(task)) for task in completed]
