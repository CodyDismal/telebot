# MESSAGE DEFREEZER
#
# If bot returns some strange errors and stacks on some kind of messages,
# you can run "python defreeze.py" to let it "eat" broken messages and 
# let your bot works normally.
#

import telebot
import global_vars
bot = telebot.TeleBot(global_vars.private_key)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print ("Message defreezed\n")
bot.polling()