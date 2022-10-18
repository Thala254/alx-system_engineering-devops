#!/usr/bin/python3
"""api module"""
import requests
from sys import argv


def count(todos=None):
    """Counts ompleted tasks"""
    counter = 0
    for todo in todos:
        if todo.get('completed') is True:
            counter += 1
    return counter


if __name__ == "__main__":
    payload = {'id': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=payload).json()
    payload1 = {'userId': argv[1]}
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params=payload1).json()
    print("Employee {} is done with tasks ({}/{}):".format(
        user[0].get('name'),
        count(todos),
        len(todos)))
    for todo in todos:
        if todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
