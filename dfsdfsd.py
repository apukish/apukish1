import telebot
import config
import random
import os
from os import listdir
from os.path import isfile, join
from telebot import types

url = "https://api.telegram.org/bot1087809691:AAF0b8B9Sy_wEU5vwbM8C6rKC5GcXsfVCuw/"

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')

    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("На твой выбор, брат")
    item3 = types.KeyboardButton("Рецепт дня")
    item4 = types.KeyboardButton("Каталог")

    markup.add(item1 , item3, item4)

    markup2 = types.InlineKeyboardMarkup(row_width=2)
    item11 = types.InlineKeyboardButton("Братан", callback_data='good')
    item22 = types.InlineKeyboardButton("Подружаня", callback_data='bad')
    markup2.add(item11, item22)

    bot.send_message(message.chat.id,
                     "Добрейший вечерочек, {0.first_name}!\nЯ - <b>{1.first_name}</b>, созданный чтоб помочь пацанам.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

    bot.send_message(message.chat.id,
                     "{0.first_name}, Как мне к тебе обращаться?".format(message.from_user, bot.get_me()),
                     reply_markup=markup2)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Красава, тогда стартуем-пиздуем 🚀')
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id,
                             'Паблик вообще-то пацанский, но все же я тебе помогу...\n\n\n\nтолько не говори пацанам😉',
                             parse_mode='html')
        elif call.data == 'types':
            markup4 = types.InlineKeyboardMarkup(row_width=1)
            item121 = types.InlineKeyboardButton("Жарим", callback_data='zharim')
            item122 = types.InlineKeyboardButton("Варим", callback_data='varim')
            item123 = types.InlineKeyboardButton("В микроволновке", callback_data='microwave')
            item124 = types.InlineKeyboardButton("Просто смешать и сожрать", callback_data='simple eat')
            markup4.add(item121, item122, item123, item124)
            bot.send_message(call.message.chat.id, "?", reply_markup=markup4)
        elif call.data == 'ingredients':
            markup5 = types.InlineKeyboardMarkup(row_width=1)
            item131 = types.InlineKeyboardButton("Дошик", callback_data='doshik')
            item132 = types.InlineKeyboardButton("Мазик", callback_data='mazik')
            item133 = types.InlineKeyboardButton("Пельмени", callback_data='pelmeni')
            item134 = types.InlineKeyboardButton("Кетчуп", callback_data='ketchup')
            markup5.add(item131, item132, item133, item134)
            bot.send_message(call.message.chat.id, "?", reply_markup=markup5)
        elif call.data == 'zharim':
            sti = open('2.jpg', 'rb')
            bot.send_photo(call.message.chat.id, sti)
        elif call.data == 'varim':
            sti = open('1.jpg', 'rb')
            bot.send_photo(call.message.chat.id, sti)
        elif call.data == 'microwave':
            sti = open('3.jpg', 'rb')
            bot.send_photo(call.message.chat.id, sti)
        elif call.data == 'simple eat':
            sti = open('1.jpg', 'rb')
            bot.send_photo(call.message.chat.id, sti)
        elif call.data == 'doshik':
            DIR = 'doshik'
            files = os.listdir(DIR)
            y = 0
            for y in range(len(files)):
                sti = open(os.path.join(DIR, files[y]), 'rb')
                bot.send_photo(call.message.chat.id, sti)
                y + 1
        elif call.data == 'mazik':
            DIR = 'mazik'
            files = os.listdir(DIR)
            y = 0
            for y in range(len(files)):
                sti = open(os.path.join(DIR, files[y]), 'rb')
                bot.send_photo(call.message.chat.id, sti)
                y + 1
        elif call.data == 'pelmeni':
            DIR = 'pelmeni'
            files = os.listdir(DIR)
            y = 0
            for y in range(len(files)):
                sti = open(os.path.join(DIR, files[y]), 'rb')
                bot.send_photo(call.message.chat.id, sti)
                y + 1
        elif call.data == 'ketchup':
            DIR = 'ketchup'
            files = os.listdir(DIR)
            y = 0
            for y in range(len(files)):
                sti = open(os.path.join(DIR, files[y]), 'rb')
                bot.send_photo(call.message.chat.id, sti)
                y + 1
        # все ответы на инлайновые сообщения прописывать однорангово в этом условии!!!!!
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.message_handler(content_types=['text', 'sticker', 'photo'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'На твой выбор, брат':
            DIR = 'Kartinki'
            sti = open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
            bot.send_photo(message.chat.id, sti)
        elif message.text == 'Подобрать':
            bot.send_message(message.chat.id, 'Спасибо, брат')
        elif message.text == 'Рецепт дня':
            sti = open('2.jpg', 'rb')
            bot.send_photo(message.chat.id, sti)
        elif message.text == 'Каталог':
            markup3 = types.InlineKeyboardMarkup(row_width=1)
            item111 = types.InlineKeyboardButton("По типу готовки", callback_data='types')
            item112 = types.InlineKeyboardButton("По продуктам", callback_data='ingredients')
            markup3.add(item111, item112)
            bot.send_message(message.chat.id, "Как выбирать будем?", reply_markup=markup3)


        else:
            bot.send_message(message.chat.id, 'Не, ну ты определись че надо?')


bot.polling(none_stop=True)
