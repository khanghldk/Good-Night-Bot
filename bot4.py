from fbchat import Client
from fbchat.models import *
import random
import config
import schedule
import time

client = Client(config.username, config.password)

def chucEn():
	wish = 'Giao thừa đến rồi, năm cũ đã qua đi, năm mới lại đến.\nChúc em và gia đình năm mới tâm an, vạn sự lành.\nChúc riêng em đồ án suông sẻ, công việc tốt đẹp, và nhất là luôn xinh đẹp.\nChúc mừng năm mới!\n'
	client.sendRemoteImage(config.image, message=wish, thread_id='100003961497991', thread_type=ThreadType.USER)
	time.sleep(1)
	mess = config.mess.format('em')
	client.sendMessage(message = mess, thread_id = '100003961497991', thread_type = ThreadType.USER)

def NewYear():
	for friend in config.friendlist:
		wish = config.wish.format(config.friendlist[friend])
		client.sendRemoteImage(config.image, message=wish, thread_id=friend, thread_type=ThreadType.USER)
		time.sleep(1)

		mess = config.mess.format(config.friendlist[friend])
		client.sendMessage(message = mess, thread_id = friend, thread_type = ThreadType.USER)

schedule.every().day.at("00:57").do(NewYear)
schedule.every().day.at("00:57").do(chucEn)

while True:
    schedule.run_pending()
    time.sleep(1)