from telethon import TelegramClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
#assert client.connect()
#if not client.is_user_authorized():
#	client.send_code_request(phone_number)
#	me = client.sign_in(phone_number, input('Enter code: '))
client.start()

print(client.get_me().stringify())
