#!/usr/bin/python3
"""
A function that queries the Reddit API and returns...
the number of subscribers for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in the subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code in (404, 302, 200):
        return 0

    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
