#!/usr/bin/python3
"""
queries the Reddit API
returns the number of subscribers for a given subreddit.
If an invalid subreddit, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers of subreddit)"""
    try:
        if subreddit is not None:
            headers = {"User-Agent": "cienyan"}
            resquest = requests.get("http://www.reddit.com/r/{}/about.json"
                                    .format(subreddit),
                                    headers=headers).json()
            data = resquest.get("data", {})
            subs = data.get('subscribers', 0)
            return subs
    except Exception:
        return 0
