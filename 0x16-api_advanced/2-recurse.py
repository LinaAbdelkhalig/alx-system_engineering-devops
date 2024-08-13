#!/usr/bin/python3
"""
this is a module that contains a recursive function that
returns the titles of the ot posts from a particular
subreddit and appends them to a list
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    queries the api recursively and adds posts titles

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to collect the titles of hot articles.

    Returns:
        list: A list containing titles of all hot articles, or None if
              the subreddit is invalid or if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'reddit-topten-posts'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post.get("data", {}).get("title", "")
            if title:
                hot_list.append(title)

        after = data.get("data", {}).get("after", None)
        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list

    return None
