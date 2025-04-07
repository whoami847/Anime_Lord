from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from .delete import delete_file

scheduler = BackgroundScheduler()
scheduler.start()

def set_file_expiry(update, context):
    try:
        hours = int(context.args[0])
        file_id = context.args[1]  # Get from uploaded file
        expiry_time = datetime.now() + timedelta(hours=hours)
        
        scheduler.add_job(
            delete_file,
            'date',
            run_date=expiry_time,
            args=[file_id]
        )
        update.message.reply_text(f"⏳ File will auto-delete in {hours} hours")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /expire <HOURS> <FILE_ID>")
