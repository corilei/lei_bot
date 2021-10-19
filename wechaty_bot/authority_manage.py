#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/17
# Modified: lei.cheng 2021/10/17
from spider.bilibili_spider.config import global_config
from wechaty import Message


def is_permission(msg: Message):
    """验证聊天权限"""
    whitelist_enable = global_config.get_raw('lei_bot_function', 'whitelist_enable')
    # 不需要验证权限
    if not whitelist_enable:
        return True
    # 读取白名单
    whitelist = global_config.get_raw('lei_bot_function', 'whitelist').split(',')
    if msg.talker().name in whitelist:
        return True
    else:
        return False


async def add_whitelist(msg: Message):
    """加入白名单"""
    text = msg.text()
    if msg.is_self():
        if text.startswith('磊添加用户'):
            if len(text) <= 5:
                await msg.say('磊：请输入完整姓名！')
            name = text[5:]
            whitelist = global_config.get_raw('lei_bot_function', 'whitelist').split(',')
            if name in whitelist:
                await msg.say('磊：' + name + '已在白名单中！')
                return
            whitelist_str = global_config.get_raw('lei_bot_function', 'whitelist')
            new_whitelist_str = whitelist_str + ',' + name
            global_config.set('lei_bot_function', 'whitelist', new_whitelist_str)
            await msg.say('磊：添加成功！')


async def delete_whitelist(msg: Message):
    """将用户从白名单中删除"""
    text = msg.text()
    if msg.is_self():
        if text.startswith('磊删除用户'):
            if len(text) <= 5:
                await msg.say('磊：请输入完整姓名！')
            name = text[5:]
            whitelist = global_config.get_raw('lei_bot_function', 'whitelist').split(',')
            if name not in whitelist:
                await msg.say('磊：' + name + ' 不在白名单中！')
                return
            whitelist.remove(name)
            new_whitelist_str = ','.join(whitelist)
            global_config.set('lei_bot_function', 'whitelist', new_whitelist_str)
            await msg.say('磊：删除成功！')


async def select_whitelist(msg: Message):
    """查看白名单"""
    text = msg.text()
    if msg.is_self():
        if text.startswith('磊查看用户'):
            whitelist = global_config.get_raw('lei_bot_function', 'whitelist')
            await msg.say('磊：用户如下：\n' + whitelist)
