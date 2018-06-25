from fbchat import log, Client # Nạp thư viện của fbchat

class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id) # Đánh dấu đã nhận tin nhắn
        self.markAsRead(author_id) # Đánh dấu đã đọc tin nhắn
        
        # Nếu id của tác giả tin nhắn không phải là bạn thì
        if author_id != self.uid:
        	# Gửi tin nhắn cho cuộc hội thoại có id là thread_id
            self.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

client = EchoBot("*", "*") # Điền email, password tài khoản Facebook của bạn vô đây
client.listen() # Bot sẽ chạy cập nhật tin nhắn