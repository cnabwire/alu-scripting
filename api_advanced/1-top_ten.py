#!/usr/bin/python3
"""Script that fetches the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit.
    If subreddit is invalid, print OK."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = (
        "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    )

    response = requests.get(
        subreddit_url, headers=headers, allow_redirects=False
    )

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get("data", {}).get("children", [])
        if posts:
            for i in range(min(10, len(posts))):
                print(posts[i].get("data", {}).get("title"))
        else:
            print("OK", end+"")  # Fix: Changed "None" to "OK" for empty subreddits
    else:
        print("OK", end="")  # Fix: Changed "None" to "OK" for invalid subreddits

