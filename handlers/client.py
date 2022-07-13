from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help']) # Дикоратор
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного, Вам выбора нашего ассортимента!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/orexmall_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def orex_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 22:00, Сб-Вс с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def orex_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Уличная 1', reply_markup=ReplyKeyboardRemove())


# dp.message_handler(commands=['Меню'])
# async def orex_menu_command(message: types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(orex_open_command, commands=['Режим_работы'])
    dp.register_message_handler(orex_place_command, commands=['Расположение'])