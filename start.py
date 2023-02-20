import asyncio
import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from chatGPT import chatGPT
from background import keep_alive

load_dotenv()    
token = os.getenv('BOTTOKEN')
bot = AsyncTeleBot(token)

@bot.message_handler(commands=['start'])
async def sendWelcome(message):
    print(message)
    await bot.send_message(message.from_user.id, 'Nice to meet you! 😇 \n' +
                           'Write me some questions and i’ll try to give you answers 😅')


@bot.message_handler(content_types=['text'])
async def getQuestion(message):
    await bot.send_message(message.from_user.id,'Wait...')
    answer = await chatGPT(message.text)
    await bot.send_message(message.from_user.id, answer)
    
keep_alive()
asyncio.run(bot.infinity_polling())