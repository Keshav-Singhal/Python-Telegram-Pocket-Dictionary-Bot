import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

def get_url(word):
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Token 8f2b211a8d8ed2fe2ed3c073f52f75df7fa065af'
    }

    # Make the API request
    response = requests.get('https://owlbot.info/api/v4/dictionary/' + word, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        return {"error": "API request failed with status code " + str(response.status_code)}

    # Try to parse the response as JSON
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Failed to decode JSON from API response"}

async def name(update: Update, context):
    user_input = update.message.text
    data = get_url(user_input)

    # Check if there was an error
    if "error" in data:
        await update.message.reply_text(data["error"])
        return

    defy = data.get('definitions')
    
    if defy:
        await update.message.reply_text("Meaning: " + defy[0]['definition'])
        await update.message.reply_text("Example: " + defy[0].get('example', 'No example available'))
        await update.message.reply_text("Image: " + defy[0].get('image_url', 'No image available'))
    else:
        await update.message.reply_text("No definitions found for the word.")

def main():
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Add handler for text messages
    application.add_handler(MessageHandler(filters.TEXT, name))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
