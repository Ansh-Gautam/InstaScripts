import random
from instagrapi import Client

password = 'goodansh2000'
username = 'an_us_kha'
client = Client()
client.login(username,password)
hashtag = "selfielove"
#comments = ["Great Post","Blissful Post","Happy for you","Its Wonderful"]
comments = [
    "Looking gorgeous! ❤️",
    "You are absolutely stunning! 😍",
    "Love the selfie, you are a natural beauty! 🌸",
    "Your smile is so infectious! 😊",
    "Beautiful picture! 🔥",
    "Love your confidence, keep shining! ✨",
    "You're so photogenic! 😘",
    "Slaying it with this selfie! 🔥",
    "Gorgeous shot! 📸",
    "You look amazing, keep slaying! 💕",
    "Absolutely stunning! 😍",
    "Beautiful selfie, you have such a great smile! 😊",
    "Love the picture, you are a natural beauty! 🌸",
    "You're a natural in front of the camera! 😘",
    "Flawless shot! 🔥",
    "This picture is amazing, love your style! ✨",
    "You are stunning, keep shining! 💕",
    "Great selfie, you have such a lovely personality that shines through! 🌟",
    "Love the selfie, you are rocking it! 🙌",
    "Incredible shot, you are a true beauty! 😍"
]

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
