#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/13
# Modified: lei.cheng 2021/10/13

from datetime import datetime, timedelta
from wechaty import Message, FileBox

from spider.bilibili_spider.config import global_config


async def good_morning_and_medicine(msg: Message):
    good_morning_and_medicine_enable = global_config.get_raw('lei_bot_function', 'good_morning_and_medicine_enable')
    if good_morning_and_medicine_enable != 'true':
        return
    if msg.is_self():
        if ('早上好' in msg.text()) or ('早安' in msg.text()):
            morning_begin_time = '06:00'
            morning_end_time = '12:00'
            current_time = (datetime.now() - timedelta(hours=15)).strftime("%H:%M")
            if morning_begin_time < current_time < morning_end_time:
                await msg.say("机器人磊磊：早安吃药！")


async def good_night_and_sweet_dreams(msg: Message):
    good_night_and_sweet_dreams_enable = global_config.get_raw('lei_bot_function', 'good_night_and_sweet_dreams_enable')
    if good_night_and_sweet_dreams_enable != 'true':
        return
    if '晚安' in msg.text():
        await msg.say("机器人磊磊：今日份好梦：")
        await msg.say("老婆好梦呢！")

        file_box = FileBox.from_url(
            'https://img-blog.csdnimg.cn/a824386289054e0a8fe746b989e40014.png',
            name='sweet-dreams.jpg'
        )
        await msg.say(file_box)
