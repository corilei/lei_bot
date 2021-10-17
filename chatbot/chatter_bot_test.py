#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/13
# Modified: lei.cheng 2021/10/13
from chatbot.chatter_bot import chatbot

if __name__ == "__main__":

    print('Type something to begin...')

    while True:
        try:
            user_input = input()

            bot_response = chatbot.get_response(user_input).text

            print(type(bot_response), ': ', bot_response)

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


