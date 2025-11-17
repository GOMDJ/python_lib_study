#datatime : 날짜, 시간
#time : 시스템 시간, 타이머, sleep
from datetime import datetime, timedelta, date, time

now = datetime.now()    #현재 시각
print(now)

# 년, 월, 일, 시, 분, 초 따로 접근
print(now.year)    # 2025
print(now.month)   # 11
print(now.day)     # 13
print(now.hour)    # 15
print(now.minute)  # 30
print(now.second)  # 45

#특정 날짜/시간 만들기
dt = datetime(2024, 12, 25, 18, 30, 0)
print(dt)
day = date(2024, 12, 25)
print(day)

#날짜 계산(timedelta)
future = now + timedelta(days = 3)  #weeks, minutes도 가능
past = now - timedelta(hours = 2)
diff = future - past
print(future)
print(past)
print(diff)

#문자열 변환(strftime)
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))

date_str = "2024-12-25 18:30:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt)

"""
print(now.strftime("%Y-%m-%d"))에선 now라는 객체가 생성되었기 때문에 datetime.을 안 붙여도된다.
하지만 dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") 객체가 생성되지 않았기 때문에 datetime.을 붙여야함.
"""