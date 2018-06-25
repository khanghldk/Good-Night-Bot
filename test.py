from fbchat import Client
from fbchat.models import *
import random
import config
import schedule
import time

client = Client(config.username, config.password)

def NewYear():
	for friend in config.friendlist:
		wish = config.wish.format(config.friendlist[friend])
		client.sendRemoteImage(config.image, message=wish, thread_id=friend, thread_type=ThreadType.USER)
		time.sleep(1)

		mess = config.mess.format(config.friendlist[friend])
		client.sendMessage(message = mess, thread_id = friend, thread_type = ThreadType.USER)

schedule.every().day.at("20:25").do(NewYear)

while True:
    schedule.run_pending()
    time.sleep(1)