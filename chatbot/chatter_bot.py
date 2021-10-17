#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/13
# Modified: lei.cheng 2021/10/13

# Modified: lei.cheng 2021/10/7
from typing import List

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import platform

database_uri = ''

if platform.system() == 'Linux':  # linux
    database_uri = 'sqlite:////root/chenglei/lei_bot/chatbot/chatbot_database.sqlite3'
elif platform.system() == 'Darwin':  # mac
    database_uri = 'sqlite:////Users/cori/PycharmProjects/lei_bot/chatbot/chatbot_database.sqlite3'

chatbot = ChatBot(
    'lei_chatter_bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri=database_uri,
    # database_uri='sqlite:////root/chenglei/lei_bot/chatbot/chatbot_database.sqlite3',
)


async def chat_bot_trainer(conversation: List):
    """对话训练器"""
    list_trainer = ListTrainer(chatbot)
    list_trainer.train(conversation)


if __name__ == "__main__":

    # conversation = [
    #     "Hello",
    #     "Hi there!",
    #     "How are you doing?",
    #     "I'm doing great.",
    #     "That is good to hear",
    #     "Thank you.",
    #     "You're welcome."
    # ]
    # trainer = ListTrainer(chatbot)
    # trainer.train(conversation)

    # trainer = ChatterBotCorpusTrainer(chatbot)
    # trainer.train('chatterbot.corpus.chinese')

    # conversation_1 = [
    #     "我最喜欢干什么",
    #     "拉屎"
    # ]
    # chat_bot_trainer(conversation_1)

    print('Type something to begin...')

    while True:
        try:
            user_input = input()

            bot_response = chatbot.get_response(user_input)

            print(bot_response)

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
