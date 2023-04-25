from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from dotenv import dotenv_values

conf = dotenv_values('settings\.env')

BOT = Bot(token=conf['TOKEN'])
DP = Dispatcher(BOT)


