from sqlalchemy.orm import Session
from .models import User, ActivityLog

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def log_activity(db: Session, user_id: int, action: str, timestamp):
    log = ActivityLog(user_id=user_id, action=action, timestamp=timestamp)
    db.add(log)
    db.commit()
