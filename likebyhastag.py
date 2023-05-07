import random
from instagrapi import Client

password = 'password'
username = 'username'
client = Client()
client.login(username,password)
hashtag = "selfielove"
comments = ["Great Post","Blissful Post","Happy for you","Its Wonderful"]

medias = client.hashtag_medias_recent(hashtag,100)

for i,media in enumerate(medias):
	client.media_like(media.id)
	print(f"Liked post number : {i+1} of hashtag {hashtag}")
	if i%4 == 0:
		client.delay_range = [10,60]
		client.user_follow(media.user.pk)
		print(f"Followed user : {media.user.username}")
		comment = random.choice(comments)
		client.media_comment(media.id,comment)
		print(f"Commented : {comment} under post {i+1}")
