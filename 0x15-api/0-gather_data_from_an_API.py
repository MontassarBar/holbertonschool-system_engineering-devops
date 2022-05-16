#!/usr/bin/python3
'''Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress'''
from sys import argv
from requests import get
if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    x = get(URL)
    y = get(URL2)
    c = 0
    v = 0
    response = x.json()
    response2 = y.json()
    name = response2.get('name')
    for i in range(0, len(response)):
        if response[i]["userId"] == int(argv[1]):
            c += 1
            if response[i]["completed"] is True:
                v += 1
    print("Employee {} is done with tasks({}/{}):".format(name, v, c))
    for i in range(0, len(response)):
        if response[i]["userId"] == int(argv[1]) and response[i][
                "completed"] is True:
            print("     ", response[i]["title"])
