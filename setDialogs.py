from telethon import TelegramClient
from pymongo import MongoClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

mongo = MongoClient('localhost',27017)
db = mongo.zzc
user_col = db.list
#mes_col = db.mes

#for item in result:
#	print(item)

msg = client.get_dialogs()

for msg_item in msg:
	msg_item = msg_item.to_dict()
	style = msg_item['entity']
#       print(style)
	if style.__class__.__name__ == 'User':
		if style.bot == False:
			user = {
				'name': msg_item['name'],
				'type': 'User',
				'id': str(style.id),
				'username': str(style.username),
				'first_name': str(style.first_name),
				'last_name': str(style.last_name)
			}
			user_col.insert(user)
		else:
			pass
#                print('name: ' + msg_item['name'] + ' type: User')
#                print('id: ' + str(style.id) + ' username: ' + str(style.username) + ' first_name: ' + str(style.first_name) + ' last_name: ' + str(style.last_name) + ' bot: ' + str(style.bot))
	elif style.__class__.__name__ == 'Chat':
		chat = {
			'name': msg_item['name'],
			'type': 'Chat',
			'title': str(style.title),
			'count': str(style.participants_count)
			'creator': str(style.creator)
		}
		user_col.insert(chat)
#                print('name: ' + msg_item['name'] + ' type: Chat')
#                print('id: ' + str(style.id) + ' title: ' + str(style.title) + ' count: ' + str(style.participants_count))
	else:
		channel = {
			'name': msg_item['name'],
			'type': 'Channel',
			'title': str(style.title)
			'creator': str(style.creator)
		}
		user_col.insert(channel)
#                print('name: ' + msg_item['name'] + ' type: Channel')
#                print('id: ' + str(style.id) + ' title: ' + str(style.title))
#       print('name: ' + msg_item['name'] + ' id: ' + str(style.id))

