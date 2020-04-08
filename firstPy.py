# # class Animal(object):
# #     def run(self):
# #         ("alimal is running...")


# # class Dog(Animal):
# #     pass

# # class Cat(Animal):
# #     pass

# # dog = Dog()


# # cat = Cat()


# # # def run_twice(Animal):
# # #   Animal.run()
# # #   Animal.run()

# # if type(dog) == type(cat) :
# #   print(1)
# # else:
# #   print(0)


# # print( isinstance(dog,Animal) )


# class Language(object):
#   """docstring for Language"""
#   def __init__(self,name, *arg):
#     super(Language, self).__init__()
#     self.arg = arg
#     self.name = name
#   def getName(self):
#     print(self.name)



# L = Language('php')
# L.getName()


# class Student(object):
#   def __init__(self,name):
#     self.name = name


# s = Student('niushaogang')

# s.love = "willa"

# print(s.name)
# print(s.love)


# class Student(object):
# #   """docstring for Student"""
# #   name = "NiuShaoGang"
# #   def __init__(self, *arg):
# #     super(Student, self).__init__()
# #     self.arg = arg



# # s = Student()
# # print(s.name)
# # s.name = 'xiaofeng'
# # print(s.name)
# # print(Student.name)
# # print(s.name)

# # #print(s.name)
# class Stu(object):
#   """docstring for Stu"""
#   count = 0
#   def __init__(self, *arg):
#     super(Stu, self).__init__()
#     Stu.arg = arg
#     Stu.count = Stu.count+1


# a = Stu()
# print(a.count)
# b = Stu()
# print(b.count)
# c = Stu()
# print(Stu.count)



# class Student(object):
#   pass

# s = Student()

# s.name = 'bob'

# print(s.name)

# def set_age(self,age):
#   self.age = age

# def test_bind_fun(self):
#     print('test bind')

# from types import MethodType

# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)

# s.test_bind_fun = MethodType(test_bind_fun,s)
# s.test_bind_fun()


# def set_score(self,score):
#     print(score)

# Student.set_score = set_score

# s.set_score(100)

# s2 = Student()

# s2.set_score(160)

# class Student(object):
#   """docstring for Student"""
#   __slots__ = ('name','age')


# s = Student()

# s.name = 'bob'
# print(s.name)
# s.age = '20'
# print(s.age)
# s.score = 2
# print(s.score)


# class Student(object):
#   """docstring for Student"""
#   def get_score(self):
#     print(self._score)

#   def set_score(self,value):
#     if not isinstance(value,int):
#       raise ValueError('score must be an integer')
#     if value<0 or value >100:
#       raise ValueError('score must be 0-100')
#     self._score = value


# s = Student()
# s.set_score(98)
# s.get_score()
