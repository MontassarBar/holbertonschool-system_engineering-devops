#!/usr/bin/python3
'''function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit'''

from requests import get


def top_ten(subreddit):
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    x = get(URL, headers={'User-agent': 'monta'})
    response = x.json()
    if (response == {'message': 'Not Found', 'error': 404}):
        print('None')
    else:
        y = response.get("data").get("children")
        for i in range(0, 10):
            j = y[i].get('data').get('title')
            print(j)
