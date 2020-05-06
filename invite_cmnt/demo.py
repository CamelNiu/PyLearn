from datetime import datetime
import pymysql,random,time

class setShowUid:
  """docstring for setShowUid"""
  cursor=""
  db = ""

  def __init__(self):
    self.db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
    self.cursor = self.db.cursor()

  def getShowUid(self,uid):
    if len(uid) != 6 :
      return 'Error'
    randomStr = str(random.randint(100,999))
    showUid = uid[0:3]+randomStr+uid[3:]
    return int(showUid)

  def getMemIds(self):
    sql = "select member_id from iwala_member"
    self.cursor.execute(sql)
    memdata = self.cursor.fetchall()
    memIds = []
    for i in memdata:
      memIds.append(i[0])
    memIds = tuple(memIds)
    return memIds


  def opreateDb(self):
    memIds = self.getMemIds()
    try:
      res = []
      for i in memIds :
        showUid = self.getShowUid(str(i))
        sql = "update `iwala_member` set `show_uid` = '"+str(showUid)+"' where `member_id` = '"+str(i)+"'"
        self.cursor.execute(sql)
      self.db.commit()
      print('Success')
    except:
      self.db.rollback()
      print('Error')



class ivtUserData:
  """docstring for ivtUserData"""
  db = ""
  cursor = ""


  def __init__(self):
    self.db = pymysql.connect("10.100.0.81","shuzibi","YjExOGQzMDhkYzZmOWRlNjU5","shuzibi" )
    self.cursor = self.db.cursor()


  def clearIvtUser(self):
    sql = "truncate table iwala_user_invite"
    try:
      self.cursor.execute(sql)
      self.db.commit()
      print('Success')
    except Exception as e:
      self.db.rollback()
      print('Error')


  def mysqlSelResToList(self,res):
    listRes = []
    for i in res:
      listRes.append(i[0])
    return tuple(listRes)


  def randomGetMemId(self,num=20):
    sql = "select member_id from iwala_member where member_id<=300000 order by rand() limit "+str(num)
    self.cursor.execute(sql)
    data = self.cursor.fetchall()
    data = self.mysqlSelResToList(data)
    return data

  def randomGetMemIdNotId(self,memId,num=20):
    sql = "select member_id from iwala_member where member_id <> "+str(memId)+" order by rand() limit "+str(num)
    self.cursor.execute(sql)
    data = self.cursor.fetchall()
    data = self.mysqlSelResToList(data)
    return data

  def getDictData(self):
    data = self.randomGetMemId(18)
    dictData = {}
    for i in data:
      dictData[i] = self.randomGetMemIdNotId(i,random.randint(1,20))
    return dictData

  def insertDb(self):
    data = self.randomGetMemId(30);

    for i in range(7270):
      j = i+1
      key = random.randint(0,29)
      memId = data[key]
      sql = "update iwala_user_invite set member_id = %s where id = %s" % (str(memId),str(j))

      self.cursor.execute(sql)
      self.db.commit()



iud = ivtUserData()

iud.insertDb()