async def parse_rsa_rf(text, client, alarm_receiver):
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
