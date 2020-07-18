from telegram.ext import Updater, MessageHandler, Filters
import requests

def get_url(word):
    headers = { 'Content-Type': 'application/json', 'Authorization': 'Token 8f2b211a8d8ed2fe2ed3c073f52f75df7xxxxx',}
    data = requests.get('https://owlbot.info/api/v4/dictionary/'+word, headers = headers).json()
    return data


def name(update, context):
  chat_id = update.message.chat_id
  user_input = update.message.text
  data = get_url(user_input)
  defy = data['definitions']
  update.message.reply_text("Meaning: "+defy[0]['definition'])
  update.message.reply_text("Example: "+defy[0]['example'])
  update.message.reply_text("Image: "+defy[0]['image_url'])


def main():
    updater = Updater("1364914392:AAHHoNu1uRpjPB3bAaOzi0oixxxxxxx", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, name))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
