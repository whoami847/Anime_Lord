import shutil
from datetime import datetime
from config.settings import DB_PATH

def backup_db():
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    backup_name = f"backup_{timestamp}.db"
    shutil.copyfile(DB_PATH, backup_name)
    return backup_name
