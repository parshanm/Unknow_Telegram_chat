from telebot import TeleBot
from config import API_Token
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from db import Data

bot = TeleBot(API_Token)

db = Data()

db.add_table()

CHANNEL_USERNAME = 'unknow2025chat'# https://t.me/unknow2025chat

def canncel_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    canncel = KeyboardButton('cancel❎')
    markup.add(canncel)
    return markup

def is_member(user_id):
    try:
        member = bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

def join_channel_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="Join Channel", url=f'https://t.me/{CHANNEL_USERNAME}')
    check_btn = InlineKeyboardButton(text='joined✔', callback_data='joined')
    markup.add(button, check_btn)
    return markup

def profile_create_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    button_change = InlineKeyboardButton(text='create profile📰', callback_data='create prof')
    markup.add(button_change)
    return markup

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    chat_btn = KeyboardButton('chat with someone unknow')
    profile_btn = KeyboardButton('Your Profile')
    markup.add(chat_btn, profile_btn)
    return markup

def create_profile(message):
    bot.send_message(message.chat.id, 'please enter your name.')
    bot.register_next_step_handler(message, name_handel)

def name_handel(message):
    name = message.text
    bot.send_message(message.chat.id, 'Please enter your gender (you can choose between male, female or don\'t say)')
    bot.register_next_step_handler(message, gender_handel, name=name)

def gender_handel(message, name):
    gender = message.text
    bot.send_message(message.chat.id, 'Please enter your age')
    bot.register_next_step_handler(message, age_handel, name=name, gender=gender)

def age_handel(message, name, gender):
    try:
        age = int(message.text)
        bot.send_message(message.chat.id, 'Please enter your age')
        db.update_user(user_id, {'first_name':name, 'gender':gender, 'age':age})
    except ValueError:
        bot.send_message(message.chat.id, 'please enter a number for age')
        bot.send_message(message.chat.id, 'Please enter your age')
        bot.register_next_step_handler(message, age_handel, name=name, gender=gender)


@bot.message_handler(commands=['start'])
def Welcome(message):
    global user_id
    user_id = message.from_user.id
    if is_member(user_id):
        bot.send_message(message.chat.id, "Welcome to my bot.", reply_markup=main_menu())
    else:
        bot.send_message(message.chat.id, "Welcome to my bot.")
        bot.send_message(message.chat.id, "Please join the channel below", reply_markup=join_channel_markup())
    print(db.check_user(user_id))
    if db.check_user(user_id=user_id):
        pass
    else:
        db.add_user(info={'user_id':user_id,
                           'chat_id':message.chat.id,
                           'first_name':'dont',
                           'gender':'dont', 
                           'age':0})

@bot.message_handler(func=lambda message:message.text == 'Your Profile')
def profile(message):
    global prof_message
    prof_message = message
    bot.reply_to(message, 'Your profile👇')
    dat = db.get_info(user_id)
    print(dat['first_name'])
    if dat['first_name'] != '':
        prof = f'name: {dat[2]}\n gender:{dat[3]}\n age:{str(dat[4])}'
        bot.send_message(message.chat.id, prof)
    else:
        bot.send_message(message.chat.id, 'You have not filled your profile yet', reply_markup=profile_create_markup())

@bot.message_handler(func=lambda message:message.text == 'cancel❎')
def cancel(message):
    bot.send_message(message.chat.id, 'cancelled')
    bot.send_message(message.chat.id, 'You backed to the main menu', reply_markup=main_menu())

@bot.callback_query_handler(lambda call:True)
def callback_query(call):
    if call.data == 'joined':
        member = bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        print(member.status)
        if member.status in ['member', 'administrator', 'creator']:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text='Thanks. You can use the bot now🎉', reply_markup=None)
            bot.send_message(call.message.chat.id, "Welcome to my bot.", reply_markup=main_menu())
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text='Please join the channel', reply_markup=join_channel_markup())
    if call.data == 'create prof':
        create_profile(prof_message)

bot.polling()
