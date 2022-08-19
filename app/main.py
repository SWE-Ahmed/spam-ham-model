## import the required libraries
from pyrogram import Client

## define helper functions

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

# MAIN function
async def main():
    async with app:
        await app.send_message("me", "Hi!")

#############################################

# initialize the telegram bot
# these variables can later be omitted if the sessions are created for both the user and the bot
api_id, api_hash, bot_token = get_credentials()
app = Client("my_account", 
             api_id=api_id, 
             api_hash=api_hash)


#! app starting point
app.run(main())