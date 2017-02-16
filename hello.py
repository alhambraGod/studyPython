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
dict = {'111':10, '222':50, '333':80}
print(dict['222'])
#print(dict['sdsdfsdf']) # error
key = 'error'
if (key in dict):
  print(dict[key])
else:
  print("key not in dict: ", key)
  
if (dict.get(key)):
  print(dict[key])
else:
  print("key not get(): ", key)

print('len(dict): ', len(dict))
dict.pop('222')
print('len(dict): ', len(dict))

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
exit()
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
now()
log(now)()
log(log(now))()
log(log(print))()

print(log)
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

# ConvertUnixTime().convert([1340159970])
# ConvertUnixTime().convert()
# exit()
