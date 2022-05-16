#!/usr/bin/python3
'''export data in the JSON format'''
import json
from requests import get
from sys import argv
if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    x = get(URL)
    y = get(URL2)
    l = []
    dict2 = {}
    file = "{}.json".format(argv[1])
    response = x.json()
    response2 = y.json()
    name = response2.get('username')
    for i in range(0, len(response)):
        if response[i]["userId"] == int(argv[1]):
            dict = {}
            dict["task"] = response[i]["title"]
            dict["completed"] = response[i]["completed"]
            dict["username"] = name
            l.append(dict)
    dict2[argv[1]] = l
    with open(file, mode="w") as x:
        json.dump(dict2, x)
