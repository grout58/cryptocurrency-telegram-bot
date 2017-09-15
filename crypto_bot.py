import telebot, urllib.request, json

bot = telebot.TeleBot("<TOKEN>")

user = bot.get_me()

@bot.message_handler(commands=['help'])
def print_help(message):
	bot.reply_to(message, """
	/eth - displays the price of Ether
	/btc - displays the price of Bitcoin
	/xmr - displays the price of Monero
	/ltc - displays the price of Litecoin
	/bcc - displays the price of Bitcoin Cash
""")

@bot.message_handler(commands =['eth'])
def eth_price(message):
	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR") as url:
		data = json.loads(url.read().decode())
		for currency, price in data.items():
				if currency == 'USD':
					bot.reply_to(message, "The price of Ethereum is currently {} {}".format(currency, price))

@bot.message_handler(commands =['btc'])
def btc_price(message):
	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BTC,USD,EUR") as url:
		data = json.loads(url.read().decode())
		for currency, price in data.items():
				if currency == 'USD':
					bot.reply_to(message, "The price of Bitcoin is currently {} {}".format(currency, price))

@bot.message_handler(commands =['xmr'])
def xmr_price(message):
	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=BTC,USD,EUR") as url:
		data = json.loads(url.read().decode())
		for currency, price in data.items():
				if currency == 'USD':
					bot.reply_to(message, "The price of Monero is currently {} {}".format(currency, price))

@bot.message_handler(commands =['ltc'])
def xmr_price(message):
	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=BTC,USD,EUR") as url:
		data = json.loads(url.read().decode())
		for currency, price in data.items():
				if currency == 'USD':
					bot.reply_to(message, "The price of Litecoin is currently {} {}".format(currency, price))

@bot.message_handler(commands =['bcc'])
def bcc_price(message):
	with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=BCC&tsyms=BTC,USD,") as url:
		data = json.loads(url.read().decode())
		for currency, price in data.items():
				if currency == 'USD':
					bot.reply_to(message, "The price of Bitcoin Cash is currently {} {}".format(currency, price))



bot.polling()
