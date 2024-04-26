import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from config import TOKKEN
from calback import router
from handlers import router
from sql import create_table


# Запуск процесса поллинга новых апдейтов
async def main():
    # Объект бота
    bot = Bot(token=TOKKEN)
    # Диспетчер
    dp = Dispatcher()
    dp.include_router(router)
    # Запускаем создание таблицы базы данных
    await create_table()
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())     
    except KeyboardInterrupt:
        print('Выход')