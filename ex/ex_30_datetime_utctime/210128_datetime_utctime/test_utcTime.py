import datetime
from pytz import utc, timezone
from pytz import all_timezones

def getCurrentDateTime():
    currentUtcNaiveTime = datetime.datetime.utcnow()
    return utc.localize(currentUtcNaiveTime)

def convertUtcTimeToLocalTime(dt, **kwargs):
    targetTimezone = None
    if kwargs.get('timezone', None) is None:
        targetTimezone = timezone('Asia/Seoul')
    if dt.tzinfo is None:
        return utc.localize(dt).astimezone(targetTimezone)
    else:
        return dt.astimezone(targetTimezone)

utcCurrentTime = getCurrentDateTime()
currentLocalTime = convertUtcTimeToLocalTime(utcCurrentTime)
print('utcCurrentTime : ', utcCurrentTime)
print('localTime : ', currentLocalTime)
print('localTime :', convertUtcTimeToLocalTime( datetime.datetime(2021, 1, 1, 12, 0, 0) ))