#!/usr/bin/python3
""" List of all Hot posts """


def recurse(subreddit, hot_list=[], after=""):
    """ Returns a list of all posts under Hot, or None if subreddit is invalid
    """
    import requests

    if after is None:
        return []
    elif len(after) == 0:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".\
              format(subreddit, after)

    r = requests.get(url,
                     allow_redirects=False,
                     headers={'User-Agent': 'PlaceholderAgent'})

    if r.status_code == 200:
        if r.json()['data']['children'] is not None:
            for post in r.json()['data']['children']:
                hot_list.append(post['data']['title'])
    else:
        return None

    return (hot_list + recurse(subreddit, hot_list, r.json()['data']['after']))
