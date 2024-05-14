import requests
import datetime
import time

# Замените на свой токен бота
bot_token = '6420636316:AAGFcU-CI9sucLIiMOp4dcGmFfXo9ig6pks'

# Замените на ID чата или пользователя, которому нужно отправить сообщение
chat_id = '541549984'

def send_message(message):
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(send_text)
    return response.json()

def send_message_at_8am():
    while True:
        now = datetime.datetime.now()
        if now.hour == 7 or now.minute == 30:
            message = "Доброе утро, Мой господин!"
            send_message(message)
            break
        elif now.hour == 15 or now.minute == 30:
            message = 'Добрый вечер, Мой господин!'
            send_message(message)
            break
        else:
            time.sleep(60)  # Подождать минуту и проверить время снова

send_message_at_8am()