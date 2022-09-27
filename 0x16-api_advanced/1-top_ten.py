#!/usr/bin/python3
"""
queries the Reddit API
prints titles of top 10 hot posts listed for a given subreddit
If an invalid subreddit, print None
"""
import requests


def top_ten(subreddit):
    """prints titles of top 10 hot posts of subreddit)"""
    try:
        if subreddit is not None:
            headers = {"User-Agent": "cienyan"}
            limit = {"limit": 10}
            resquest = requests.get("http://www.reddit.com/r/{}/hot.json"
                                    .format(subreddit),
                                    headers=headers,
                                    params=limit).json()
            data = resquest.get("data")
            posts = data.get("children")
            for post in posts:
                print(post.get("data").get("title"))
    except Exception:
        print(None)
