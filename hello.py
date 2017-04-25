# -*- coding: utf-8 -*-
# ###########################################
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。######### input & output ##################
print('hello')
print('I','am,','luke')
print('I\'m "ok"')
print('''line 1
line2
   line3
''')
print(35,'0x334')
print(True)
print(-3>0)
print(not (-3>0))
print(0/3)  # output 0.0
print(3/1)  # output 3.0, still float

print('test:', 1.23e9)
print('ok:', 123e99)  # output: inf: 1.23e+101
# good number
print('inf:', 123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789)
print('repeat' * 5)


# a string is constant, replace() returns a new object but not change current object
str1 = 'abc'
print(str1)
str1.replace('a', 'A')
print(str1)

str1 = str1.replace('a', 'A')
print(str1)
 
print('\n')
###########################################

###########################################
var = 'luke'
print(var)
var = 3
print(var)
# print(var = 123) #error
###########################################

###########################################
# character coding
print('蔡经伟')
print(ord('蔡'))
print(chr(66))
print(chr(34081), chr(34082), )
print('\u4e2d\u6587')

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('unicode')) #error
#>>> b'ABC'.decode('ascii')
#'ABC'
#>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#'中文'

print(len('中文'.encode('utf-8')))  # 6
print('中文'.encode('utf-8'))
print(len('中文'))                  # 2
###########################################

###########################################
s1=72
s2=85
print('upgrade %.2f%%' % (((s2 - s1) / s1) * 100))
###########################################


#if int(input()) > 1 :
#  print('>1')
#else: print('<=1')

print('\n')

###########################################
######### list & tuple ##################
classmates= ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])                 
print(classmates[1])
print(classmates[-2]) # good
#print(classmates[4])  # out of range

classmates.pop(1)
classmates.append('new end')
classmates.insert(1, '1111')
print(classmates)


all = ['start', classmates, 567, 'énd']
print(len(all))
print(all)

tuple1 = ('t1', 't2', 'end')
print(tuple1)
tuple1 = (1)  # not tuple, int 1
print(tuple1)
tuple1 = (1,)  # add comma for a 1-element tuple
print(tuple1)

tuple2 = ('1', '2', ['A', 'B'], 'end') 
print(tuple2)
tuple2[2][1] = 'X'
print(tuple2)
print('\n')


print('----------- dict ---------------')
ddd = {'111':10, '222':50, '333':80}
print(ddd['222'])
#print(dict['sdsdfsdf']) # error
key = 'error'
if (key in ddd):
  print(ddd[key])
else:
  print("key not in dict: ", key)
  
if (ddd.get(key)):
  print(ddd[key])
else:
  print("key not get(): ", key)

print('len(dict): ', len(ddd))
ddd.pop('222')
print('len(dict): ', len(ddd))

print('----------- set ---------------')
set1  = set([1, 2, 2, 5, 9, 6, 6, 3, 3])
set2 = set([1, 2, 2, 5, 9, 6, 6, 3, 3])
print(set1)
for ele in set1:
  print(ele)
#print(set[1])  # not support indexing
set1.add(100)
set1.add(100)
set1.remove(5)
print(set1)

print('set1 & set2', set1 & set2)
print('set1 | set2', set1 | set2)

print('----------- set: end ---------------')


###########################################

###########################################
array = ('1', '2', ['A', 'B'], 'end')
for ele in array:
  print(ele)

total1 = 0
n = 1
while n <= 100:
  total1 += n
  n += 1
  if n > 90:
    break
print('total: ', total1)

###########################################

###########################################
n1 = 255
n2 = 1024
print(hex(n1))
hhh = hex
print(hhh(n2))
help(hhh) # print help()

from function import *
print(my_abs(-10))
print(my_abs('string'))

eee = empty
print(eee('2324'))

print(nop())

print(return_two(5, 10))  # return a tuple

###########################################
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
print(power(5))
print(power(5))
print(power(5, 3))
print(power(5, 100))


from function import bad_add_end
from function import good_add_end
print(bad_add_end())
print(bad_add_end())
print(bad_add_end())
print(good_add_end())
print(good_add_end())

#from function import calc_power_list
# from function import calc_power_var
import function
print(function.calc_power_list([1, 2, 3]))
print(function.calc_power_var(1, 2, 3))

from function import *
keyword_parameters('111', 111)
keyword_parameters('222', 222, city='beijing')
keyword_parameters('222', 222, city='beijing', rich='$100')
extra={'city':'gz', 'money':'5000'}
keyword_parameters('333', 333, city=extra['city'])
keyword_parameters('444', 444, **extra)

from function import keyword_named_parameters
keyword_named_parameters('111', 111, city='named city', money='5555')

###########################################
# slice
l1 = list(range(100))
print(l1[0:3])
print(l1[:3])
print(l1[2:5])
print(l1[:5])
print(l1[:-5])

print(l1[7:5])   # []
print(l1[-1:5])  # []
print(l1[0:0])   # []
print(l1[:0])    # []
print(l1[0:])    # [0, 1, ....., 99]
print(l1[:])     # [0, 1, ....., 99]
#print(list[])     # invalid syntax

print(l1[1])      # 1
print(l1[1:2])    # [1]
print(l1[:1])     # [0]
print(l1[-1])     # 99
print(l1[-1:])    # [99]
print(l1[99:])    # [99]

print(l1[-1:-3]) # []
print(l1[-3:0])  # []
print(l1[-3:3])  # []
print(l1[-3:-1])
print(l1[2:-3])
print(l1[5:])
print(l1[-5:])

print(l1[100:])    # []
print(l1[101:])    # []
print(l1[2222:])    # []
print(l1[2222:3333])    # []
print(l1[:3333])    # [0, 1, ....., 99]
print(l1[-100:])    # [0, 1, ....., 99]
print(l1[-1001:])   # [0, 1, ....., 99]
#print(list[-1001])  # index out of range
print(l1[:-1001])   # []
print(l1[-1111:2])  # [0, 1]
print(l1[-1111:-1111])  # []
print(l1[-1111:0])   # []

# print(list[::0])  # ValueError: slice step cannot be zero
print(l1[::1000])  # [0]
print(l1[::5])  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
print(l1[::-5]) # [99, 94, 89, 84, 79, 74, 69, 64, 59, 54, 49, 44, 39, 34, 29, 24, 19, 14, 9, 4]

print('123456789')
print('123456789'[:])
print('123456789'[2:5])
print('123456789'[::3])
print('123456789'[::-3])

###########################################
import sys
from sys import argv
if (len(sys.argv) == 1):
  print('hello, world')
else:
  print('hello: ', argv[1])

from PIL import Image
# image = Image.open('1.png')
# imageFileName = r'D:\install\python\study'
# imageFileName = r'D:\install\python\study\1.png'
imageFileName = r'D:\install\python\study\notexist.png'
image = None
try:
    image = Image.open(imageFileName)
except FileNotFoundError:
    print('Fail to find the file: ', imageFileName)
except PermissionError:
    print('Permission error: ', imageFileName)
except Exception:
    print('Exception error: ', imageFileName)
if (image != None):
    image.thumbnail((200, 200))
    image.save('thumb.jpg', 'JPEG')
    # image.rotate(45).show()


class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('A.__private()')

    def public(self):
        print('A.public()')


class B(A):
    def __private(self):
        print('B.__private()')

    def public(self):
        print('B.public()')

print('=========================')
a = A()  # 实例化对象a
b = B()  # 实例化对象b
# print(a.__private())  # 这里会报错,说 AttributeError: 'a' object has no attribute '__private'
# print(b.__private())  # 这里会报错,说 AttributeError: 'B' object has no attribute '__private'
# print
b._A__private()  # 因为私有变量轧压机制,__private方法变成_A__private()
print(dir(b))  # 通过自省方法dir(),查看b所具有的属性
print('=========================')

###########################################

# for, isinstance
l = list(range(100))
for i, value in enumerate(l[:4]):
    print(i, value)

d = {'a':1, 'b':2, 'c':3}
for key in d:  # default: same as keys()
    print(key)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k, v)

from collections import Iterable
print(isinstance("abc", Iterable))
print(isinstance(123, Iterable))
print(isinstance(l, Iterable))

# list comprehensions
l = [x * 2 + 1 for x in range(3)]
print(l)
l = [x * x for x in range(10) if x % 3 == 0]
print(l)
l = [k + str(v) for k, v in d.items()]
print(l)
l = [ch.upper() for ch in d.keys()]
print(l)

# generator
gen = (x * x for x in range(10) if x % 3 == 0)
print(gen)
print(next(gen))
print(next(gen))
print("for value in gen:")
for value in gen:
    print(value)

print(fib(10))
print('call generator')
gen = fib_generator(6)
while True:
    try:
        # print(next(fib_generator(6)))     # error: endless loop
        print(next(gen))
    except StopIteration as e:
        print("fib_generator() ends and returns:", e.value)
        break

for value in output_yanghui_triangle():
    if value >= 10:
        break

for value in output_yanghui_triangle2():
    if value >= 10:
        break
###########################################
print('test: now()')
now()
print('test: log(now)()')
log(now)()
print('test: log(log(now))()')
log(log(now))()

# print('test: log(print)()')
# log(print('print called'))()
# AttributeError: 'NoneType' object has no attribute '__name__'

print("test: log(print)('called print')")
log(print)('called print')

print('test: log(print)()')
log(print)()

print('test: log(log(print))()')
log(log(print))()

print('test: print(log)')
print(log)
print('test: print(log(now))')
print(log(now))

log(log)(now)

log(log)(now)()

###########################################
s = Solution()
s.plusOne([1,2,3])
s.plusOne([])
s.plusOne([0])
s.plusOne([1,2,9])
s.plusOne([9])
s.plusOne([9,9])

# even system function can be changed
# abs = print
# abs(10)
from function import *
print(higher_order_func(5, -5, abs))
print(higher_order_func(5, -5, calc_power_var))
# print(higher_order_func(5, -5, now)) # error

r = map(abs, [1, -1, 2, -2])
print(r)
r = map(abs, range(-8, 9))
print(list(r)) # list receives an iterator

from functools import reduce
r = reduce(add, [1, 2, 3, 4])
print(r)
print(factorial(1))
print(factorial(1, 2, 3))
print(factorial([1, 2, 3]))
print(factorial(range(4)))
print(factorial(list(range(4))))
# TypeError: unsupported operand type(s) for *: 'int' and 'range'
# print(factorial(1, range(4)))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, range(1, 6)))

r = test_reduce_normalize(['adam', 'LISA', 'barT'])
print(list(r))

print(prod([2, 3, 4, 5]))
print(str2float('123.456'))
print(str2float('1.456'))
print(str2float('0.456'))
print(str2float('10.4500'))

###########################################
t = TestSelf()
t.prt()
t.x



###########################################
# sorted
from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, reverse = True))  # ?? how to sort?
print(sorted(L, key = lambda x : x[0]))
print(sorted(L, key = itemgetter(0)))


# ======================================
# closure
print('closure test')
def count():
    funcArray= []
    for i in range(1, 4):
        def func():
            return i * i
        funcArray.append(func)
    return funcArray

funcArray = count()
for func in funcArray:
    print(func())

def count2():
    funcArray= []

    for i in range(1, 4):
        def func():
            j = i
            return j * j
        funcArray.append(func)
    return funcArray

funcArray = count2()
for func in funcArray:
    print(func, func())

import functools
int2 = functools.partial(int, base = 2)
print(int2('1011'))
int16 = functools.partial(int, base = 16)
print(int16('1AC'))
print(int16('1001', base = 2))  # can still override 16 as 2
max10 = functools.partial(max, 10)  # 10 is added to the end of parameter list
print(max10(5, 6))
print(max10(5, 6, 12))

######################################################
# static class member
class a():
    num = 0

obj1 = a()
obj2 = a()
print(obj1.num, obj2.num, a.num, obj1.num is obj2.num, obj1.num is a.num, obj2.num is a.num)

obj1.num += 1
print(obj1.num, obj2.num, a.num, obj1.num is obj2.num, obj1.num is a.num, obj2.num is a.num)

a.num += 2
print(obj1.num, obj2.num, a.num, obj1.num is obj2.num, obj1.num is a.num, obj2.num is a.num)

obj2.num += 1
print(obj1.num, obj2.num, a.num, obj1.num is obj2.num, obj1.num is a.num, obj2.num is a.num)

# for a class member, after using self.member, will create a new instance other than class.member
# 0 0 0 True True True
# 1 0 0 False False True
# 1 2 2 False False True
# 1 3 2 False False False
######################################################

######################################################
# default parameter value of function: only INIT ONCE
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
print(f(4, ['x']))
print(f(5))
# [1]
# [1, 2]
# [1, 2, 3]
# ['x', 4]
# [1, 2, 3, 5]


################# test bit operation ###################
a = 9
b = 3
#    1001
#      11
# ^: 1010   4 bits
# &:    1   4 bits
# |: 1011   4 bits
print(bin(a), bin(b))
print(bin(a ^ b))
print(bin(a & b))
print(bin(a | b))

def bit_add(a, b):
    if (b == 0):
        return a
    sum = a ^ b
    carry = (a & b) << 1
    return bit_add(sum, carry)

print(bit_add(int('1011', base = 2), 3))

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print('<h1>Hello, web! Time: %s</h1>' % t)

print('########### types, static method, class method ###########')
import types
def fn():
    pass

print(type(fn))
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(abs)==types.BuiltinMethodType)
print(type(lambda x : x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)
print(dir(types))
print(dir(time))
class Animal:
    def run(self):
        print('Animal run...')

class Dog(Animal):
    def run(self):
        print('Dog run...')
    def __len__(self):
        print("Dog's len is 100")
        return 100

    @classmethod
    def class_method(cls):
        print('class_method: ', cls)

    @staticmethod
    def static_method():
        print('static_method')

class DuckType:  # duck type, not child class of Animal
    def run(self):
        print('DuckType run...')

def test_duck_type(duck):
    duck.run()

test_duck_type(Animal())
test_duck_type(Dog())
test_duck_type(DuckType())
print('isinstance(Dog, Animal): ', isinstance(Dog, Animal))
print('isinstance(Dog(), Animal()): ', isinstance(Dog(), Animal))
print('isinstance(DuckType, Animal): ', isinstance(DuckType(), Animal))
print('len(Dog()): ', len(Dog()))
dog = Dog()
print('Dog.class_method(): ', Dog.class_method())
print('dog.class_method(): ', dog.class_method())
print('Dog.static_method(): ', Dog.static_method())
print('dog.static_method(): ', dog.static_method())
print(hasattr(Dog, '__init__'))
print(hasattr(Dog, 'run'))
print(hasattr(Dog, '__len__'))
print(hasattr(Dog, 'class_method'))
print(hasattr(Dog, 'static_method'))
print(hasattr(dog, '__init__'))
print(hasattr(dog, 'run'))
print(hasattr(dog, '__len__'))
print(hasattr(dog, 'class_method'))
print(hasattr(dog, 'static_method'))
l = getattr(dog, '__len__')
l()
del dog
l()  # still valid. only name of dog is invalid, "dog object" is still valid
# error when run following line: NameError: name 'dog' is not defined
# s = getattr(dog, 'static_method')
s = getattr(Dog, 'static_method')
s()

dog = Dog()
dog.run()
Dog.run(dog)
Dog.__len__(dog)
# Dog.len(dog)  # AttributeError: type object 'Dog' has no attribute 'len'
print('########### END: types, static method, class method ###########')

print('########### START: __slots__ ###########')
class TestSlots(object):
    pass

t = TestSlots()
t.name = 'snake'
print(t.name)
from types import MethodType
def bind_method(self, n):
    print('bind_method: ', n)
    self.name = 'bind'

bind_method(t, 100)
t.bind = MethodType(bind_method, t)
t.bind(200)
print('t.name', t.name)
t2 = TestSlots()
# binded method not valid for other object instances
# t2.bind() # AttributeError: 'TestSlots' object has no attribute 'bind'
# should bind to the class, then all instances have the binded method
TestSlots.bind = bind_method
t.bind(500)
t2.bind(600)

class TestSlots():
    # limit the members
    __slots__ = ('name', 'age')
    pass

t = TestSlots()
t.name = 'luke'
print(t.name)
# ERROR: __slots__ does not includ score
# AttributeError: 'TestSlots' object has no attribute 'score'
# t.score = 300
# print(t.score)
# ERROR: object can not bind method, either
# t.bind = MethodType(bind_method, t)
# t.bind()
# GOOD: __slots__ only limits object instance's members, not class
TestSlots.score = 'score'
print(t.score)

# child class is not limited by parent class' __slots__
class TestSlotsChild(TestSlots):
    pass

tchild = TestSlotsChild()
tchild.score = 300
print(tchild.score)

print('########### END: __slots__ ###########')

print('########### START: @property ###########')
class TestProperty():
    @property
    def score(self):
        return self._score

    # @property # AttributeError: can't set attribute
    @score.setter
    def score(self, s):
        if (not isinstance(s, int)):
            raise ValueError('Must be integer')
        if (s < 0 or s > 100):
            raise ValueError('Must be [0, 100]')
        self._score = s

    def __init__(self, v):
        self._age = v

    # read-only property, not proper.setter
    @property
    def age(self):
        return self._age

t = TestProperty(66)
print(t.age)
try:
    t.score = 50
    print(t.score)
    t.score = -1
except ValueError as e:
    print('Caught error: ', e)

try:
    t.score = 50
    print(t.score)
    t.score = 200
    print(t.score)
except ValueError as e:
    print('Caught error: ', e)

print('########### END: @property ###########')

print('########### START: customized class:  ###########')
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
class Chain():
    def __init__(self, path = ''):
        self.path = 'luke'
        if (path != ''):
            self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))
    def __str__(self):
        return self.path

    def __call__(self, *args, **kwargs):
        print('Call self. path: %s' % self.path)
    __repr__ = __str__

# simulate restful API calls
print(Chain().user.status.list)
c = Chain()
c()  # use class object as function
print('callable(c): ', callable(c))
print('callable(Chain): ', callable(Chain))
print('########### END: customized class:  ###########')

print('########### START: enum ###########')
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar'))
for name, member in Month.__members__.items():
    print(name, ' -> ', member, ', ', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 8
    Fri = 9
    Sat = 5
    # Sat = 10  # with @unique, TypeError: Attempted to reuse key: 'Sat'

day1 = Weekday.Sat
print(day1)
print(day1.Mon)
print(day1.value)
print(Weekday['Tue'])
print(Weekday.Tue)
print(Weekday(8)) # Thu
print(day1 == Weekday(5))
for name, member in Weekday.__members__.items():
    print(name, ' -> ', member, ', ', member.value)
print('########### END: enum ###########')

print('########### START: meta class ###########')
def meta_fn(self, name = 'world'):
    print('hello, ', name)

# Hello = type('Hello', (object, ), dict(hello = meta_fn))
# TypeError: 'dict' object is not callable
Hello = type('Hello', (object, ), {'hello':meta_fn})
h = Hello()
h.hello()

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass
l = MyList()
l.add(1)
l.add(5)
print(l)

class MyListBase:
    def add(self, value):
        self.append(value)

class MyList(list, MyListBase):
    pass
l = MyList()
l.add(1)
l.add(5)
print(l)

print('########### END: meta class  ###########')

print('########### START: exception, assert ###########')
import logging
# note:
# logging.basicConfig(level=logging.INFO)
# debug，info，warning，error

class FooError(ValueError):
    pass

try:
    raise FooError(5)
except BaseException as e:
    print(e)
    logging.exception(e)
finally:
    print('finally of exception')

import pdb
############################################
# 1)following code will auto pause when run with
#   'python hello.py'
# 2) python -m pdb hello.py
# pdb commands: l (list code), n (step over), p (see variable), q (quit)
# pdb.set_trace()

print('test assert')
try:
    print("assert((1 < 0), 'assertion: 1 < 0')")
    # following code NO assertion failure:
    # actually assert a tuple
    assert((1 < 0), 'assertion: 1 < 0')

    print("assert  1 < 0, 'assertion: 1 < 0'")
    assert  1 < 0, 'assertion: 1 < 0'
except BaseException as e:
    print(e)
finally:
    print('finally of exception')

print('########### END: exception, assert ###########')

print('########### START: file I/O ###########')
print('test: file IO')
with open('./elsie.html') as f:
    lines = f.readlines()
i = 0
while (i < len(lines)):
    if ((i % 2) == 0):
        print(lines[i].strip())
    # print(lines[i])
    i += 1

from io import StringIO, BytesIO, SEEK_SET, SEEK_END
print('test: StringIO')
f = StringIO('start')
print(f.getvalue())
print(f.tell())
f.seek(SEEK_END)
print(f.tell())
f.write('hello\n')
f.writelines(['line1', 'line2', 'end'])
print(f.getvalue())

f.seek(SEEK_SET)
lines = f.readlines()
print(lines)


print('########### END: file I/O ###########')


print('########### START: handle file and dir ###########')
import os
# import shutil

# shutil.copy()

# os.remove(), os.rename(), os.join(), os.split()
# NOT support in Windows
# AttributeError: module 'os' has no attribute 'uname'
# print(os.uname())
print(os.name)

# list all files
print([x for x in os.listdir('.') if os.path.isdir(x)])
# list .py files
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
print('########### END: handle file and dir ###########')

print('########### START: pickle ###########')
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open(r'D:\temp\python_dump.txt', 'wb')
f.write(pickle.dumps(d))
# pickle.dump((d, f))
f.close()

f = open(r'D:\temp\python_dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

import json
print(json.dumps(d))

# every class has a __dict__ property to store instance variable
# except the class which defines __slots__
# json.loads() restores a dict object, and then object_hook()
# can convert this dict object to class instance
class TestPickle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('TestPickle run...')

    @staticmethod
    def toDict(std):
        return {'name':std.name, 'age': std.age}

    @staticmethod
    def fromDict(std):
        return TestPickle(std['name'], std['age'])

t = TestPickle('pickle', 55)
# TypeError: <hello.TestPickle object at 0x000001A86C9C4E80> is not JSON serializable
# print(json.dumps(t))
print(json.dumps(t, default=TestPickle.toDict))

json_str = '{"age": 20, "name": "Bob"}'
t = json.loads(json_str, object_hook=TestPickle.fromDict)
print(t.name, t.age)

str = json.dumps(t, default=lambda obj:obj.__dict__)
print(str)
t2 = json.loads(json_str, object_hook=TestPickle.fromDict)
print(t2.name, t2.age)

print('########### END: pickle ###########')

def TestTCPSocket():
    print('########### START: TCP socket ###########')
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.sina.com.cn', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # receive data
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open(r'd:\temp\python_sina.html', 'wb') as f:
        f.write(html)
    print('########### END: TCP socket ###########')
######################################################

# exit()

import threading

WAIT_INPUT = 8
hasInput = False
counter = 0

def timer_exit():
    while True:
        global counter
        time.sleep(1)
        counter += 1
        # print("counter： ", counter)
        if (counter >= WAIT_INPUT) and (not hasInput):
            print('\nNO INPUT. Exit')
            # exit()  # only exit current thread
            # threading.main_thread().exit()  # error code
            from os import _exit
            _exit(0)  # exit the process

threadExit = threading.Thread(target=timer_exit)
threadExit.setDaemon(True)
threadExit.start()

while True:
    hasInput = False
    counter = 0

    print('''
    0  --- reset input timer
    1  --- parse web links
    2  --- convert unix time
    3  --- web browser (mechanicalsoup)
    ''')
    # item = input('Please select menu item (%ds):' % WAIT_INPUT)
    item = 6  # <0 indicate exit()
    item = int(item)

    hasInput = True
    if item == 0:
        print('input to reset timer')
    elif (item == 1):
        from parse_links import parse_links_test
        parse_links_test()
    elif item == 2:
        # convert UNIX time in excel file
        ConvertUnixTime().convert([1340159970])
        ConvertUnixTime().convert()
    elif item == 3:
        from webBrowser import test_web_browser
        test_web_browser()
    elif item == 4:
        TestTCPSocket()
    elif item == 5:
        from SendMail import  sendMail

        sendMail()
    elif item == 6:
        from TestSqlLite import testSqlLite

        testSqlLite()
    else:
        exit()
    break


######################################################
