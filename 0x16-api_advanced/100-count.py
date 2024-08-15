#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the titles of all hot articles, and prints a sorted count of given
keywords.
"""

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API and counts the occurrences of given
    keywords in the titles of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        word_count (dict): holds the count of each keyword
        after (str): The pagination token.

    """
    if word_count is None:
        word_count = defaultdict(int)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my-reddit-hot-posts'}
    params = {'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            sorted_words = sorted(word_count.items(),
                                  key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")
            return

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                word_count[word] += len(re.findall(rf'\b{re.escape(word)}\b',
                                                   title, re.IGNORECASE))

        after = data.get("data", {}).get("after", None)
        if after:
            return count_words(subreddit, word_list, word_count, after)

    return None
