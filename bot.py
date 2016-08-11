from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from telegram import ParseMode, ReplyKeyboardMarkup, Emoji
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token="262687283:AAFCR8A11Re67G-0PmpRAvoeEi8ovCcHRJE")
dispatcher = updater.dispatcher

logger = logging.getLogger()
logger.setLevel(logging.INFO)

custom_keyboard = [[ Emoji.THUMBS_UP_SIGN, Emoji.THUMBS_DOWN_SIGN ]]

reply_markup = ReplyKeyboardMarkup(custom_keyboard)

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, *please* talk to me!", parse_mode=ParseMode.MARKDOWN)
	bot.sendPhoto(chat_id=update.message.chat_id, photo='https://telegram.org/img/t_logo.png')
	bot.sendMessage(chat_id=update.message.chat_id, text="Some text", reply_markup=reply_markup)

def engineer(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Ok! Please list the technologies that you have experience separated by comma. *Please follow this example*: \n\n_/skills node-js, python, java, html, css, javascript_", parse_mode=ParseMode.MARKDOWN)

def list_of_skills(bot, update):
	msg = update.message.text.replace("/skills", "").replace(" ", "").split(",")
	choose = [[]]
	temp = 0
	for i in msg:
		if len(choose[temp]) > 4:
			temp = temp + 1
			choose.append([])
		choose[temp].append(i)

	choose_markup = ReplyKeyboardMarkup(choose)
	if bot.getMe().username != update.message.chat.username:
		bot.sendMessage(chat_id=update.message.chat_id, text="Please, choose your primary skill.", reply_markup=choose_markup)

start_handler = CommandHandler('start', start)
engineer_handler = CommandHandler("engineer", engineer)
list_of_skills_handler = CommandHandler("skills", list_of_skills)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(engineer_handler)
dispatcher.add_handler(list_of_skills_handler)

updater.start_polling()
