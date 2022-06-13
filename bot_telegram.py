from aiogram.utils import executor
from create_bot import dp


# bot = Bot(token=os.getenv('TOKEN'))


async def on_startup(_):
    print('Бот вышел онлайн')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)