#App api_id:
#5086045
#App api_hash:
#e0bcc2b6aba38988f6675767aee63591

import configparser
import json
import asyncio
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
import datetime
from parser_rsa_rf import parse_rsa_rf
from parser_rsamonitor import parse_rsamonitor
from parser_egarant_limiti import parse_egarant_limiti


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
    await parse_rsa_rf(text, client, alarm_receiver)
    await parse_rsamonitor(text, client, alarm_receiver)
    await parse_egarant_limiti(text, client, alarm_receiver)

with client:
    client.run_until_disconnected()
