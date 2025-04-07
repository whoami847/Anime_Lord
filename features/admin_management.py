from telegram import Update
from database.crud import update_user_role

def add_admin(update: Update, context):
    target_user = context.args[0]
    if not validate_user(update.effective_user.id):
        update.message.reply_text("Permission denied!")
        return
    
    update_user_role(target_user, "admin")
    update.message.reply_text(f"✅ {target_user} promoted to admin")

def remove_admin(update: Update, context):
    target_user = context.args[0]
    update_user_role(target_user, "user")
    update.message.reply_text(f"❌ {target_user} demoted")
