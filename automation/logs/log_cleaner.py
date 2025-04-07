from database.crud import clear_activity_logs

def clear_logs(update: Update, context: CallbackContext) -> None:
    clear_activity_logs()
    update.message.reply_text("Logs cleared!")
