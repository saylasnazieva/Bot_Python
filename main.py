

from aiogram import types, executor , Dispatcher, Bot
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup 

TOKEN = "6203280405:AAFFry3h-y0cTaBXts7f_oakLpD2gvBs8Ao"
bot = Bot(token=TOKEN) 
dp = Dispatcher(bot)



@dp.message_handler(cammands=["start"])
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton("Как дела?,"  callback_data="but_1) 
    markup.add(but_1)

    await bot.send_message(message.chat.id, "Привет, Привет !", reply_markup=markup)
    

@dp.message_handler(content_types=["text"])
async def text(message: types.Message):

 if message.text.lower() == "пока" :
    await bot.send_message(message.chat.id,"Пока")


@dp.callback_query_handler(lambda c: c.data == "but_1")
async def button_reaction(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send.message(call.message.chat.id,"Дела нормально")

