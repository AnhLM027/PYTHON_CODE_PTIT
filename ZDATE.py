import datetime
from datetime import date, time, datetime, timedelta
import calendar

# today = date.today()        # chỉ ngày (YYYY-MM-DD)
# now = datetime.now()        # ngày + giờ hiện tại
# utc_now = datetime.utcnow() # giờ UTC

d = date(2025, 11, 22)            # năm, tháng, ngày
t = time(14, 30, 0)               # giờ, phút, giây
dt = datetime(2025, 11, 22, 14, 30, 0)

d.year, d.month, d.day
t.hour, t.minute, t.second
dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second

d = date(2025, 11, 22)
s = d.strftime("%Y-%m-%d")       # '2025-11-22'
s2 = d.strftime("%d/%m/%Y")      # '22/11/2025'
s3 = d.strftime("%A, %d %B %Y")  # 'Saturday, 22 November 2025'

# %Y – 4 chữ số năm
# %y – 2 chữ số năm
# %m – tháng 01-12
# %d – ngày 01-31
# %H – giờ 00-23
# %M – phút 00-59
# %S – giây 00-59
# %A – tên thứ trong tuần
# %B – tên tháng đầy đủ

dt = datetime.strptime("22-11-2025", "%d-%m-%Y")
dt2 = datetime.strptime("2025/11/22 14:30:00", "%Y/%m/%d %H:%M:%S")



d1 = date(2025, 11, 22)
d2 = d1 + timedelta(days=5)   # cộng 5 ngày
d3 = d1 - timedelta(weeks=2)  # trừ 2 tuần

delta = d3 - d1               # trả về timedelta
print(delta.days)             # số ngày



d = date(2025, 11, 22)
d.weekday()    # 0 = Monday, 6 = Sunday
d.isoweekday() # 1 = Monday, 7 = Sunday



import calendar
calendar.monthrange(2025, 11) # (weekday_of_first_day, num_days)
calendar.isleap(2024)         # True nếu năm nhuận
calendar.month_name[11]       # 'November'


d1 = date(2025,11,22)
d2 = date(2025,11,25)

d2 > d1  # True
d2 == d1 # False
d2 != d1 # True
