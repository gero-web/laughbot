from aiogram import Dispatcher




def register_callback(dp:Dispatcher, callback , filter):
    dp.register_callback_query_handler( callback, lambda f: f.data == filter )
