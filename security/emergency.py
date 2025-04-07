import os
from config.settings import DB_PATH

def emergency_reset():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    # Add other cleanup operations
