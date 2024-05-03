import asyncio 
import logging
from aiogram import Bot, Dispatcher, types , F 
from aiogram.filters.command import Command 
from aiogram.types import Message , FSInputFile , InlineKeyboardButton
from aiogram.types import KeyboardButton , InlineKeyboardMarkup
from aiogram.filters import and_f

API_TOKEN="6888623440:AAE7u1l8fRl4HqvUfNCbciQHbc4KnbBxHTc"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN,protect_content=True)
dp = Dispatcher()


import requests
url = "http://127.0.0.1:8000/"
r = requests.get(url).json()




@dp.message()
async def kino(message: types.Message):
   for i in r:
      if int(message.text) == int(i['kod']):
         await message.answer_video(video=i['silka'],caption=i['qoshimcha'])
      else:
         await message.answer("kod xato")




@dp.message(Command("start"))
async def hastart(message: types.Message):
    start_param = message.text.split(' ')[-1]
    for i in r:
      if int(start_param) == int(i['kod']):
         await message.answer_video(video=i['silka'],caption=i['qoshimcha'])
      else:
         await message.answer("kod xato")








async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())