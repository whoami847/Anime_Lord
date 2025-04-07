from telegram import Update
from database.crud import get_all_users

def list_users(update: Update, context: CallbackContext) -> None:
    users = get_all_users()
    user_list = "\n".join([f"{user.id}: {user.username}" for user in users])
    update.message.reply_text(f"Users:\n{user_list}")
