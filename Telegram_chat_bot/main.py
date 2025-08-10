from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_USERNAME = "@tele_1997_bot"

class Reference:
    '''
    This class is used to manage the reference memory.
    Stores the previous responses from openai API.
    '''

    # Empty memory
    def __init__(self) -> None:
        self.response = ""


reference = Reference()
model_name = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


def clear_chat_history():
    """
    Function to clear the chat history.
    """
    reference.response = ""


@dp.message_handler(commands=['clear'])
async def command_clear_handler(message: types.Message):
    '''
    This handler receives messages with /clear command
    '''
    clear_chat_history()
    await message.reply("Chat history cleared.")


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    '''
    This function receives messages with /start command
    '''
    await message.reply("Hi!\nI'm your echo bot.\nHow may I assist you?")


@dp.message_handler(commands=['help'])
async def command_help_handler(message: types.Message):
    '''
    This handler receives messages with /help command
    '''
    help_command = """
    Available commands:
    /start - Start the bot
    /clear - Clear the chat
    /help - Show this help message
    """
    await message.reply(help_command)


@dp.message_handler()
async def chatgpt(message: types.Message):
    '''
    A handler to process the user's input and generate
    a response using the chatGPT API.
    '''
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = model_name,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} # our query
        ]
    )
    reference.response = response.choices[0].message.content
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(
        chat_id=message.chat.id,
        text=reference.response
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 

"""
Skip_updates=True means that the bot will not process any updates that were sent while it was offline
if its false, the bot will process all updates, including those that were sent while it was offline
"""