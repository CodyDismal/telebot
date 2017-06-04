#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
from user_operations import *
from constants import love_markup
from random import randrange

class Global_message:
    def __init__(self):
        self._users = []
        ids = os.listdir("./saves")
        for i in ids:
            self._users.append(os.path.splitext(i)[0])
    
    def get_list(self):
        return self._users

    def get_random_user_id(self):
        return self._users[randrange(0, len(self._users))]

    def send_to_random(self, bot, text):
        bot.send_message(self._users[randrange(0, len(self._users))], text)

    def send(self, bot, text):
        for i in self._users:
            bot.send_message(i, text)
        return 1


def send_message_to_random_user(bot, type):
    g_m = Global_message()
    chat_id = g_m.get_random_user_id()
    del g_m
    a = load_user(chat_id)
    if (type == "love"):
        sti = open('./Images/love.webp', 'rb')
        bot.send_message(chat_id, u"Your {0} loves you!!!😻 Do you love it back?".format(a.name))
        bot.send_sticker(chat_id, sti, reply_markup=love_markup)
    
