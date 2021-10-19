#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/19
# Modified: lei.cheng 2021/10/19

from wechaty import Contact, Message
from typing import Union


async def lei_say(speaker: Union[Contact, Message], text):
    """机器人回复标志，'磊：xxxxxxxx' """

    await speaker.say('磊：{}'.format(text))

