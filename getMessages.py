from telethon import TelegramClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

from telethon.tl.functions.messages import GetHistoryRequest

result = client(GetHistoryRequest(
    peer=1116410516,      # On which chat/conversation
    offset_id=0,    # ID of the message to use as offset
    offset_date=None,    # ID of the message to use as offset
    add_offset=0,   # Additional offset
    limit=10,       # How many results
    max_id=0,       # Maximum message ID
    min_id=0,       # Minimum message ID
    hash=0          # Special number to return nothing on no-change
))
for item in result.to_dict()['messages']:
	if 'message' in item:
		print(item['message'])
#for item in result.messages:
#	print(item)
#print(result.messages)
#print(result.to_dict()['chats'][0]['title'].encode('utf-8'))
#print(result)
