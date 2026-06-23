#!/usr/bin/python3
"""Recursively collects all hot post titles for a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/yourname)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    hot_list += [child.get("data", {}).get("title")
                 for child in data.get("children", [])]
    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
