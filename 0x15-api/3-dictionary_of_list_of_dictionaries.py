#!/usr/bin/python3
'''export data in the JSON format'''
import json
from requests import get
if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/"
    x = get(URL)
    y = get(URL2)
    l = []
    dict2 = {}
    file = "todo_all_employees.json"
    response = x.json()
    response2 = y.json()
    for j in range(1, len(response2)):
        for i in range(0, len(response)):
                dict = {}
                dict["username"] = response2[j]["username"]
                dict["task"] = response[i]["title"]
                dict["completed"] = response[i]["completed"]
                l.append(dict)
        dict2[j] = l
    with open(file, mode="w") as x:
        json.dump(dict2, x)
