from Adafruit_IO import Client
from telegram.ext import Updater,MessageHandler,Filters
import os

feed_key = os.getenv('feed_key')

aio = Client('uvi', feed_key)  #for light

aio1 = Client('uvi', feed_key)  #for fan

greeting = ["hi","hello","hey"]
tay = ["what can you do","what will you do","say about yourself"]
howlist = ["how are you"]
finelist = ["fine","great","good"]
light_on = ["turn on the light","turn on light","lights on","light on","its dark here","on the light"]
light_off = ["turn off the light","turn off light","lights off","light off"]
fan_on = ["turn on the fan","turn on fan","fan on","on the fan"]
fan_off = ["turn off the fan","turn off fan","fan off","off the fan"]


def ledon(bot,update):
  chat_id = bot.message.chat_id
  animation_url = 'https://media.baamboozle.com/uploads/images/68811/1618179100_34871_gif-url.gif'
  bot.message.reply_text("Done,lights turned on!✌")
  update.bot.sendAnimation(chat_id=chat_id,animation=animation_url,duration=2)
  aio.send('led', 1)
  
def ledoff(bot,update):
  chat_id = bot.message.chat_id
  path='https://labblog.uofmhealth.org/sites/lab/files/2018-11/michigan-med-l-ocd-study.gif'
  bot.message.reply_text("Done,lights turned off!👍")
  update.bot.sendAnimation(chat_id=chat_id,animation=path)
  aio.send('led', 0)
  
def fanon(bot,update):
  chat_id = bot.message.chat_id
  path='https://mir-s3-cdn-cf.behance.net/project_modules/disp/bafb3929035897.55decb26f207b.gif'
  bot.message.reply_text("Done,fan turned on!✌")
  update.bot.sendAnimation(chat_id=chat_id,animation=path)
  aio1.send('fan', 1)
  
def fanoff(bot,update):
  chat_id = bot.message.chat_id
  path='https://pbs.twimg.com/media/DKamHGZUQAIkX4J.jpg'
  bot.message.reply_text("Done,fan turned off!👍")
  update.bot.sendAnimation(chat_id=chat_id,animation=path)
  aio1.send('fan', 0)
  
def inval(bot,update):
  bot.message.reply_text("Invalid command!")

def greet(bot,update):
  bot.message.reply_text("👋Hi!")
  
def about(bot,update):
  bot.message.reply_text("I can turn on and off the light and fan for you")

def fine(bot,update):
  mes = random.choice(finelist)
  bot.message.reply_text(mes)

                         

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
  elif a in greeting:
    greet(bot,update)
  elif a in tay:
    about(bot,update)
  elif a in howlist:
    fine(bot,update)
  else:
    inval(bot,update)

BOT_TOKEN = os.getenv('BOT_TOKEN')
up = Updater(BOT_TOKEN,use_context=True)
dp = up.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
up.start_polling()
up.idle()
