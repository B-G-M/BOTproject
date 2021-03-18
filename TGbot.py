import telebot

bot = telebot.TeleBot('1698737996:AAFXkYNDMop31dGGAnGrLl_cvjQllmZW3fQ')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Узнать прайс лист', 'Написать в тех.поддержку', 'Сделать заказ', 'Узнать о процессе буста')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет. Я бот по бусту в CS:GO', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, 'Привет, выбери один из пунктов ниже')
    elif message.text.lower() == 'Узнать прайс лист':
        bot.send_message(message.chat.id, '''1.
        2.
        3.
        4.
        5.''')
    elif message.text.lower() == 'Написать в тех.поддержку':
        bot.send_message(message.chat.id, '@azazaatata')
    elif message.text.lower() == 'Сделать заказ':
        bot.send_message(message.chat.id, 'Выберети категорию')
    elif message.text.lower() == 'Узнать о процессе буста':
        bot.send_message(message.chat.id, '')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()