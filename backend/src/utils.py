from datetime import datetime
from zoneinfo import ZoneInfo


def get_current_time():
    timezone = ZoneInfo("Asia/Ho_Chi_Minh")
    return datetime.now(timezone)