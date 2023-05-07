import random
import time
from instagrapi import Client

password = 'password'
username = 'username'
client = Client()
client.login(username, password)

followers = client.user_followers(client.user_id)
following = client.user_following(client.user_id)

key_to_unfollow = set(following.keys()).difference(followers.keys())
for key in key_to_unfollow:
    userid = following[key].pk
    name = following[key].username
    print(f"Unfollowed : {name}")
    client.delay_range = [10,60]
    client.user_unfollow(userid)

