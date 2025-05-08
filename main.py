import random
import telebot
from telebot import types
import csv
game_places = []
game_jobs = []
game_countries = []
with open('words.csv', newline='') as csvfile:
    worddss = csv.reader(csvfile, quotechar='|')
    for row in worddss:
        game_places.append(row[0])
        game_jobs.append(row[1])
        game_countries.append(row[2])

API_TOKEN = '7734843388:AAEhAKJYNeWkbUgr-98hlI0ZRlKgvz9EzyA'
bot = telebot.TeleBot(API_TOKEN)


user_data = {}
random_player = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Places")
    btn2 = types.KeyboardButton("Jobs")
    btn3 = types.KeyboardButton("Countries")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Welcome to the game, Select the theme", reply_markup=markup)







@bot.message_handler(func=lambda m: m.text == "Places")
def ask_players(message):
    bot.send_message(message.chat.id, "How many players are playing? Enter a number between 4 and 10.")
    bot.register_next_step_handler(message, handle_player_count_places)

def handle_player_count_places(message):
    try:
        count = int(message.text)
        if 4 <= count <= 10:
            random_word = game_places[random.randint(1,54)]
            random_special_index = random.randint(0, count - 2)
            user_data[message.chat.id] = {
                "count": count * 2 + 1,
                "presses": 0,
                "special_index": random_special_index,
                "game_word": random_word
            }
            send_word_message_places(message.chat.id, "Waiting")
        else:
            bot.send_message(message.chat.id, "Please enter a number between 4 and 10.")
    except ValueError:
        bot.send_message(message.chat.id, "That's not a number. Please enter a number between 4 and 10.")

def send_word_message_places(chat_id, word):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Next", callback_data="next_word")
    markup.add(btn)
    bot.send_message(chat_id, word, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "next_word")
def update_word(call):
    data = user_data.get(call.message.chat.id)
    if data and data["presses"] < data["count"]:
        data["presses"] += 1

        if data["presses"] == data["count"]:
            word = "Game is going"
        elif data["presses"] % 2 == 0:
            word = "Waiting"
        elif data["presses"] - 1 == data["special_index"]*2:
            word = "You are SPY"
        else:
            word = data["game_word"]

        try:
            if word == "Game is going":
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=word)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=word,
                                      reply_markup=call.message.reply_markup)
        except Exception as e:
            print(f"Error editing message: {e}")
    else:
        bot.answer_callback_query(call.id, "No more presses allowed.")










@bot.message_handler(func=lambda m: m.text == "Countries")
def ask_players(message):
    bot.send_message(message.chat.id, "How many players are playing? Enter a number between 4 and 10.")
    bot.register_next_step_handler(message, handle_player_count_countries)

def handle_player_count_countries(message):
    try:
        count = int(message.text)
        if 4 <= count <= 10:
            random_word = game_countries[random.randint(1,54)]
            random_special_index = random.randint(0, count - 2)
            user_data[message.chat.id] = {
                "count": count * 2 + 1,
                "presses": 0,
                "special_index": random_special_index,
                "game_word": random_word
            }
            send_word_message_countries(message.chat.id, "Waiting")
        else:
            bot.send_message(message.chat.id, "Please enter a number between 4 and 10.")
    except ValueError:
        bot.send_message(message.chat.id, "That's not a number. Please enter a number between 4 and 10.")

def send_word_message_countries(chat_id, word):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Next", callback_data="next_word")
    markup.add(btn)
    bot.send_message(chat_id, word, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "next_word")
def update_word(call):
    data = user_data.get(call.message.chat.id)
    if data and data["presses"] < data["count"]:
        data["presses"] += 1

        if data["presses"] == data["count"]:
            word = "Game is going"
        elif data["presses"] % 2 == 0:
            word = "Waiting"
        elif data["presses"] - 1 == data["special_index"]*2:
            word = "You are SPY"
        else:
            word = data["game_word"]

        try:
            if word == "Game is going":
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=word)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=word,
                                      reply_markup=call.message.reply_markup)
        except Exception as e:
            print(f"Error editing message: {e}")
    else:
        bot.answer_callback_query(call.id, "No more presses allowed.")











@bot.message_handler(func=lambda m: m.text == "Jobs")
def ask_players(message):
    bot.send_message(message.chat.id, "How many players are playing? Enter a number between 4 and 10.")
    bot.register_next_step_handler(message, handle_player_count_jobs)

def handle_player_count_jobs(message):
    try:
        count = int(message.text)
        if 4 <= count <= 10:
            random_word = game_jobs[random.randint(1,54)]
            random_special_index = random.randint(0, count - 2)
            user_data[message.chat.id] = {
                "count": count * 2 + 1,
                "presses": 0,
                "special_index": random_special_index,
                "game_word": random_word
            }
            send_word_message_jobs(message.chat.id, "Waiting")
        else:
            bot.send_message(message.chat.id, "Please enter a number between 4 and 10.")
    except ValueError:
        bot.send_message(message.chat.id, "That's not a number. Please enter a number between 4 and 10.")

def send_word_message_jobs(chat_id, word):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Next", callback_data="next_word")
    markup.add(btn)
    bot.send_message(chat_id, word, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "next_word")
def update_word(call):
    data = user_data.get(call.message.chat.id)
    if data and data["presses"] < data["count"]:
        data["presses"] += 1

        if data["presses"] == data["count"]:
            word = "Game is going"
        elif data["presses"] % 2 == 0:
            word = "Waiting"
        elif data["presses"] - 1 == data["special_index"]*2:
            word = "You are SPY"
        else:
            word = data["game_word"]

        try:
            if word == "Game is going":
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=word)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=word,
                                      reply_markup=call.message.reply_markup)
        except Exception as e:
            print(f"Error editing message: {e}")
    else:
        bot.answer_callback_query(call.id, "No more presses allowed.")

bot.infinity_polling()




