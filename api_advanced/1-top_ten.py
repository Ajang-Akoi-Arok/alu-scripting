#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    PARAMS = {"limit": 10}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, params=PARAMS,
                                allow_redirects=False)
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        for post in HOT_POSTS:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
