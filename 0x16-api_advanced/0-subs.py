#!/usr/bin/python3
"""
the module contains a function that
queries the reddit api and returns the number of subscribers for ta given sub
"""


import requests


def number_of_subscribers(subreddit):
    """this function uses the reddit api
        to return the number of subsscribers
        subscribed to a particular "subreddit"

    Args:
        subreddit (str): name of the subreddit

    Returns:
        int: the number of subscribers if successful or 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-reddit-subscriber-counter'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        return data.get("subscribers")
    return 0
