import telebot

bot = telebot.TeleBot("373564934:AAEwA-Uv38sH8BxNNgtLPMGDTTa273l9l1Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print ("----\n"+str(message))
    if (message.text == "FEED ME"):
        bot.send_message(message.from_user.id, "GIVE ME PUSSY BOSS")
    bot.reply_to(message, message.text)

bot.polling()
