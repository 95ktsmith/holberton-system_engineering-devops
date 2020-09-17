#!/usr/bin/python3
""" Top Ten """


def top_ten(subreddit):
    """ Prints the first 10 post titles under Hot, or None if subreddit
        is invalid
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
