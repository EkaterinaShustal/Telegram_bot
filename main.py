import telebot
from telebot import types

bot = telebot.TeleBot('5630936350:AAHtHSDs0esZS01ET6Xf4z_EFk1nCQilKYk')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://vk.com/k.gnedko'))
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    #id = types.KeyboardButton('/id')
    markup.add(website, start)
    #bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, '<b>И тебе привет!</b>', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'<b>Твой ID: {message.from_user.id}</b>', parse_mode='html')
    elif message.text == 'photo':
        photo = open('IMG_7452.jpg','rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, '<b>Я тебя не понимаю...</b>', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, '<b>Вау, крутое фото!</b>', parse_mode='html')


bot.polling(none_stop=True)