from datetime import datetime,timedelta,timezone
import time
#当前时间
now = datetime.now()
print(now)
print(type(now))
#指定日期时间（顺序年月日时分秒）
dt = datetime(2015,12,5,6,7,8)
print(dt)
#转换时间戳
print(now.timestamp())
print(dt.timestamp())
#时间戳转时间
t1 = now.timestamp()
print(datetime.fromtimestamp(t1))
print(datetime.utcfromtimestamp(t1))


#str转换为datetime
t3 = '2015-06-07 00:02:30';
t2 = datetime.strptime(t3,'%Y-%m-%d %H:%M:%S')
print(type(t2))
print(type(t3))

#datetime转化为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
#时间的加减运算

print(now+timedelta(hours=10))
print(now+timedelta(days=10))
print(now+timedelta(days=-10))

#本地时间转化为ut时间
tz_utc_6 = timezone(timedelta(hours=6))
now = datetime.now()
print(now.replace(tzinfo=tz_utc_6))

#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
t1 = now.timestamp()
now = datetime.now()
print(now.timestamp())
print(time.time())