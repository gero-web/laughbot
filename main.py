from loader import  DP, BOT
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from keyboards import InlineKeyBoardBuilder



def register_handlers(handlers:list):
    for handler in handlers:
        handler(DP)




async def  callback(callback_query):
    await BOT.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
    


async def echo(msg:Message):
    b = InlineKeyBoardBuilder([("Button", 'kek')])
    await msg.answer(msg.text, reply_markup=b)
    

def register_echo_hendlers(dp:Dispatcher):
    dp.register_message_handler(echo, content_types=['text'])





def start():
     executor.start_polling(DP, skip_updates=True)

if __name__ == '__main__':
    register_handlers([register_echo_hendlers])
    start()
   