#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/17
# Modified: lei.cheng 2021/10/17

from wechaty import Message

from wechaty_bot.authority_manage import add_whitelist, delete_whitelist, select_whitelist


async def bot_setting(msg: Message):
    """机器人设置"""
    await add_whitelist(msg)
    await delete_whitelist(msg)
    await select_whitelist(msg)
