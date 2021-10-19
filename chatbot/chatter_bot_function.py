#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/13
# Modified: lei.cheng 2021/10/13
from wechaty.user import Room
from wechaty import Contact

from chatbot.chatter_bot import chatbot, chat_bot_trainer
from spider.bilibili_spider.config import global_config
from typing import Union

chat_friend: list = []
# whitelist = ['wxid_8980079809015']
whitelist = []

train_question: str = ''
train_response: str = ''

wake_word = ['机器人磊磊', '磊磊机器人']
stop_word = ['再见', '拜拜', '关闭', '退出']


async def chat_bot_mode(msg):
    """聊天机器人模式"""
    chat_bot_mode_enable = global_config.get_raw('lei_bot_function', 'chat_bot_mode_enable')
    if chat_bot_mode_enable != 'true':
        return
    from_contact = msg.talker()
    text = msg.text()
    room = msg.room()
    conversation: Union[
        Room, Contact] = from_contact if room is None else room

    if ("再见磊" == text) or (any([word in text for word in wake_word]) and any([word in text for word in stop_word])):
        try:
            chat_friend.remove(conversation)
        except Exception as e:
            return
        await conversation.ready()
        await conversation.say('磊：好的，有需要随时叫我')
        return

    elif ("磊" == text) or any([word in text for word in wake_word]):
        chat_friend.append(conversation)
        await conversation.ready()
        await conversation.say('磊：闲聊功能开启成功！现在你可以和我聊天啦！')
        return

    if conversation in chat_friend and not text.startswith('0'):
        data = chatbot.get_response(text).text
        await conversation.ready()
        await conversation.say('磊：{}'.format(data))
        return


async def train_chat_bot_mode(msg):
    """训练聊天机器人模式"""
    train_chat_bot_mode_enable = global_config.get_raw('lei_bot_function', 'train_chat_bot_mode_enable')
    if train_chat_bot_mode_enable != 'true':
        return
    from_contact = msg.talker()
    text = msg.text()
    room = msg.room()
    conversation: Union[
        Room, Contact] = from_contact if room is None else room

    global train_question
    global train_response

    if conversation in chat_friend:
        if not text.startswith('0'):
            train_question = text
        if text.startswith('0') and train_question:
            train_response = text[1:]
            await chat_bot_trainer([train_question, train_response])
            await conversation.say('磊：get!')


async def chat_bot_super_manager_mode(msg):
    """聊天机器人超级管理员模式"""
    chat_bot_super_manager_mode_enable = global_config.get_raw('lei_bot_function', 'chat_bot_super_manager_mode_enable')
    if chat_bot_super_manager_mode_enable != 'true':
        return
    from_contact = msg.talker()
    text = msg.text()
    room = msg.room()
    conversation: Union[
        Room, Contact] = from_contact if room is None else room

    if msg.is_self():
        if '关闭聊天功能' == text:
            global_config.set('lei_bot_function', 'chat_bot_mode_enable', 'false')
            global_config.set('lei_bot_function', 'train_chat_bot_mode_enable', 'false')
            await msg.say("磊：关闭聊天功能！")
        if '开启聊天功能' == text:
            global_config.set('lei_bot_function', 'chat_bot_mode_enable', 'true')
            global_config.set('lei_bot_function', 'train_chat_bot_mode_enable', 'true')
            await msg.say("磊：开启聊天功能！")

        if '关闭晚安好梦功能' == text:
            global_config.set('lei_bot_function', 'good_night_and_sweet_dreams_enable', 'false')
            await msg.say("磊：关闭晚安好梦功能！")
        if '开启晚安好梦功能' == text:
            global_config.set('lei_bot_function', 'good_night_and_sweet_dreams_enable', 'true')
            await msg.say("磊：开启晚安好梦功能！")

        if '关闭白名单' == text:
            global_config.set('lei_bot_function', 'whitelist_enable', 'false')
            await msg.say("磊：关闭白名单！")
        if '开启白名单' == text:
            global_config.set('lei_bot_function', 'whitelist_enable', 'true')
            await msg.say("磊：开启白名单！")
