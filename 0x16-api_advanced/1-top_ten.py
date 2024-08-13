#!/usr/bin/python3
"""
the module contains a function that
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """this function returns the ttitles
    of the top ten posts in a subreddit

    Args:
        subreddit (str): name of the subreddit
    Returns:
        int: _description_
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'top-ten-hot-posts'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for i, post in enumerate(posts[:10]):
            title = post.get("data", {}).get("title", "")
            print(f"{i + 1}. {title}")
    else:
        print(None)
