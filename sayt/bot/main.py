import asyncio 
import logging
from aiogram import Bot, Dispatcher, types , F 
from aiogram.filters.command import Command 
from aiogram.types import Message , FSInputFile , InlineKeyboardButton
from aiogram.types import KeyboardButton , InlineKeyboardMarkup
from aiogram.filters import and_f

API_TOKEN="6888623440:AAE7u1l8fRl4HqvUfNCbciQHbc4KnbBxHTc" 
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("salom")


import requests
url = ""
r = requests.get(url).json()

@dp.message()
async def xabar(message: Message):
    for i in r:
        if int(message.text) == int(i['kod']):
            await message.answer_video(video=i['silka'],caption=i['qoshimcha'])
        else:
            await message.answer("kod noto'g'ri")







async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())