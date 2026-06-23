#!/usr/bin/python3
"""
Function to query Reddit API and get top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
    
    Returns:
        None: Prints titles or None if invalid subreddit
    """
    # Set up the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (com.example.mybot)'
    }
    params = {
        'limit': 10
    }
    
    try:
        # Make the request with redirects disabled
        response = requests.get(url, headers=headers, params=params, 
                               allow_redirects=False)
        
        # Check if the request was successful and not a redirect
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])
        else:
            # Invalid subreddit or other error
            print(None)
            
    except requests.exceptions.RequestException:
        # Network error or other exception
        print(None)
