import requests
import time
update_id = 1470776266
TOKEN = '2057362453:AAF4KKW38cqBVK5YW2sdn76mAxAObTP9_kY'

api_url = f'https://api.telegram.org/bot{TOKEN}/'

def send_request_with_method(method):
    return requests.get(api_url + method).json()

def send_message(text,chat_id):
    return send_request_with_method(f'sendMessage?chat_id={chat_id}&text=Your answer is:{eval(text)}')

# print(send_message('getUpdates'))

for i in range(100):
    time.sleep(5)
    response = send_request_with_method(f'getUpdates?offset={update_id}')
    print(response)
    results = response['result']
    for result in results:
        update_id = int(result['update_id']) + 1
        chat_id = result['message']['chat']['id']
        send_message(result['message']['text'],chat_id)

# for i in range(10):
#     send_request_with_method('sendMessage?chat_id=1470776266&text=Malik')


# import telebot
# import time

# TOKEN = '2057362453:AAF4KKW38cqBVK5YW2sdn76mAxAObTP9_kY'


# def listener(messages):
#     """
#     When new messages arrive TeleBot will call this function.
#     """
#     for m in messages:
#         chatid = m.chat.id
#         if m.content_type == 'text':
#             text = m.text
#             tb.send_message(chatid, text)


# tb = telebot.TeleBot(TOKEN)
# tb.set_update_listener(listener) #register listener
# tb.polling()
# #Use none_stop flag let polling will not stop when get new message occur error.
# tb.polling(none_stop=True)
# # Interval setup. Sleep 3 secs between request new message.
# tb.polling(interval=3)

# while True: # Don't let the main Thread end.
#     pass