from cgitb import text
from datetime import datetime
import string
from xmlrpc.client import NOT_WELLFORMED_ERROR
import telebot
import random
from gtts import gTTS
import qrcode
import datetime



bot = telebot.TeleBot("5102593802:AAGWwFnerqhwmarycs5dAgJ6Smf0Qqx53lg")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message , message.from_user.first_name+"به بات من خوش اومدی")





@bot.message_handler(commands=['game'])
def start_message(message):
  game = random.randint(70,210)
  mess = bot.send_message(message.chat.id,"به بازی حدس عدد خوش آمدید، بین اعداد 70 تا 210 عدد وارد کنید")
  
  @bot.message_handler(func= lambda m: True)
  def guess(message):
    username = int(message.text)
    if game == username:
      bot.reply_to(message,'تبریک برنده شدید، عدد را درست حدس زدید')
    elif username < game:
      bot.reply_to(message,'عدد را بالاتر وارد کنید')
    elif username > game:
      bot.reply_to(message,'عدد را پایین تر وارد کنید')



@bot.message_handler(commands=['voice'])
def text_to_voice(message):
    sentence = bot.send_message(message.chat.id, "متن را به انگلیسی وارد کنیدتا متن را به صدا برایتان بفرستم")
    bot.register_next_step_handler(sentence, convertor)

def convertor(message):
        myobj = gTTS(text = message.text, slow=False)
        myobj.save('file.mp3')
        voice = open('file.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)



@bot.message_handler(commands=['max'])
def findmax(message):
    arr = bot.send_message(message.chat.id, " مثل اعداد روبه رو اعداد وارد کنید : 105,45,80,110,75,51 تا بزرگترین عدد رو بهتون نمایش بدم")
    bot.register_next_step_handler(arr, maxfunc)

def maxfunc(userarray):
        array = userarray.text.split(",")
        arraynum = []
        for i in range(len(array)):
            arraynum.append(int(array[i]))
        MAX = max(arraynum)
        bot.send_message(userarray.chat.id,MAX)



@bot.message_handler(commands=['argmax'])
def findmax(message):
    arr2 = bot.send_message(message.chat.id, "مثل اعداد روبه رو اعداد وارد کنید :  105,45,80,110,75,51 تا اندیس بزرگترین عدد رو بهتون نمایش بدم")
    bot.register_next_step_handler(arr2, maxfunc2)

def maxfunc2(userarray):
        array = userarray.text.split(",")
        arraynum = []
        for i in range(len(array)):
            arraynum.append(int(array[i]))
        MAX = max(arraynum)
        index_max = 0
        for i in range(len(arraynum)):
            if MAX == arraynum[i]:
                indexmax = i
        bot.send_message(userarray.chat.id,indexmax)



@bot.message_handler(commands=['qrcode'])
def get_qrcode(message):
    qr_code = bot.send_message(message.chat.id, 'متنی وارد کنید تا کیو آر کد آن را برای شما ارسال کنم')
    bot.register_next_step_handler(qr_code, creat_qr)

def creat_qr(message):
        qrcode_image = qrcode.make(message.text)
        qrcode_image.save('qrcode.png')
        photo = open('qrcode.png', 'rb')
        bot.send_photo(message.chat.id, photo)



bot.infinity_polling()
