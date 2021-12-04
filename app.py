#App api_id:
#5086045
#App api_hash:
#e0bcc2b6aba38988f6675767aee63591

import configparser
import json
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
import datetime
import parser_rsa_rf
import parser_rsamonitor
import parser_egarant_limiti


api_id = "5086045"
api_hash = "e0bcc2b6aba38988f6675767aee63591"
#аккаунт получателя алярма
alarm_receiver = "IC_quantity"
#название канала
entity = "rsa_rf", "rsamonitor", "egarant_limiti"
#максимальное количество квот при котором отправляется сообщение (включительно)
max_quotes = 1
max_polis = 2
time = datetime.datetime.now()

client = TelegramClient("anon", api_id, api_hash)
client.start()
print("Client Created")

@client.on(events.NewMessage(chats=entity))
async def my_event_handler(event):
    #разбиваем сообщение по строкам
    text=event.message.message.split("\n")
    print("reading message")
    parser_rsa_rf(text)
    parser_rsamonitor(text)
    parser_egarantl_limiti(text)

with client:
    client.run_until_disconnected()
