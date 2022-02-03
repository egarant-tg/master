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
string_session = "1ApWapzMBu2f2kSOeSv5_ylPQvqHW9ti3UvFwJm9seNAUyYRhmGoO7bsorJdqULdJb_2xaiv5HTHXBjVqnMZri_pDnc9EGh-FQ0Fpr3OiKtWcMNSrTdTU3elYhLk6niCtvt5-wiYfMTAfoVZcKNEGDskpkNauzfUCLyA5H5JfNGlxJlWbw5s1-tLCLOORCzVHsqf37grRo14AM00e9UioBDsQ6GitamrB2iSz3e0_UbhugtsuvCghE7y4VXb17L34VqeSM481AQO0vw_c0RZ7olPqUC_ywluueIxGh31EgtpouiDtKYcYh4rplJPsFh-cX8reATA5meBIa1BsBqxmDgvoeL11vhM="
#аккаунт получателя алярма
alarm_receiver = "IC_quantity"
#название канала
entity = "rsa_rf", "rsamonitor", "egarant_limiti"
#максимальное количество квот при котором отправляется сообщение (включительно)
max_quotes = 1
max_polis = 2
time = datetime.datetime.now()

client = TelegramClient(StringSession(string_session), api_id, api_hash)
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
