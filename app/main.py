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

#################################################

# initialize the telegram bot and load in the model
# these variables can later be omitted if the sessions are created for both the user and the bot
api_id, api_hash, bot_token = get_credentials()
app = Client("my_bot", 
             api_id=api_id, 
             api_hash=api_hash,
             bot_token=bot_token)

print('>>> Loading Model...')
model = tf.keras.models.load_model("../model/spam_detection_model")
print('>>> Model Loaded Successfully.')

#################################################

## handlers for the bot
# monitor the messages sent
@app.on_message(filters.text)
async def monitor(client, message):
    
    # model classifies commands as spam, thus we ignore them
    if (message.text).split()[0][0] != '/':
        # classify the incoming message as either spam or not
        result = model.predict([message.text])
        result = tf.squeeze(tf.round(result))
        if result == 1:
            name = message.from_user.first_name + ' ' + message.from_user.last_name
            chat_id = message.chat.id
            id = message.from_user.id
            await message.delete()
            await client.ban_chat_member(chat_id=chat_id, user_id=id)
            await client.send_message(text=f"User, {name}, with ID, {id}, has been kicked out for sending spam.", chat_id=chat_id)
        
# commands for the bot
@app.on_message(filters.command(['start']))
async def commands_handler(client, message):
    message.reply('Online and working at full capacity...')


#################################################

#! app starting point
app.run()