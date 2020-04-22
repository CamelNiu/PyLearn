from datetime import datetime
import pymysql,random,time
# ALTER TABLE f_i1_iwala_trade_user PARTITION BY RANGE COLUMNS(stime)
# (
# PARTITION p20200326 VALUES LESS THAN ('2020-03-27'),
# PARTITION p20200327 VALUES LESS THAN ('2020-03-28')
# );


# pre = 'ALTER TABLE `f_i1_iwala_trade_user` PARTITION BY RANGE COLUMNS(`stime`) \n(';

# minTime = 1577808000;
# maxTime = 1588262400;

# allDay = []
# while minTime<maxTime:
#   dtt = datetime.fromtimestamp(minTime+(3600*24))
#   dtp = datetime.fromtimestamp(minTime)
#   dttFmt = dtt.strftime('%Y-%m-%d')
#   dtpFmt = dtp.strftime('%Y%m%d')
#   day = {'t':dttFmt,'p':dtpFmt}
#   allDay.append(day)
#   minTime = minTime+(3600*24)

# allParStr = ''
# for v in allDay:
#   parStr = ("PARTITION %s VALUES LESS THAN ('%s'),\n") % ('p'+v['p'],v['t'])
#   allParStr = allParStr+parStr;


# allParStr = allParStr.strip(',\n')

# sql = pre+'\n'+allParStr+'\n)'

# print(sql)





# db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","puti" )
# cursor = db.cursor()
# data = cursor.execute(sql)
# print(data)
# data = cursor.fetchall()
# print(data)



db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
cursor = db.cursor()
sqlmem = 'select member_id from iwala_member';
cursor.execute(sqlmem)
data = cursor.fetchall()

memList = []
for i in data:
  memList.append(i[0])

sqlCur = 'select currency_id from iwala_currency';
cursor.execute(sqlCur)
data = cursor.fetchall()

curList = []
for i in data:
  curList.append(i[0])


sqlBase = 'select currency_id from iwala_currency where if_base=2';
cursor.execute(sqlBase)
data = cursor.fetchall()

baseList = []
for i in data:
  baseList.append(i[0])





def getRangeTime():
  minTime = 1577808000
  maxTime = 1588262400
  randTime = random.randint(minTime,maxTime)
  date = datetime.fromtimestamp(randTime).strftime('%Y-%m-%d %H:%M:%S')
  return date

def getMemberId():

  db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
  cursor = db.cursor()
  sql = 'select member_id from iwala_member order by rand() limit 1';
  cursor.execute(sql)
  data = cursor.fetchone()
  return data[0]

def getCurrencyId():

  db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
  cursor = db.cursor()
  sql = 'select currency_id from iwala_currency order by rand() limit 1';
  cursor.execute(sql)
  data = cursor.fetchone()
  return data[0]

def getBaseCurrencyId():

  db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
  cursor = db.cursor()
  sql = 'select currency_id from iwala_currency where if_base=2 order by rand() limit 1';
  cursor.execute(sql)
  data = cursor.fetchone()
  return data[0]



def getRandOne(tmp):
  length = len(tmp)
  randKey = random.randint(0,length-1)
  return tmp[randKey]

pre = "insert into `f_i1_iwala_trade_user` (`stime`,`trade_no`,`okcoin_orderid`,`member_id`,`opposite_uid`,`currency_id`,`currency_trade_id`,`price`,`num`,`money`,`fee`,`dft_fee`,`coupon_fee`,`type`,`kind`,`add_time`,`status`,`order_id`,`usdt_value`,`is_maker`) values \n"

allValues = "";

begin = datetime.now()
print(begin)
begin = begin.timestamp()







for i in range(10000):
  time = getRangeTime()
  memberId = getRandOne(memList)
  currencyId = getRandOne(curList)
  baseId = getRandOne(baseList)
  isMaker = getRandOne([0,1])
  buytype = getRandOne(['buy','sell','buy_market','sell_market'])
  kind = getRandOne(['spot','margin'])
  value = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'),\n" % (time,'1','1',memberId,100000,currencyId,baseId,2,2,2,1,0.5,0.2,buytype,kind,'123',1,1,28,isMaker)

  allValues = allValues+value


allValues = allValues.strip(',\n')

sql = pre+allValues

putiDb = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","puti" )
cursor = putiDb.cursor()
date = cursor.execute(sql)
putiDb.commit()

end = datetime.now()
print(end)
end = end.timestamp()

print(end-begin)
