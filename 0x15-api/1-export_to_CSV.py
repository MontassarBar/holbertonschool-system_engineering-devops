#!/usr/bin/python3
'''export data in the CSV format'''
import csv
from requests import get
from sys import argv
if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    x = get(URL)
    y = get(URL2)
    file = "{}.csv".format(argv[1])
    response = x.json()
    response2 = y.json()
    name = response2.get('username')
    for i in range(0, len(response)):
        if response[i]["userId"] == int(argv[1]):
            with open(file, mode='a') as x:
                y = csv.writer(x, delimiter=',', quoting=csv.QUOTE_ALL)
                y.writerow([response[i]["userId"], name, response[i][
                    "completed"], response[i]["title"]])
