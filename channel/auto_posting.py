from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
from config.settings import TOKEN

scheduler = BackgroundScheduler()
bot = Bot(token=TOKEN)

def autopost_to_channel(channel: str, content: str) -> None:
    scheduler.add_job(
        bot.send_message,
        'interval',
        hours=24,
        kwargs={'chat_id': channel, 'text': content}
    )
