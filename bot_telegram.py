from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

import os

# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел онлайн')
'''*********************************КЛИЕНТСКАЯ ЧАСТЬ*********************************'''


@dp.message_handler(commands=['start', 'help']) # Дикоратор
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного, Вам выбора нашего ассортимента!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/orexmall_bot')


@dp.message_handler(commands=['Режим_работы'])
async def orex_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 22:00, Сб-Вс с 10:00 до 23:00')


@dp.message_handler(commands=['Расположение'])
async def orex_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Уличная 1')

'''*********************************АДМИНСКАЯ ЧАСТЬ*********************************'''
'''*********************************ОБЩАЯ ЧАСТЬ*********************************'''


@dp.message_handler() # Дикоратор
async def echo_send(message: types.Message):
    if message.text == 'Привет':

        await message.answer('И тебе привет!')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)