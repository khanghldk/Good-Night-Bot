from fbchat import Client
from fbchat.models import *
import random
import config
import schedule
import time

client = Client(config.username, config.password)

def TestMessage():
	for friend in config.friendlist:
		mess = random.choice(config.mess).format(config.friendlist[friend])
		client.sendMessage(message = mess, thread_id = friend, thread_type = ThreadType.USER)
		time.sleep(1)

TestMessage()