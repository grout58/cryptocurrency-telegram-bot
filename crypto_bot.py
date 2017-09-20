import telebot
import urllib.request
import json
import threading

bot = telebot.TeleBot("190646199:AAH27kykgbSYcmxfDkXfADDMkzi5FHXk0Lc")

user = bot.get_me()

@bot.message_handler(commands=['help'])
def print_help(message):
	bot.reply_to(message, """
	To get the current price of any cryptocurrency type
	in: /<abbreviation>
	IE /btc
	IE /eth
	You can also receive prices in other currency by entering
	the desired currency abbreviation after the currency
	you're looking for:
	IE "/btc eur" will give you the price of Bitcoin to Euros.
"""
)


@bot.message_handler(func=lambda m: True)
def all_price(message):
	try:
		crypto_abbrev = message.text.replace("/", "").upper()
		crypto_abbrev_list = crypto_abbrev.split()
		if len(crypto_abbrev_list) == 1:
			crypto_abbrev_list.append('USD')
			with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(crypto_abbrev_list[0],crypto_abbrev_list[1])) as url:
				data = json.loads(url.read().decode())
				for currency, price in data.items():
					bot.reply_to(message, "The price of {} is currently {} {}".format(crypto_abbrev_list[0],price, currency))
		else:
			with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(crypto_abbrev_list[0],crypto_abbrev_list[1])) as url:
				data = json.loads(url.read().decode())
				for currency, price in data.items():
					bot.reply_to(message, "The price of {} is currently {} {}".format(crypto_abbrev_list[0],price, currency))



	except:
	 	bot.reply_to(message, "Invalid format")
bot.polling()
