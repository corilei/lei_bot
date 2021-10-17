"""
Python Wechaty - https://github.com/wechaty/python-wechaty
Authors:    Huan LI (李卓桓) <https://github.com/huan>
            Jingjing WU (吴京京) <https://github.com/wj-Mcat>
2020 @ Copyright Wechaty Contributors <https://github.com/wechaty>
Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from wechaty import Contact, Message, Wechaty, ScanStatus

from chatbot.chatter_bot_function import chat_bot_mode, train_chat_bot_mode, chat_bot_super_manager_mode
from conversion.message_function import good_morning_and_medicine, good_night_and_sweet_dreams
from spider.bilibili_spider.query_bili import query_dynamic

from spider.bilibili_spider.config import global_config
from wechaty import get_logger

from wechaty_bot.authority_manage import is_permission
from wechaty_bot.bot_setting import bot_setting

os.environ['WECHATY_PUPPET'] = "wechaty-puppet-service"
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = "corilei_8888"
os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = "8.130.176.152:9099"

logger = get_logger('Wechaty')


async def on_message(msg: Message):
    """
    Message Handler for the Bot
    """
    if not is_permission(msg):
        return
    # 机器人设置
    await bot_setting(msg)
    # 早安吃药消息
    await good_morning_and_medicine(msg)
    # 晚安好梦消息
    await good_night_and_sweet_dreams(msg)
    # 聊天机器人消息
    await chat_bot_mode(msg)
    # 训练聊天机器人消息
    await train_chat_bot_mode(msg)
    # 聊天机器人超级管理员模式
    await chat_bot_super_manager_mode(msg)


async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    """
    Scan Handler for the Bot
    """
    logger.info('Status: ' + str(status))
    logger.info('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    """
    Login Handler for the Bot
    """
    logger.info(user)
    await user.say("wechaty bot 启动成功！")


async def create_bot():
    """
    Async Main Entry
    """
    #
    # Make sure we have set WECHATY_PUPPET_SERVICE_TOKEN in the environment variables.
    #
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        logger.info('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    scheduler = AsyncIOScheduler()
    # B站定时爬虫
    scheduler.add_job(code_spider, 'interval', seconds=5, args=[bot])
    scheduler.start()

    bot.on('scan',      on_scan)
    bot.on('login',     on_login)
    bot.on('message',   on_message)

    await bot.start()

    logger.info('[Python Wechaty] Ding Dong Bot started.')


async def code_spider(bot):
    uid_list = global_config.get_raw('config', 'uid_list').split(',')
    for uid in uid_list:
        msg = query_dynamic(uid)
        if msg:
            contact = await bot.Contact.find('程磊')
            await contact.say("机器人磊磊：{}".format(msg))


if __name__ == "__main__":
    asyncio.run(create_bot())
