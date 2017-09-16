import telebot, urllib.request, json

bot = telebot.TeleBot("TOKEN")

user = bot.get_me()

@bot.message_handler(commands=['help'])
def print_help(message):
	bot.reply_to(message, """
	To get the current price of any cryptocurrency type
	in /<abbreviation>
	IE /btc
	IE /eth
"""



@bot.message_handler(func=lambda m: True)
def all_price(message):
	try:
		crypto_abbrev = message.text.replace("/", "").upper()
		with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=BTC,USD,EUR".format(crypto_abbrev)) as url:
			data = json.loads(url.read().decode())
			for currency, price in data.items():
				if currency == 'USD':
					bot.reply_to(message, "The price of {} is currently {} {}".format(crypto_abbrev,currency, price))

	except:
		bot.reply_to(message, "Error, use / then abbreviation")
bot.polling()
