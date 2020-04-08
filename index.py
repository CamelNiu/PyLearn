class Mydict(object):
  """docstring for Mydict"""
  def __init__(self, **arg):
    super().__init__(**arg)


  def __getattr__(self,key):
    try:
      return self[key]
    except KeyError as e:
      raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
  def __setattr__(self,key,value):
    self[key] = value



s = Mydict({'wang':'lei'})
s.__setattr__('niu','shaogang')
res = s.__getattr__.niu
print(res)