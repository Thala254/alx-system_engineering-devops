#!/usr/bin/python3
"""
Script to make request from an API
"""
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


def to_csv(user=None, todos=None, file_name=None):
    """prints response from an api to csv format"""
    with open(file_name, 'w') as csv_file:
        fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow({"USER_ID": todo.get('userId'),
                             "USERNAME": user[0].get('username'),
                             "TASK_COMPLETED_STATUS": todo.get('completed'),
                             "TASK_TITLE": todo.get('title')})


def to_json(user=None, todos=None, file_name=None):
    """prints response from an api in json format"""
    with open(file_name, 'w') as json_file:
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


def to_json_all(users=None, todos=None, file_name=None):
    """prints response from an api in json format"""
    with open(file_name, 'w') as employees_file:
        data = {}
        for user in users:
            user_obj = []
            id = user.get('id')
            for todo in todos:
                task_dict = OrderedDict()
                if id == todo.get('userId'):
                    task_dict['task'] = todo.get('title')
                    task_dict['completed'] = todo.get('completed')
                    task_dict['username'] = user.get('username')
                    user_obj.append(task_dict)
            data[id] = user_obj
        json.dump(data, employees_file)


if __name__ == "__main__":
    try:
        user_payload = {'id': argv[1]}
        todo_payload = {'userId': argv[1]}
        json_file = f"{argv[1].json}"
        csv_file = f"{argv[1].csv}"
    except Exception:
        user_payload = {}
        todo_payload = {}
        json_file = 'todo_all_employees.json'
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=user_payload).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params=todo_payload).json()
    try:
        to_standard_output(user, todos)
        to_csv(user, todos, csv_file)
        to_json(user, todos, json_file)
    except Exception:
        to_json_all(user, todos, json_file)
