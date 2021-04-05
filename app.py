from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='1650077573:AAHfZMCUxCyMdBE42gpK9JPRcRVD0O2k_gQ')

dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'Какой-то другой текст'

    await bot.send_message(chat_id=chat_id, text=text)

executor.start_polling(dp)
