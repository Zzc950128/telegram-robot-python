from telethon import TelegramClient

app_id = 237708
app_hash = '500d225c06f5427ac74c38c69fb24686'
phone_number = '+8613020305798'

client = TelegramClient('zhangzhicong', app_id, app_hash)
client.start()

# For normal chats
from telethon.tl.functions.messages import AddChatUserRequest

client(AddChatUserRequest(
#    chat_id,
#    user_to_add,
    305536970,
#    258594619,
    616027765,
    fwd_limit=10  # Allow the user to see the 10 last messages
))

from telethon.tl.functions.channels import InviteToChannelRequest

#client(InviteToChannelRequest(
#    channel,
#    [users_to_add]
#     -305536970,
#     616027765
#))

