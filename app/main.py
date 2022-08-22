## import the required libraries
from operator import le
from pyrogram import Client, filters
from pyrogram.types import User, MessageEntity
from os import path
import json
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

# commands for the bot
@app.on_message(filters.command(['start']))
async def commands_handler(client, message):
    await message.reply('Online and working at full capacity...')

## handlers for the bot
# monitor the messages sent
@app.on_message(filters.text)
async def monitor(client, message):

    # classify the incoming message as either spam or not
    result = model.predict([message.text])
    result = tf.squeeze(tf.round(result))
    # usually spam messages are longer than 10 words + to avoid wrong cases of spam
    if result == 1 and len(message.text.split(sep=' ')) > 10:
        # store in the data of the user
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_warnings = 0
        kick_user = False
        mode = 'w'
        
        if path.exists(f'chat{chat_id}.json'):
            mode = 'r'
        # deal with the file based on its mode (since if it doesn't exit we will create a new object)
        with open(f'chat{chat_id}.json', mode) as file:
            if mode == 'w':
                json_object = {}
            else:
                json_object = json.load(file)
            
            if str(user_id) in list(json_object.keys()):
                user_warnings = json_object.get(str(user_id))
            # if the user has 2 warnings, then remove him/her from the file
            if user_warnings == 2:
                kick_user = True
                json_object.pop(str(user_id))
            # if not, then just increment the warnings count of the user
            else:
                user_warnings = user_warnings + 1
                # json_object[user_id] = user_warnings
                json_object.update({f'{user_id}': user_warnings})
        # update the file with the new values
        with open(f'chat{chat_id}.json', 'w') as file:
            json_object = json.dumps(json_object)
            file.write(json_object)
            
        # if the user exceeded 2 warnings, ban the user from the chat & delete the latest message
        if kick_user:
            username = message.from_user.username
            await message.delete()
            await client.ban_chat_member(chat_id=chat_id, user_id=user_id)
            await client.send_message(text=f"User: {username}\nID: {user_id}\nHas been banned for sending potential spam.", chat_id=chat_id)
        # warn the user of his/her potential spam message
        else:
            await message.reply(f'Potential Spam Detected.\nWarning # {user_warnings}\n3 warnings and you will be removed.')
        


#################################################

#! app starting point
app.run()