# Messages Monitoring Model Capable of Detecting and Deleting Spam in Public Telegram Group Chats
<p align="center">
<a href="url"><img src="https://docs.pyrogram.org/_static/pyrogram.png" align="center" height="250" width="250" ></a>
<a href="url"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/2048px-Telegram_logo.svg.png" align="center" height="250" width="250" ></a>
<a href="url"><img src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/google-tensorflow-icon.png" align="center" height="250" width="250" ></a>
</p>

## Repository Structure
```
.
├── README.md
├── app
│   ├── main.py
├── data
│   ├── sms_spam.csv
│   ├── SPAM text message 20170820 - Data.csv
│   ├── spam.csv
├── model
│   ├── spam_detection_model
│   │   ├── assets
│   │   ├── variables
│   │       ├── variables.data-00000-of-00001
│   │       ├── variables.index
│   │   ├── keras_metadata.pb
│   │   ├── saved_model.pb
│   ├── model.png
│   ├── spam_ham_model.ipynb
├── presentations
│   ├── capstone_presentation.key
│   ├── capstone_presentation.pdf
├── reports
│   ├── capstone_report
│   │   ├── capstone_report_files
│   │   ├── capstone_report.html
│   │   ├── capstone_report.qmd
│   │   ├── styles.css
│   ├── progress_report
│       ├── progress_report.md
│       ├── progress_report.pdf
.
```

## Project Description

This project addresses the problem of spam messages being sent out via various users to public groupchats. A possible solution has been built in this project, in which a deep learning model was trained on sms messages, labelled as either spam or not, and then used in a Telegram bot to detect incoming spam messages in the deployed Telegram groupchats.

## Detailed Description

**Background:**

As public group-chats become larger and larger, they become a spammer’s dream. These spammers try to utilise such heavily populated group-chats to either mislead others with false websites, accounts or services. Instead of manually looking out for such messages within a group-chat, we can deploy a ML model capable of detecting these messages and deleting them as soon as they are sent. I will be able to deploy it to an active telegram bot that I can build using the `Pyrogram` package in Python, and then just program my bot to activate the trained model on incoming messages when I add it to a group-chat.

## Data Description

| label | whether the message is classified as `spam` or not spam, `ham`|
| :---:   | :-: |
| message | the English message to classify in text format |
