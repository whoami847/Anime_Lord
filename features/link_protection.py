from database.crud import save_protected_link

def protect_link(update, context):
    try:
        link = context.args[0]
        password = context.args[1]
        save_protected_link(link, password)
        update.message.reply_text(
            f"🔒 Link protected!\n"
            f"URL: {link}\n"
            f"Password: ||{password}||"
        )
    except IndexError:
        update.message.reply_text("Usage: /protect <URL> <PASSWORD>")
