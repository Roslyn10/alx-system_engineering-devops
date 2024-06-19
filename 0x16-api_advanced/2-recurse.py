#!/usr/bin/python3
"""A function that queries the Reddit API and retuns all hot articles"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titels of all hot articles"""
