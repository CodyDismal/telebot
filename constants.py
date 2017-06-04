#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from telebot import types

token = "373564934:AAEwA-Uv38sH8BxNNgtLPMGDTTa273l9l1Q"

main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
itembtn1 = types.KeyboardButton('🍗')
itembtn2 = types.KeyboardButton('🥛')
itembtn3 = types.KeyboardButton('🎮')
itembtn4 = types.KeyboardButton('ℹ️')
itembtn5 = types.KeyboardButton('💤')
itembtn6 = types.KeyboardButton('💵')
main_menu_markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

sleep_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtn1 = types.KeyboardButton('⛔️')
sleep_markup.add(itembtn1)

games_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
itembtn1 = types.KeyboardButton('Casino')
itembtn2 = types.KeyboardButton('2 ? 3')
cancel = types.KeyboardButton("⛔️")
games_markup.add(itembtn1, itembtn2, cancel)


money_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtn1 = types.KeyboardButton("Find cat's job")
itembtn3 = types.KeyboardButton("⛔️")
money_markup.add(itembtn1, itembtn3)

job_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtn1 = types.KeyboardButton('⛔️')
job_markup.add(itembtn1)

love_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtn1 = types.KeyboardButton('❤️')
love_markup.add(itembtn1)

gameover_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtn1 = types.KeyboardButton('/start')
gameover_markup.add(itembtn1)

