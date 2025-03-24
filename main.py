from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

API_key = 'YOUR_BOT_TOKEN'

bot = TeleBot(API_Key)

CHANNEL_USERNAME = 'unknow2025chat'# https://t.me/unknow2025chat

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

@bot.message_handler(commands=['start'])
def Welcome(message):
    global user_id
    user_id = message.from_user.id
    if is_member(user_id):
        bot.send_message(message.chat.id, "Welcome to my bot.")
    else:
        bot.send_message(message.chat.id, "Welcome to my bot.")
        bot.send_message(message.chat.id, "Please join the channel below", reply_markup=join_channel_markup())

@bot.callback_query_handler(lambda call:True)
def callback_query(call):
    if call.data == 'joined':
        member = bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        print(member.status)
        if member.status in ['member', 'administrator', 'creator']:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text='Thanks. You can use the bot now🎉', reply_markup=None)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text='Please join the channel', reply_markup=join_channel_markup())

bot.polling()
