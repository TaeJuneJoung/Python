import time

now = time.gmtime(time.time())
#우리나라[한국] 시간이 아님 - 국제표준시(UTC)
print(f'{now.tm_year}/{now.tm_mon}/{now.tm_mday}')


from datetime import date
'''
#특정날짜 객체 생성
: date(년, 월, 일)

#현재 날짜 객체 생성
: date.today()
'''
now = date.today()
print(f'{now.year}/{now.month}/{now.day}')

from datetime import time
#시간을 나타낼 때 사용

from datetime import datetime
#date일 때와는 다르게 시간까지 나타내줌
now = datetime.now()

print(f'{now.year:04}/{now.month:02}/{now.day:02}')

print(now.strftime('%Y/%m/%d'))