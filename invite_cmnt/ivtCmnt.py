from datetime import datetime
import pymysql,random,time

def getMemberId(sta,end):
  db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
  cursor = db.cursor()
  sta = time.strptime(sta, "%Y-%m-%d %H:%M:%S")
  sta = int(time.mktime(sta))

  end = time.strptime(end, "%Y-%m-%d %H:%M:%S")
  end = int(time.mktime(end))

  sql = "update iwala_user_invite set create_time=floor(%s+((%s-%s)*rand()))" % (sta,end,sta);

  res = cursor.execute(sql)
  s = db.commit()
  if res:
    return True
  else:
    return False





mem = getMemberId('2020-04-01 00:00:00','2020-06-01 00:00:00');

print(mem);