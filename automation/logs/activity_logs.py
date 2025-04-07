from database.crud import get_activity_logs

def show_activity_logs(update: Update, context: CallbackContext) -> None:
    logs = get_activity_logs()
    log_text = "\n".join([f"{log.timestamp}: {log.action}" for log in logs])
    update.message.reply_text(f"Activity Logs:\n{log_text}")
