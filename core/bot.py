from telegram.ext import Updater, CommandHandler
from config.settings import TOKEN
import core.commands as commands

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("admin", commands.handle_admin))
    dp.add_handler(CommandHandler("protect", commands.protect_link))
    dp.add_handler(CommandHandler("expire", commands.set_expiry))
    # Add other commands...

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
