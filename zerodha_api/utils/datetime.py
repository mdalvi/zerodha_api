from datetime import datetime

import pytz
from pytz import timezone


def get_date_now(time_zone):
    timezone_ = timezone(time_zone)
    utc_ = datetime.utcnow()
    utc_pytz = datetime(
        utc_.year,
        utc_.month,
        utc_.day,
        utc_.hour,
        utc_.minute,
        utc_.second,
        tzinfo=pytz.utc,
    )
    return utc_pytz.astimezone(timezone_).date()
