from telegram import Bot
from database.crud import get_all_users
from config.settings import TOKEN

bot = Bot(token=TOKEN)

def broadcast_message(message: str) -> None:
    users = get_all_users()
    for user in users:
        bot.send_message(chat_id=user.id, text=message)
