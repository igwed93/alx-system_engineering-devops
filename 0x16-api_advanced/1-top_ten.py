#!/usr/bin/python3
"""
Querry Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
        prints the titles of the first 1o hot posts
        prints None if an invalid subreddit is given
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent'})

    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
