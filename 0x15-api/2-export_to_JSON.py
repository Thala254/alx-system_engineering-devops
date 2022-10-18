#!/usr/bin/python3
"""script that queries an api and gives responses in json format"""
from collections import OrderedDict
from sys import argv
import csv
import json
import requests


def count(todos=None):
    """Counts ompleted tasks"""
    counter = 0
    for todo in todos:
        if todo.get('completed') is True:
            counter += 1
    return counter


def to_standard_output(user=None, todos=None):
    """prints reponse from api to standard output"""
    print("Employee {} is done with tasks ({}/{}):".format(
        user[0].get('name'),
        count(todos),
        len(todos)))
    for todo in todos:
        if todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))


def to_csv(user=None, todos=None):
    """prints response from an api to csv format"""
    with open(f'{argv[1]}.csv', 'w') as csv_file:
        fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow({"USER_ID": todo.get('userId'),
                             "USERNAME": user[0].get('username'),
                             "TASK_COMPLETED_STATUS": todo.get('completed'),
                             "TASK_TITLE": todo.get('title')})


def to_json(user=None, todos=None):
    """prints response from an api in json format"""
    with open(f'{argv[1]}.json', 'w') as json_file:
        task_dict = OrderedDict()
        task_objs = []
        for todo in todos:
            task_dict['task'] = todo.get('title')
            task_dict['completed'] = todo.get('completed')
            task_dict['username'] = user[0].get('username')
            task_objs.append(task_dict)
            task_dict = OrderedDict()
        data = {argv[1]: task_objs}
        json.dump(data, json_file)


if __name__ == "__main__":
    payload = {'id': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=payload).json()
    payload1 = {'userId': argv[1]}
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params=payload1).json()
    to_standard_output(user, todos)
    to_csv(user, todos)
    to_json(user, todos)
