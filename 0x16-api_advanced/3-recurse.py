#!/usr/bin/python3
""" recursive function that queries the Reddit API """

import requests
import sys
params = {'limit': 100, 'after': fn}

def recurse(subreddit, hot_list=[]):
    """    Args:
        subreddit: subreddit name
        hot_list: list of hot title in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    
    global after
    headers = {'User-Agent': 'My User Agent'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after: after'}
    res = requests.get(url, headers=headers, allow_redirects=False, params=parameters)
    item  = res.json().get('data').get('children')
    fn = item.get('kind') + '_' + item.get('data').get('id')

    
    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for t in list_titles:
            hot_list.append(t.get('data').get('title'))
        return hot_list
    else:
        return (None)
