#!/usr/bin/python3
'''function that queries the Reddit API and
returns the number of subscribers'''

from requests import get


def number_of_subscribers(subreddit):
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    x = get(URL, headers={'User-agent': 'monta'})
    response = x.json()
    if (response == {'message': 'Not Found', 'error': 404}):
        return (0)
    else:
        y = response.get("data").get("subscribers")
        return (y)
