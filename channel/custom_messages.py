from telegram import Update
from telegram.ext import CallbackContext
from database.crud import update_channel_message

def set_join_message(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text("Usage: /setjoinmsg Your custom message")
        return
    
    message = ' '.join(context.args)
    update_channel_message(message)
    update.message.reply_text("Custom message updated!")
