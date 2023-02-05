import re
import telegram
from telegram.ext import Updater, MessageHandler, Filters

def remove_abv_words(text):
    return ' '.join(re.sub(r'\b\w*абв\w*\b', '', word) for word in text.split())

def text_message(update, context):
    text = update.message.text
    filtered_text = remove_abv_words(text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=filtered_text)

def main():
    bot = telegram.Bot(token='TOKEN')
    updater = Updater(bot.token, use_context=True)
    dispatcher = updater.dispatcher

    text_handler = MessageHandler(Filters.text, handle_text_message)
    dispatcher.add_handler(text_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
