import time
import telebot
from telebot import types
from get_data import get_data1
from get_data import get_data2

bot_token = 'YOUR TOKEN'
bot = telebot.TeleBot(bot_token)


class UserState:
    def __init__(self):
        self.show_only_shirts = None
        self.use_sorting = 0
        self.gender = None
        self.max_price = None
        self.min_discount = None
        self.step = 0
        self.page_count = 0


user_states = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item11 = types.KeyboardButton("Покажи товары")
    markup1.add(item11)
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Мужчины", callback_data='men')
    item2 = types.InlineKeyboardButton("Женщины", callback_data='women')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Для кого ищем товары?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    if message.chat.type == 'private':
        if user_id in user_states:
            state = user_states[user_id]
            if state.step == 1:
                state.gender = message.text.lower()
                state.step += 1
                bot.send_message(message.chat.id, 'Показывать:')
            elif state.step == 2:
                state.step += 1
                bot.send_message(message.chat.id, 'Сортировать по: ')
            elif state.step == 3:
                state.step += 1
                bot.send_message(message.chat.id, 'Минимальную скидка (%):')
            elif state.step == 4:
                state.min_discount = int(message.text)
                state.step += 1
                bot.send_message(message.chat.id, 'Количество страниц:')
            elif state.step == 5:
                state.page_count = int(message.text)
                state.step += 1
                bot.send_message(message.chat.id, 'Максимальная цена:')
            elif state.step == 6:
                state.step = 0
                state.max_price = int(message.text)
                process_user_query(user_id)


def process_user_query(user_id):
    state = user_states[user_id]
    a1, a2, a3, a4, a5 = get_data1(state.show_only_shirts, state.use_sorting, state.gender, state.max_price,
                                   state.page_count)
    for i in range(len(a1)):
        b1, b2, b3, b4, b5 = get_data2(i, state.min_discount, a1, a2, a3, a4, a5)
        if all(p != '' for p in [b1, b2, b3, b4, b5]):
            bot.send_message(user_id, b1 + 'Было: ' + str(b3) + '\nСтало: ' +
                             str(b4) + '\nСкидка: ' + str(b5) + '%')
            bot.send_message(user_id, b2)
            time.sleep(2)
    bot.send_message(user_id, 'Конец')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    def call1():
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Только футболки", callback_data='shirts')
        item2 = types.InlineKeyboardButton("Только толстовки", callback_data='hoodies')
        item3 = types.InlineKeyboardButton("Показывать все", callback_data='all')
        markup.add(item1, item2, item3)
        bot.send_message(call.message.chat.id, 'Показывать: ', reply_markup=markup)
        state.step = 2

    def call2():
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Возрастанию цены", callback_data='option1')
        item2 = types.InlineKeyboardButton("Топу рейтинга", callback_data='option2')
        item3 = types.InlineKeyboardButton("Рекомендации", callback_data='option3')
        item4 = types.InlineKeyboardButton("Самое новое", callback_data='option4')
        markup.add(item1, item2, item3, item4)
        bot.send_message(call.message.chat.id, 'Использовать сортировку по:', reply_markup=markup)
        state.step = 3

    def call3():
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите минимальную скидку (%):')
        state.step = 4

    user_id = call.from_user.id
    state = user_states.setdefault(user_id, UserState())
    if call.message:
        if call.data == 'men':
            state.gender = 'мужчины'
            call1()
        elif call.data == 'women':
            state.gender = 'женщины'
            call1()
        elif call.data == 'shirts':
            state.show_only_shirts = '1980&'
            call2()
        elif call.data == 'hoodies':
            state.show_only_shirts = '1974&'
            call2()
        elif call.data == 'all':
            state.show_only_shirts = ''
            call2()
        elif call.data == 'option1':
            state.use_sorting = 10
            call3()
        elif call.data == 'option2':
            state.use_sorting = 7
            call3()
        elif call.data == 'option3':
            state.use_sorting = 0
            call3()
        elif call.data == 'option4':
            state.use_sorting = 9
            call3()


bot.polling(none_stop=True)
