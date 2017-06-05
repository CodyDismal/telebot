#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import global_vars
import telebot
from constants import *
from user_operations import *
import os.path
from time import time, sleep
from random import *
from job import *
from global_messages import *
from threading import *
from games import *

bot = telebot.TeleBot(global_vars.private_key)
last_time = None


def recounting_all_needs(a, t):

    lt = a.last_action_time
    print ("This user was offline for {} seconds".format((t - lt)))
    #
    #   YOUR CAT WILL LEAVE YOU IF YOU WASN'T BEEING WITH HIM MORE THEN 10 HOURS! 
    #
    if (t - lt > 43200):
        return -1

    a.food -= 0.0 + (t - lt) * 0.006
    if (a.food < 0.0):
        a.food = 0.0
    a.water -= 0.0 + (t - lt) * 0.008
    if (a.water < 0.0):
        a.water = 0.0
    if (a.action == "At work"):
        a.money += (t - lt) / 60 * 0.25
    if (a.action == "Sleeping"):
        if (a.power < 100):
            a.power += 0.0 + (t - lt) * 0.1
    else:
        a.power -= 0.0 + (t - lt) * 0.004
    if (a.power >= 100.0):
        a.power = 100.0
    if (a.power < 0.0):
        a.power = 0.0
    a.fun -= 0.0 + (t - lt) * 0.04
    if (a.fun < 0.0):
        a.fun = 0.0
    return a

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    t = time()
    print (" --- {0} --- {1} --- ").format(t, message.date)
    chat_id = message.from_user.id
    if (message.text == "/start"):
        a = create_new_user(chat_id)

        a.set_la_time ( message.date )

        bot.send_message(chat_id, "Hey, welcome to TamaBot, your virtual cat ;)")
        bot.send_message(chat_id, "First of all, enter your cat's name.")
        
        a.action = "Select pet's name"
        
        save_user(a)

        return
    
    ################################################
    #     MAIN PART OF PROGRAM (ONE GIANT IF)      #
    ################################################
    a = load_user(chat_id)
    if (a == -1): return 
    cat_name = a.name
    
    a = recounting_all_needs(a, time())

    # YOUR CAT WILL LEAVE YOU IF YOU WASN'T BEEING WITH HIM MORE THEN 12 HOURS! 
    if (a == -1):
        sti = open('./Images/gone_away.webp', 'rb')
        bot.send_sticker(chat_id, sti, reply_markup=gameover_markup)
        bot.send_message(chat_id, "Your {0} was alone for so long (more then 12 hours!) and has decided to run away from you! Don't worry, he will be okey, but what about you?! Will new cat heal pain of loss?".format(cat_name))
        remove_user(chat_id)
        return 

    del cat_name
    a.set_la_time(time())
    save_user(a)
    chat_id = chat_id
    


    if (message.text == "Math game"):
        g = Math_game(a)
        bot.send_message(chat_id, g.get_req_string(), reply_markup=sleep_markup)
        save_mini_game(g, chat_id)
        return

    if (message.text == u"Find cat's job"):
        j = Job()
        a.action = "At work"
        bot.send_message(chat_id, "Your {0} is {1} today! You will get 0.25$ per minute.".format(a.name, j()))
        sti = open('./Images/working.webp', 'rb')
        bot.send_sticker(chat_id, sti, reply_markup=sleep_markup)
        save_user(a)
        del j
        return 
    else:
        if (a.action == "At work"):
            a.action = "Main menu"
            save_user(a)
    if (message.text == u'ℹ️'):
        bot.send_message(chat_id, "Information about {3}.\n🍗 {0}/100\n🥛 {1}/100\n💤 {2}/100\n💵   {4}".format(a.food,a.water,a.power, a.name, a.money ))
        return

    if (a.action == "Select pet's name"):
        a.action = "Main menu"  
        a.name = message.text
        bot.send_message(chat_id, "Done! So, now you can play with {0}".format(a.name))
        sti = open('./Images/siting.webp', 'rb')
        bot.send_sticker(chat_id, sti, reply_markup=main_menu_markup)
        save_user(a)
        return
    
    
        
    if (message.text == u"🍗"):
        if (a.money >= 1):
            a.food += 25.0
            if (a.food > 100.0): a.food = 100.0
            a.money -= 5
            sti = open('./Images/eating.webp', 'rb')
            bot.send_sticker(chat_id, sti, reply_markup=main_menu_markup)
            bot.send_message(chat_id, "Spent 5$. Your actual balance is {0}".format(a.money))
            save_user(a)
        else:
            bot.send_message(chat_id, "You don't have enough money, you can earn he by showing tricks or try to find he at the city park.")
        return

    if (message.text == u"🥛"):
        
        if (a.money >= 1):
            a.water += 25
            if (a.water > 100.0): a.water = 100.0
            a.money -= 1
            sti = open('./Images/drinking.webp', 'rb')
            bot.send_sticker(chat_id, sti, reply_markup=main_menu_markup)
            bot.send_message(chat_id, "Spent 1$. Your actual balance is {0}".format(a.money))
            save_user(a)
        else: 
            bot.send_message(chat_id, "You don't have enough money, you can earn he by showing tricks or try to find he at the city park.")
        return

    if (message.text == u"💤"):
        sti = open('./Images/sleeping.webp', 'rb')
        bot.send_sticker(chat_id, sti, reply_markup=sleep_markup)
        bot.send_message(chat_id, "{0} is sleeping now. Be quiet. He restores 0.1 energy point every minute.".format(a.name))
        a.action = "Sleeping"
        save_user(a)
        return
    else: 
        if (a.action == "Sleeping"):
            a.action = "Main menu"
            save_user(a)
    

    if (message.text == u"💵"):
        bot.send_message(chat_id, "Your actual balance is ${0}".format(a.money), reply_markup=money_markup)
        return 
    
    if (message.text == u'🎮'):
        sti = open('./Images/wanna_play.webp', 'rb')
        bot.send_sticker(chat_id, sti)
        bot.send_message(chat_id, "Select game...", reply_markup=games_markup)
        return



    


    if (message.text == u'⛔️'):
        a.action = "Main menu"
        if (a.action == "At work"):
            bot.send_message(chat_id, "End of work day! Your balance is {0}$!".format(a.money))
        if (a.action == "Game"):
            sti = open('./Images/after_game.webp', 'rb')
            bot.send_sticker(chat_id, sti, reply_markup=main_menu_markup)
            return
    
    
    if (a.action == "Game"):
        g = load_mini_game(a.id)
        if (g.is_correct(message.text)):
            bot.send_message(chat_id, "Correct!")
        else:
            bot.send_message(chat_id, "Not correct!")
        g = Math_game(a)
        bot.send_message(chat_id, g.get_req_string(), reply_markup=sleep_markup)
        save_mini_game(g, chat_id)
        return

        
    if (message.text == u'❤️'):
        sti = open('./Images/very_loving.webp', 'rb')
        bot.send_sticker(chat_id, sti, reply_markup=main_menu_markup)
        return 

    sti = open('./Images/siting.webp', 'rb')
    bot.send_sticker(chat_id, sti, reply_markup=main_menu_markup)

    if (randrange(0,10) == 0):
        send_message_to_random_user(bot, "love")


    del a

    

def auto_count(interval):
    while True:
        g_b = Global_message()
        print g_b.get_list()
        for i in g_b.get_list():
            a = load_user(i)

            if (a == -1): return 
            cat_name = a.name
            
            a = recounting_all_needs(a, time())

            # YOUR CAT WILL LEAVE YOU IF YOU WASN'T BEEING WITH HIM MORE THEN 12 HOURS! 
            if (a == -1):
                sti = open('./Images/gone_away.webp', 'rb')
                bot.send_sticker(i, sti, reply_markup=gameover_markup)
                bot.send_message(i, "Your {0} was alone for so long (more then 12 hours!) and has decided to run away from you! Don't worry, he will be okey, but what about you?! Will new cat heal pain of loss?".format(cat_name))
                remove_user(i)
                return 

            del cat_name
            a.set_la_time(time())
            
            chat_id = i
            print "Auto_count for id={}".format(i)
                
            if ((a.power <= 45.0) and (a.last_action != "sleep")):
                sti = open('./Images/want_to_sleep.webp', 'rb')
                bot.send_sticker(chat_id, sti)
                bot.send_message(chat_id, u"Oh, it's look like {} want to eat. Feed him ❤️".format(a.name))
                a.last_action = "sleep"

            if ((a.food <= 45.0) and (a.last_action != "food")):
                sti = open('./Images/want_to_eat.webp', 'rb')
                bot.send_sticker(chat_id, sti)
                bot.send_message(chat_id, u"Oh, it's look like {} want to eat. Feed him ❤️".format(a.name))
                a.last_action = "food"

            if ((a.water <= 60.0) and (a.last_action != "water")):
                sti = open('./Images/want_to_drink.webp', 'rb')
                bot.send_sticker(chat_id, sti)
                bot.send_message(chat_id, u"Oh, it's look like {} want to drink. Give him plate of milk ❤️".format(a.name))
                a.last_action = "water"

            if ((a.power == 100.0) and (a.last_action != "power")):
                sti = open('./Images/waked_up.webp', 'rb')
                bot.send_sticker(chat_id, sti)
                bot.send_message(chat_id, u"{} waked up! Pay him some attention ❤️".format(a.name), reply_markup=love_markup)
                a.last_action = "power"

            if ((a.power >= 90.0) and (a.food >= 90.0) and (a.water >= 90.0) and (a.last_action != "love")):
                sti = open('./Images/very_loving.webp', 'rb')
                bot.send_sticker(chat_id, sti)
                a.last_action = "love"

            save_user(a)
        del g_b
        del a
        del chat_id
        sleep(interval)

t = Thread(target=auto_count, args=(600,))
t.daemon = True
t.start()

bot.polling()


