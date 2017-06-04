#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import global_vars
from global_messages import *
import telebot
from Tkinter import *


g_m = Global_message()
root = Tk()
root.title("Send message to all users")

f = Frame(root, width=300,height=200)

e = Entry(f)
e.grid(column=0, row=1)
def message_action():
    global g_m
    text = e.get()
    if (g_m.send(bot, text)):
        print "Message sent"
    else: 
        print "Error while sending"


b = Button(f, text="SEND", command=message_action).grid(column=1, row=1)
l = Label(f, text="Enter your message and click Send").grid(column=0, row=0, columnspan=2)





bot = telebot.TeleBot(global_vars.private_key)
f.pack()
root.mainloop()
#root.destroy()