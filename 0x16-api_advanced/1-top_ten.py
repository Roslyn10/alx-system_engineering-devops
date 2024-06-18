#!/usr/bin/python3
"""
A function that prints the titles of the first 10 hot posts
listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    response = requests.get(
            url, headers=headers,
            params=params, allow_redirects=False
            )

    if response.status_code == 200:
        for get_data in response.json().get("data", {}).get("children", []):
            data = get_data.get("data", {})
            title = data.get("title")
            print(title)
    else:
        print(None)
