#!/usr/bin/python3
'''function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit'''

from requests import get


def top_ten(subreddit):
    URL = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    x = get(URL, headers={'User-agent': 'monta'})
    response = x.json()
    if (response == {'message': 'Not Found', 'error': 404}):
        return (0)
    else:
        i = 0
        y = response.get("data").get("children")
        while (i < 10):
            j = y[i].get('data').get('title')
            print(j)
            i += 1
