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
    for line in text:
        #ищем нужную строку
        if "Количество СК в РСА: " in line: #настройки для "rsa_rf"
            #ищем в ней цифры
            line_with_sk = line.split()
            for n in line_with_sk:
                if n.isdigit() and int(n)>20:
                    print("Количество СК меньше или равно двум, отправляю сообщение...")
                    await client.send_message(alarm_receiver, "Возможно квота. На Е-Гаранте больше 20 СК!")
        elif "Согласие:" in line:
            #ищем в ней цифры
            line_with_sk = line.split()
            for n in line_with_sk:
                if n.isdigit() and int(n)>2:
                    print("СК 'Согласие' есть на Е-Гаранте")
                    await client.send_message(alarm_receiver, "СК 'Согласие' больше 3")
        elif "БАСК:" in line:
            #ищем в ней цифры
            line_with_sk = line.split()
            for n in line_with_sk:
                if n.isdigit() and int(n)<=200:
                    print("СК 'БАСК' меньше 200")
                    await client.send_message(alarm_receiver, "СК 'БАСК' меньше 200")
        elif "Количество компаний в РСА: " in line: #настройки для "rsamonitor"
            #ищем в ней цифры
            line_with_sk = line.split()
            for n in line_with_sk:
                if n.isdigit() and int(n)>20:
                    print("Количество СК меньше или равно двум, отправляю сообщение...")
                    await client.send_message(alarm_receiver, "Возможно квота. На Е-Гаранте больше 20 СК!")
        elif "Согласие" in line:
            #ищем в ней цифры
            line_with_sk = line.split()
            for n in line_with_sk:
                if n.isdigit() and int(n)>2:
                    print("СК 'Согласие' есть на Е-Гаранте")
                    await client.send_message(alarm_receiver, "СК 'Согласие' больше 3")
        elif "БАСК" in line:
            #ищем в ней цифры
            line_with_sk = line.split()
            for n in line_with_sk:
                if n.isdigit() and int(n)<=200:
                    print("СК 'БАСК' меньше 200")
                    await client.send_message(alarm_receiver, "СК 'БАСК' меньше 200")

with client:
    client.run_until_disconnected()
