import os
import telebot
import openai

openai.key=os.environ.get("OPENAI_API_KEY")

bot_token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  bot.reply_to(message, "Hi, I how can I help you?")


@bot.message_handler(commands=['about', 'creater'])
def about(message):
  bot.reply_to(
    message,
    "Hello, I'm Om Jagatp, and I welcome you to my Python-driven bot. vist my webpage - https://jagtapom.netlify.app/ and blog page- https://omjagtap.onrender.com/"
  )


# @bot.message_handler(commands=['', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Hi, I how can I help you?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
  bot.reply_to(message, message.text)


bot.infinity_polling()
