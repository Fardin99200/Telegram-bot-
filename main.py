import telebot

# Telegram bot token
TOKEN = "7563795311:AAF3JuIi6I-AXkRzSxnCTHzT-iPFGfz9nAM"
bot = telebot.TeleBot(TOKEN)

# Top 20 Indian stocks
stocks = ["TCS", "INFY", "RELIANCE", "HDFCBANK", "ICICIBANK", "SBIN", "AXISBANK", "KOTAKBANK", "ITC", "HINDUNILVR",
          "BAJFINANCE", "ASIANPAINT", "MARUTI", "LT", "NTPC", "SUNPHARMA", "ULTRACEMCO", "TITAN", "POWERGRID", "WIPRO"]

user_selected = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for stock in stocks:
        markup.add(stock)
    bot.send_message(chat_id, "Select a stock to get signals:", reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop_signal(message):
    chat_id = message.chat.id
    user_selected.pop(chat_id, None)
    bot.send_message(chat_id, "Stopped signals for selected stock.")

@bot.message_handler(func=lambda message: message.text in stocks)
def handle_stock_selection(message):
    chat_id = message.chat.id
    selected_stock = message.text
    user_selected[chat_id] = selected_stock
    bot.send_message(chat_id, f"Now tracking {selected_stock} for you. You'll receive signals here.")

# Placeholder: Logic for sending buy/sell signals will be added here

print("Bot is running...")
bot.polling()
