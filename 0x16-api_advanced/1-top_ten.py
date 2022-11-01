#!/usr/bin/python3
"""
    script that prints titles of the first 10 hot posts listed for a
    given subreddit
"""
import requests


def top_ten(subreddit):
    """
        queries Reddit API and prints titles of the first 10 hot posts
        listed for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    try:
        res = requests.get(url,
                           params={'limit': 10},
                           headers={'User-agent': 'yobra'},
                           allow_redirects=False).json()
        data = res['data'].get('children')
        for listing in data:
            print(f"{listing.get('data').get('title')}")
    except Exception:
        print("None")
