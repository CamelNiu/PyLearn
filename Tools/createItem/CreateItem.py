import os

class CreateWeb(object):
  """docstring for CreateWeb"""
  #固定的目录结构
  dirList = {'root':('backup','conf','dist','www','ios','LICENSE'),'www':{'static':'static','templates':'templates'}}

  def __init__(self,path="",name="pyWeb"):
    if path == "":
      path = os.path.abspath('.')
    self.path = path
    self.name = name
    self.realPath = os.path.join(path,name)


  def createDir(self,dirname,preDir="",ifFile=1):
    if dirname.strip() == "":
      raise Exception("dirname is empty")

    if preDir.strip() == "":
      realPath = self.realPath
    else:
      realPath = preDir
    finalDir = os.path.join(realPath,dirname)



    if os.path.exists(finalDir):
      return finalDir
    os.makedirs(finalDir)
    return finalDir

  def createItem(self):
    for key,value in self.dirList.items():
      if key == 'root':
        for rootName in value:
          self.createDir(rootName)
      else:
        curDir = self.createDir(key)
        for nextName in value:
          self.createDir(nextName,curDir)



