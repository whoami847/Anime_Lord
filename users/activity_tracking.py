from datetime import datetime
from database.crud import log_activity

def track_activity(user_id: int, action: str) -> None:
    log_activity(
        user_id=user_id,
        action=action,
        timestamp=datetime.now()
    )
