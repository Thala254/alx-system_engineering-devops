#!/usr/bin/python3
"""
    script that prints a list of titles for all hot articles for a
    given subreddit
"""
import requests

req = requests.Session()
req.headers.update({'User-Agent': 'yobra'})
req.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    """
        recursively queries Reddit API and returns a list of titles of
        all hot articles for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    try:
        res = req.get(url).json()
        for article in res['data']['children']:
            hot_list.append(article['data']['title'])
        if res['data']['after']:
            req.params = {'after': res['data']['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except Exception:
        return None
