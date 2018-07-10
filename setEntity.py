from telethon import TelegramClient
from pymongo import MongoClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

mongo = MongoClient('localhost',27017)
db = mongo.zzc
user_col = db.user

msg = client.get_entity('+8615210086506')
msg_item = msg.to_dict()
print(msg_item)
user = {
	'id': str(msg_item['id']),
	'phone': str(msg_item['phone']),
	'username': str(msg_item['username']),
	'first_name': str(msg_item['first_name']),
	'last_name': str(msg_item['last_name'])
}
user_col.insert(user)

print('insert success')
