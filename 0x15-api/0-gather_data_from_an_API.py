#!/usr/bin/python3
from requests import get
from sys import argv
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
            if response[i]["completed"] == True:
                v += 1
    print("Employee {} is done with tasks({}/{}):".format(name, v, c))
    for i in range(0, len(response)):
        if response[i]["userId"] == int(argv[1]) and response[i]["completed"] == True:
            print("     ",response[i]["title"])
