#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"} 
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    for post in response.json().get("data", {}).get("children", []):
        print(post.get("data", {}).get("title"))
