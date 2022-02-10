#App api_id:
#5086045
#App api_hash:
#e0bcc2b6aba38988f6675767aee63591

import configparser
import json
import asyncio
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
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
#string_session  =  "1ApWapzMBu62vBenZBzr-NOhGlR3BlVst4V_8nKC0Vag1n5hI7TUY0stSet4-wCV218Q64Y6cbYpOzRVkC0_SmiXp5JZijwclv21ls09lq-j6_WL5okhC9yv_3B94pERxUCgtLjy5Zo6Dgd-qnlpNbASsf8qLoKQq6HnnFmjH_PvkwcSQVoHJS1GKRSrkLznMdFp1DXoTMTdkNXLTiGqxVdRZ8AkrROeuzrKVIwiG5H_inO8flZ5pElgJx0RkBg8LDdYXkUGYDNQHUllqjio9w9960TrQItFfaJCW2CsqYyt6batETFZOqbtxDSxkOEkEJbiq7gcR-WRzegKCZhxREeltTGaPMUs="
string_session = "1ApWapzMBu0bZla1lYqDwSJnRI6nasEwABF4LOxOxSFq6RjzSEvHizF4mTk94Mw9r3XXOGjKGCafF6jt6V7Ps7TP3ri1yt3xThYGatUGqLntxrRoYx7WK1Ry786BVwYw2v9is0pMMWUGR91SsRXrCL2-Bcmrmi-HKEq22bA-yU6CdXe--TzOCsLZJH3Q4McOXYsHikTZjIgikVSdtKKa9PSrFkHbGH_a9S-ohiwGKCN6ZEsGnRsww3g55Q5o4rr6hfPrg4Pp_Pcf1E-_TV5BJxovEbwoaqQeSC0NMtZEOD50aRD1eeV5PZdAPhYMMctJERXE3vbEYH0hMHHWd2W1Xhh5NQraQS3U="
#аккаунт получателя алярма
alarm_receiver = "IC_quantity"
#название канала
entity = "rsa_rf", "rsamonitor", "egarant_limiti"
#максимальное количество квот при котором отправляется сообщение (включительно)
max_quotes = 1
max_polis = 2
time = datetime.datetime.now()


cd desktop/tgapp/mastetclient = TelegramClient(StringSession(string_session), api_id, api_hash)
#client = TelegramClient("anon", api_id, api_hash)
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
