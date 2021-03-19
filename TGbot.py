import telebot

bot = telebot.TeleBot('1698737996:AAFXkYNDMop31dGGAnGrLl_cvjQllmZW3fQ')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.add('Узнать прайс лист', 'Написать в тех.поддержку', 'Сделать заказ', 'FAQ')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.add('Кто бустит', 'После оплаты', 'Могу я получить бан', 'Обратно')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.add('ММ', 'FACEIT', 'Обратно')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот BoostCsGo.\nЗдесь вы можете заказать буст\nА так же узнать цены на услуги', reply_markup=keyboard1)
    


@bot.message_handler(content_types=['text'])
def first_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'Узнать прайс лист':
        bot.send_message(message.from_user.id, 'Вся оплата идет за один ранг в тире\n\nПри переходе в следующий тир +100 рублей к предыдущему тиру\n')
        bot.send_message(message.from_user.id, 'ММ:\nТир Сильвер - 85 рублей\nТир Звезда - 180 рублей\nТир Магистр-Хранитель - 330 рублей\nТир Беркут - 450 рублей\nТир Элита - 1000 рублей')
        bot.send_message(message.from_user.id, 'FACEIT:\nТир Новичок (1-3lvl) - 100 руб\nТир Опытный (4-7lvl) - 450 руб\nТир Мастер (8-10lvl) - 1000 руб\n')

    elif message.text == 'Написать в тех.поддержку':
        bot.send_message(message.from_user.id, '@hbfbfckk')

    elif message.text == 'Сделать заказ':
        bot.send_message(message.from_user.id, 'Выберети категорию', reply_markup=keyboard3)
        bot.register_next_step_handler(send, second_message)

    elif message.text == 'FAQ':
        bot.send_message(message.from_user.id, 'Выберите что вам интересно', reply_markup=keyboard2)
        second_message(message)

    elif message.text == 'Обратно':
        bot.send_message(message.from_user.id, 'Выберите категорию')


@bot.message_handler(content_types=['text'])    
def second_message(message):
    if message.text == 'Обратно':
        bot.send_message(message.from_user.id, 'Возвращение обратно.', reply_markup=keyboard1)
        first_message(message)

    elif message.text == 'ММ':
        bot.send_message(message.from_user.id, 'Напишите нашему менеджеру и он оформит ваш заказ\n@bgm99')

    elif message.text == 'FACEIT':
        bot.send_message(message.from_user.id, 'Напишите нашему менеджеру и он оформит ваш заказ\n@evreyskiyjid')

    elif message.text == 'Кто бустит':
        bot.send_message(message.from_user.id, 'Все бустера сервиса работают по контракту и имеют не просто ранг Глобал Элит, но и высокий рейтинг faceit, что гарантирует качественный и быстрый буст')

    elif message.text == 'После оплаты':
        bot.send_message(message.from_user.id, 'После оплаты заказа нашим менеджерам, вы передаете им аккаунт, и они передадут ваш заказ бустерам')

    elif message.text == 'Могу я получить бан':
        bot.send_message(message.from_user.id, 'Вы не можете получить блокировку за буст, это процедура 100% безопасна. мы не используем читы для поднятия рейтинга или фиктивные игры (Вертиго буст, за который можно получить бан) все игры проходят с реальными игроками')

    
bot.polling()
