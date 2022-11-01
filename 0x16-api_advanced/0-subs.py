#!/usr/bin/python3
"""script that finds the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
        queries Reddit API and returns the number of subscribers for a
        given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        res = requests.get(url,
                           headers={'User-agent': 'yobra'},
                           allow_redirects=False).json()
        return res['data'].get('subscribers')
    except Exception:
        return 0
