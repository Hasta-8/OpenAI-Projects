import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# print(TELEGRAM_BOT_TOKEN)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    '''
    This handler receives messages with /start and /help commands
    '''
    await message.reply("Hi!\nI'm your echo bot.\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
    '''
    This will return echo
    '''
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)