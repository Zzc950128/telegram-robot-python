from telethon import TelegramClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

msg = client.get_dialogs()
for msg_item in msg:
	msg_item = msg_item.to_dict()
	style = msg_item['entity']
#	print(style)
	if style.__class__.__name__ == 'User':
		if style.bot == False:
			print('name: ' + msg_item['name'] + ' type: User')
			print('id: ' + str(style.id) + ' username: ' + str(style.username) + ' first_name: ' + str(style.first_name) + ' last_name: ' + str(style.last_name) + ' bot: ' + str(style.bot))
	elif style.__class__.__name__ == 'Chat':
		print('name: ' + msg_item['name'] + ' type: Chat')
		print('id: ' + str(style.id) + ' title: ' + str(style.title) + ' count: ' + str(style.participants_count) + ' creator: ' + str(style.creator))
	else:
		print('name: ' + msg_item['name'] + ' type: Channel')  
		print('id: ' + str(style.id) + ' title: ' + str(style.title) + ' creator: ' + str(style.creator))
#	print('name: ' + msg_item['name'] + ' id: ' + str(style.id))
#for item in msg:
#	print(item)
