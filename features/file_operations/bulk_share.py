import os
from telegram import InputMediaDocument

def bulkshare(update, context):
    folder_path = context.args[0]
    if not os.path.isdir(folder_path):
        update.message.reply_text("❌ Invalid folder path")
        return
    
    media_group = [
        InputMediaDocument(open(os.path.join(folder_path, f), "rb"))
        for f in os.listdir(folder_path)
    ]
    
    context.bot.send_media_group(
        chat_id=update.effective_chat.id,
        media=media_group
    )
