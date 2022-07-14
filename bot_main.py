from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "" #Токен авторизации с сообществом
vk_session = vk_api.VkApi(token=token) #Авторизация с сообществом по токену

def get_buttons(label, color, payload=''):#Создаем кнопку для клавиатуры
    return {
        'action': {
            'type': 'text',
            'payload': json.dumps(payload),
            'label': label
        },
        'color': color
    } #Создаем кнопку для клавиатуры

keyboard = {
    'one_time': False, #Параметр отвечающий за показ клавиатуры
    'buttons': [[get_buttons(label='Связь со специалистом', color='negative')]]
}#Создаем клавиатуру для отображения пользователя в которой 4 кнопки

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8') #Переводим клавиатуру в формат для ВК
keyboard = str(keyboard.decode('utf-8'))


def send_message(user_id, text): #Метод отправки сообщения пользователю
    vk_session.method("messages.send", {"user_id": user_id, "message": text, 'random_id': 0, 'keyboard': keyboard})

greetings = ['привет', 'здравствуй', 'ку', 'хелло', 'прив', 'начать', 'меню', 'доброе утро', 'добрый день', 'добрый вечер', 'здравствуйте', 'салют','здорово', 'приветствую']
bue = ['пока', 'досвидания', 'до свидания', 'до встречи', 'всего хорошего']
os = ['обратная связь', 'связь со специалистом', 'свяжи со сппециалистом', 'связь', 'помощь']
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session, 200112664) #Подключение к лонгпул серверу для прослушиания входящих сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text.lower() in greetings:
            send_message(event.user_id, "Доброго времени суток! Я - Бот, и пока мало чего умею, поэтому свяжитесь со специалистом!")
        elif event.text.lower() in bue:
            send_message(event.user_id, "До свидания, я буду ждать Вас здесь.")
        elif event.text.lower() in os:
            send_message(event.user_id, 'Специалист скоро свяжется с Вами!')
            send_message(529844902, 'Клиент ждёт Вас в чате.')
            send_message(223182527, 'Клиент ждёт Вас в чате.')
            send_message(391899173, 'Клиент ждёт Вас в чате.')
            send_message(141307313, 'Клиент ждёт Вас в чате.')
        else:
            send_message(event.user_id, "Не понял Вас.")
