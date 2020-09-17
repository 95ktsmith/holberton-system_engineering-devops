#!/usr/bin/python3
""" Number of subscribers on a subreddit """


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers on a subreddit, or 0 if
        subreddit is not valid.
    """
    import requests
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, allow_redirects=False,
                     headers={'User-Agent': 'PlaceholderAgent'})
    if r.status_code == 200:
        for post in r.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
