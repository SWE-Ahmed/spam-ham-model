# Messages Monitoring Model Capable of Detecting and Deleting Spam in Public Telegram Group Chats

## 1 - Primary Concept

To be able to monitor the messages sent in a public groupchat, and immediately get rid of spam messages to not clutter up the group-chat.

## 2 - Data Description

| label | whether the message is classified as `spam` or not spam, `ham`.  | 
| :---:   | :-: |
| message | the English message to classify in text format | 

## 3 - Detailed Description

**Background:**

As public group-chats become larger and larger, they become a spammer’s dream. These spammers try to utilise such heavily populated group-chats to either mislead others with false websites, accounts or services. Instead of manually looking out for such messages within a group-chat, we can deploy a ML model capable of detecting these messages and deleting them as soon as they are sent. I will be able to deploy it to an active telegram bot that I can build using the `Pyrogram` package in Python, and then just program my bot to activate the trained model on incoming messages when I add it to a group-chat.

**What will you actually do?**

- Merge datasets together to increase our inventory of training data for this model
- Examine and become one with the dataset by investigating the structure of the messages
- Clean the dataset and preprocess it
- Experiment with various NLP models and evaluate them along the way to come up with an accurate one
- Test the final chosen model on custom data
- Build a Telegram Bot from the Pyrogram package
- Program the bot to activate the trained model on incoming messages.
- Deploy the model to a Telegram group-chat to see it working in action

**What will be the “deliverable”?**

An effective NLP model capable of detecting and deleting spam messages in Telegram group-chats. It will be deployed to an active group-chat to test it out.

**What is the “value proposition”? i.e. Who will benefit and how?**

Public group-chats admins who want to make their group-chats a safe place free of spams and unwanted messages that clutter it up.
