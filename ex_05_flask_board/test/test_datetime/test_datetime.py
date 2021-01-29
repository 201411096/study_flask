import datetime
from pytz import utc, timezone
from pytz import all_timezones

# pytz.all_timezones
# pytz가 제공하는 시간대 식별자 
for tz in all_timezones: 
    print(tz)

# naive datetime 과 aware datetime
# naive datetime은 날짜와 시각만을 갖습니다.
# naive datetime과 달리 aware datetime은 시간대 정보(tzinfo) 도 갖습니다.

KST = timezone('Asia/Seoul')

# utc 기준 naive datetime
now1 = datetime.datetime.utcnow()
print('now1 : ', now1)

# utc 기준 aware datetime
now2 =utc.localize(now1)
print('now2 : ', now2)

# utc 시각, 시간대만 KST
now3 = KST.localize(now1)
print('now3 : ', now3)

# KST 기준 aware datetime
now4 = utc.localize(now1).astimezone(KST)
print('now4 : ', now4)

# 출력 예시
# now1 :  2021-01-29 08:55:21.095828
# now2 :  2021-01-29 08:55:21.095828+00:00
# now3 :  2021-01-29 08:55:21.095828+09:00
# now4 :  2021-01-29 17:55:21.095828+09:00