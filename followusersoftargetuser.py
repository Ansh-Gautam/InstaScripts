import random
import time
from instagrapi import Client

target_user = input("Enter the target user : ")
print(f"Target user :{target_user}")
password = 'password'
username = 'usename'
client = Client()
client.login(username, password)
 
target_id = client.user_id_from_username(target_user)

followers = client.user_followers(target_id,0)

for key in followers.keys():
    userid = followers[key].pk
    name = followers[key].username
    print(f"Followed : {name}")
    client.user_follow(userid)
    client.delay_range = [10,60]

