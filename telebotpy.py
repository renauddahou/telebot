from Adafruit_IO import Client
from telegram.ext import Updater,MessageHandler,Filters
import os

feed_key = os.getenv('feed_key')

aio = Client('uvi', feed_key)  #for light

aio1 = Client('uvi', feed_key)  #for fan

light_on = ["turn on the light","turn on light","lights on","light on","its dark here","on the light"]
light_off = ["turn off the light","turn off light","lights off","light off"]
fan_on = ["turn on the fan","turn on fan","fan on","on the fan"]
fan_off = ["turn off the fan","turn off fan","fan off","off the fan"]


def ledon(bot,update):
  chat_id = bot.message.chat_id
  path='https://cdn3.vectorstock.com/i/1000x1000/52/87/abstract-lightbulb-vector-955287.jpg'
  bot.message.reply_text("Done,lights turned on!")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio.send('led', 1)
  
def ledoff(bot,update):
  chat_id = bot.message.chat_id
  path='https://png.pngtree.com/png-vector/20201114/ourlarge/pngtree-line-draw-vector-light-bulb-abstract-continuous-line-drawing-png-image_2425961.jpg'
  bot.message.reply_text("Done,lights turned off!")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio.send('led', 0)
  
def fanon(bot,update):
  chat_id = bot.message.chat_id
  #path='https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text("Done,fan turned on!")
  #update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio1.send('fan', 1)
  
def fanoff(bot,update):
  chat_id = bot.message.chat_id
  #path='https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text("Done,fan turned off!")
  #update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio1.send('fan', 0)

def main(bot,update):
  a = bot.message.text.lower()
  print(a)
  if a in light_on:
    ledon(bot,update)
  elif a in light_off:
    ledoff(bot,update)
  elif a in fan_on:
    fanon(bot,update)
  elif a in fan_off:
    fanoff(bot,update)

BOT_TOKEN = os.getenv('BOT_TOKEN')
up = Updater(BOT_TOKEN,use_context=True)
dp = up.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
up.start_polling()
up.idle()
