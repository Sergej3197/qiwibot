import logging
from aiogram import Bot, executor, Dispatcher, types
from sendmessage.command_message import user_command
from sendmessage.callback_message import user_callback
from sendmessage.user_message import users_typesMessage
from bd.bd import Database
from marcup.marcup import user_marcup


logging.basicConfig(level=logging.ERROR, filename="error.log")
TOKEN = ""
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
main_command = user_command()
user_call = user_callback()
usr_typesMessage = users_typesMessage()
bd = Database()
bd.add_tables()
add_mrkp =user_marcup()

@dp.message_handler(commands = ['start', 'admin'], chat_type=[types.ChatType.PRIVATE])
async def sender(message: types.Message):
    main_command(message.from_user.full_name, message.text, message.from_user.id)
    if main_command.user_type == 'text':
        await bot.send_message(chat_id = message.from_user.id, text = main_command.message_text, reply_markup = main_command.marcup)
   
@dp.callback_query_handler(chat_type = [types.ChatType.PRIVATE])
async def platej(callback: types.CallbackQuery):
    user_call(callback.data, callback.from_user.id)
    if user_call.user_type == 'text':
        await bot.send_message(chat_id = callback.from_user.id, text = user_call.message_text, reply_markup = user_call.marcup)
    elif user_call.user_type == 'uploading_users':
        for adm_usr in user_call.admin_users:
            await bot.send_message(chat_id = callback.from_user.id, text = f"Пользователь {adm_usr[0]}, баланс {adm_usr[1]}", reply_markup = add_mrkp.addinlineMarkup_usr(adm_usr[0]))

@dp.message_handler()
async def echo(message: types.Message):
    usr_typesMessage(message.text, message.from_user.id)
    if usr_typesMessage.user_type == 'text':
        await bot.send_message(chat_id = message.from_user.id, text = usr_typesMessage.message_text, reply_markup = usr_typesMessage.marcup)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)