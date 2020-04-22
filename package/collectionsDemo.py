from collections import namedtuple,defaultdict,OrderedDict
#namedtuple -> tuple变为对象，可以属性访问
p = (1,2)
point = namedtuple('point',['x','y'])
p = point(1,2)
l = point(4,5)
print(p.x)
print(p.y)
print(l.x)
print(l.y)
print(isinstance(l,tuple))
print(isinstance(l,point))

cycle = namedtuple('cycle',['x','y','r'])
b = cycle(1,2,5)
print(b.x)
print(b.y)
print(b.r)

#defaultdict 访问字典不存在的key时，返回值



d = {'a':'b','c':'d'}

d = defaultdict(lambda:'abcdefg')

print(d['e'])

#OrderedDict(字典排序)

e = dict([('a',1),('b',2),('c',3)])

oe = OrderedDict([('a',1),('b',2),('c',3)])

print(e)
print(oe['a'])


od = OrderedDict()

od['x'] = 1
od['y'] = 2
od['z'] = 3

print(list(od.keys()))

