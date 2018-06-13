from telethon import TelegramClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

filter = InputMessagesFilterEmpty()
result = client(SearchRequest(
    peer=1116410516,      # On which chat/conversation
    q='',      # What to search for
    filter=filter,  # Filter to use (maybe filter for media)
    min_date=None,  # Minimum date
    max_date=None,  # Maximum date
    offset_id=0,    # ID of the message to use as offset
    add_offset=0,   # Additional offset
    limit=10,       # How many results
    max_id=0,       # Maximum message ID
    min_id=0,       # Minimum message ID
    from_id=557106529,   # Who must have sent the message (peer)
    hash=0          # Special number to return nothing on no-change
))
print(result)
