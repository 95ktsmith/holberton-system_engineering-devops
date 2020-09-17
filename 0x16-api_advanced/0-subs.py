#!/usr/bin/python3
""" Number of subscribers on a subreddit """


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers on a subreddit, or 0 if
        subreddit is not valid.
    """
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'PlaceholderAgent'})
    if r.status_code != 200:
        return (0)
    return (r.json()['data']['subscribers'])
