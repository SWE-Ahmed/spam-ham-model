## import the required libraries
from pyrogram import Client, filters
import tensorflow as tf

## helper function for getting credentials
# read in the credentials
def get_credentials():
    """
    Reads the credentials for the telegram bot from a 'credentials.config' file
    Returns:
     a tuple containing the api_id and api_hash read in from the file
    """
    
    with open("./credentials.config", "r") as file:
        api_id = file.readline().strip()
        api_hash = file.readline().strip()
        bot_token = file.readline().strip()
    
    return (api_id, api_hash, bot_token)

# initialize the telegram bot and load in the model
# these variables can later be omitted if the sessions are created for both the user and the bot
api_id, api_hash, bot_token = get_credentials()
app = Client("my_account", 
             api_id=api_id, 
             api_hash=api_hash)
model = tf.keras.models.load_model("../model/spam_detection_model")

#################################################

## handlers for the bot

# monitor the messages sent
@app.on_message(filters.text)
async def monitor(client, message):
    result = model.predict([message.text])
    result = tf.squeeze(tf.round(result))
    
    if result == 1:
        await message.reply('SPAM DETECTED')

# @app.on_message(filters.text)
# def text_handler(client, message):
#     if message.text.lower() == "hi":
#         message.reply("Hello")
#     elif message.text.lower() == "profile":
#         userId = message.reply_to_message.from_user.id
#         profile = app.get_users(userId)
#         id_ = profile.id
#         name = profile.first_name + ' ' + profile.last_name
#         userName = profile.username
#         message.reply(f'Name: {name}\n ID: {id_}\n Username: {userName}')


#################################################

#! app starting point
app.run()