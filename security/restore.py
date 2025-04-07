import shutil
from config.settings import DB_PATH

def restore_db(backup_file: str) -> None:
    shutil.copyfile(backup_file, DB_PATH)
