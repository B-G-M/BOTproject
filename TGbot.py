import telebot

bot = telebot.TeleBot('1698737996:AAFXkYNDMop31dGGAnGrLl_cvjQllmZW3fQ')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Узнать прайс лист', 'Написать в тех.поддержку', 'Узнать о процессе буста', 'Узнать о бустерах', 'а', 'б', 'в', 'г', 'д', 'е')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет. Я бот по бусту в CS:GO', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, 'Привет, выбери один из пунктов ниже')
    elif message.text.lower() == 'Узнать прайс лист':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()