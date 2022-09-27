#!/usr/bin/python3
"""
recursive function that queries the Reddit API
returns a list of titles of all hot articles
for a given subreddit
If an invalid subreddit, return None
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """titles of all hot articles of subreddit"""
    try:
        if subreddit is not None:
            headers = {"User-Agent": "cienyan"}
            params = {'t': 'all', 'after': after}
            resquest = requests.get("http://www.reddit.com/r/{}/hot.json"
                                    .format(subreddit),
                                    headers=headers,
                                    params=params).json()
            data = resquest.get("data")
            posts = data.get("children")
            for post in posts:
                hot_list.append(post.get("data").get("title"))

            after = data.get("after")
            if after is not None:
                recurse(subreddit, hot_list, after)

            return hot_list
    except Exception:
        return None
