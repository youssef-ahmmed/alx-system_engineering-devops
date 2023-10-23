#!/usr/bin/python3
"""Export to CSV"""

import csv
from sys import argv

import requests

if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open('{}.csv'.format(user_id), mode='w') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)

        [writer.writerow([user_id, user.get('username'),
                          task.get('completed'), task.get('title')])
         for task in todos]
