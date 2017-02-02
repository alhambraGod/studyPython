# -*- coding: utf-8 -*-
###########################################

def my_abs(x):
  if not isinstance(x, (int)):
    return TypeError('should be int')
  if x >= 0:
    return x
  else:
    return -x
    
def return_none(x):
  return
  
def empty(x):
  return None
  
def nop():
  pass
  
def return_two(x, y):
  return 2 * x, 2 * y

# this function will be replaced by def power(x, n = 2):
def power(x):
    return x * 100

def power(x, n = 2):
    ret = x
    while n > 1:
        ret *= x
        n -= 1
    return ret

def bad_add_end(p = []):
    p.append('end')  # p will be changed every call with default parameter
    return p

def good_add_end(p = None):
    if p is None:
        p = []
    p.append('end')
    return p

def calc_power_list(numbers):
    ret = 0;
    for n in numbers:
        ret += n * n
    return ret

def calc_power_var(*numbers):
    ret = 0;
    for n in numbers:
        ret += n * n
    return ret

def keyword_parameters(name, age, **kw):
    print('name: ', name, 'age: ', age,  'other:', kw)
    return

def keyword_named_parameters(name, age, *, city, money):
    print('name: ', name, 'age: ', age,  'city: ', city, 'money: ', money)
    return

# a function
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# a generator based on fib()
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1
def output_yanghui_triangle2():
    thisRow = [1]
    print(thisRow)
    yield 1

    thisRow = [1, 1]
    print(thisRow)
    yield 2

    while True:
        thisRow = [thisRow[i] + thisRow[i + 1] for i in range(len(thisRow) - 1)]
        thisRow.insert(0, 1)
        thisRow.append(1)
        print(thisRow)
        yield len(thisRow)
    return 0

def output_yanghui_triangle():
    row = 1
    lastRow, thisRow = [], []
    while True:
        lastRow = thisRow   # save as last row
        thisRow = [1]       # clear this row
        index = 0;
        while (row > 2 and index < len(lastRow) - 1):
            thisRow.append(lastRow[index] + lastRow[index + 1])
            index += 1
        if (row > 1):
            thisRow.append(1)
        print(thisRow)
        yield row
        row += 1
    return 0

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s(): ' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log   # now = log(now)
def now():
    print('today')


##################
# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        print('old:', digits)
        if (len(digits) == 0):
            print('new:', [1])
            return
        # handle last digit
        if (digits[-1] == 9):
            add = 1
            digits[-1] = 0
        else:
            add = 0
            digits[-1] += 1
        # for value in enumerate(digits):
        # while True:
        # for i, value in enumerate(digits[::-1]):
        for i in range(len(digits) - 1)[::-1]:
            temp = digits[i] + add
            digits[i] = temp % 10
            add = temp // 10
            # value = digits[i]
            # if (add == 1 and value == 9):
            #     digits[i] = 0
            #     add = 1
            # else:
            #     digits[i] += 1
            #     add = 0
        if add == 1:
            digits.insert(0, 1)
        print('new:', digits)
        return

def higher_order_func(x, y, f):
    return f(x) + f(y)

def add(x, y):
    return x + y

def mul(x, y):
    # print('%d * %d' % x % y)
    print(x, ' * ', y)
    return x * y


from functools import reduce


def factorial(*numbers):
    print('numbers: ', numbers)
    return reduce(mul, numbers)

import string
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
def __normalize_name(name):
    # string.replace()
    print(name)
    return name.title()

def test_reduce_normalize(names):
    # return map(__normalize_name, names)
    return map(lambda name: name.title(), names)
# def test_char(ch):
#     return ch - 'a' + 'A'

# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l):
    return reduce(lambda x,y: x * y, l)

#一篇文章让你彻底搞清楚Python中self的含义
# http://www.cnblogs.com/jessonluo/p/4717140.html

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：
def __before_point(x, y):
    return 10 * x + y

def __after_point(x, y):
    return x + y / 10

def __str2float_map(ch):
    beforePoint = True
    while True:
        if (ch == '.' and beforePoint):
            beforePoint = False
        if (ch == '.'):
            return 0
            continue # next loop
        if (beforePoint):
            return ch * 10
        else:
            return ch / 10
    return

def __str2float_generator(n):
    func = __before_point
    while True:
        if (n == '.' and func == __before_point):
            func = __after_point()
        yield func(string.digits.find(n))
    return

def str2float(str):
    return
    # return reduce(lambda x, y : x + y, map(__str2float_map, str))

class TestSelfDesc:
    def __get__(self, ins, cls):
        print('self in TestSelfDesc: %s' % self)
        print(self, ins, cls)

class TestSelf:
    x = TestSelfDesc()
    def prt(self):
        print('self in TestSelf: %s' % self)

import time
import xlrd
import xlwt # pip install xlwt
import xlutils.copy

class ConvertUnixTime:

    def __init__(self):
        super().__init__()
        self.unixTimes = list()
        self.newTimes = list()
        self.fileName = "idev1.xlsx"
        self.sheetName = "idev"
        self.startRow = 1
        self.endRow = 39086
        # self.endRow = 58005
        self.dataCol = 0
        self.newCol = 3

    # workbook = xlrd.open_workbook('E:\\Code\\Python\\testdata.xls')
    # # 抓取所有sheet页的名称
    # worksheets = workbook.sheet_names()
    # print('worksheets is %s' % worksheets)
    # # 定位到sheet1
    # worksheet1 = workbook.sheet_by_name(u'Sheet1')
    # num_rows = worksheet1.nrows
    # for curr_row in range(num_rows):
    #     row = worksheet1.row_values(curr_row)
    # print('row%s is %s' % (curr_row, row))
    # # 遍历sheet1中所有列col
    # num_cols = worksheet1.ncols
    # for curr_col in range(num_cols):
    #     col = worksheet1.col_values(curr_col)
    # print('col%s is %s' % (curr_col, col))
    # # 遍历sheet1中所有单元格cell
    # for rown in range(num_rows):
    #     for coln in range(num_cols):
    #         cell = worksheet1.cell_value(rown, coln)
    # print
    # cell
    #
    def readExcel(self):
        workbook = xlrd.open_workbook(self.fileName)
        worksheet = workbook.sheet_by_name(self.sheetName)
        row = self.startRow
        while (row < self.endRow):
            # self.unixTimes.append(worksheet.cell_value(row, self.dataCol) // 1000)
            self.newTimes.append(worksheet.cell_value(row, self.dataCol) // 1000)
            row += 1
            if (row >= 100 and row % 100 == 0):
                print('Read row: %d' % row)
            # print(self.unixTimes)

    # 创建workbook和sheet对象
    # workbook = xlwt.Workbook()  # 注意Workbook的开头W要大写
    # sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    # sheet2 = workbook.add_sheet('sheet2', cell_overwrite_ok=True)
    # # 向sheet页中写入数据
    # sheet1.write(0, 0, 'this should overwrite1')
    # 保存该excel文件,有同名文件时直接覆盖
    # workbook.save('E:\\Code\\Python\\test2.xls')
    def writeExcel(self):
        from xlutils.copy import copy
        oldWorkbook = xlrd.open_workbook(self.fileName)
        workbook = copy(oldWorkbook)
        worksheet = workbook.get_sheet(0)
        i = 0
        row = self.startRow
        while (i < len(self.newTimes)):
            t = self.newTimes[i]
            newTime = time.gmtime(t)
            strTime = "%d/%d/%d" % (newTime.tm_year, newTime.tm_mon, newTime.tm_mday)
            worksheet.write(row, self.newCol, strTime)
            # print(strTime)
            row += 1
            i += 1
            if (i >= 100 and i % 100 == 0):
                print('Written row: %d' % i)

        print('workbook.save')
        # workbook.save(self.fileName)
        workbook.save('new1.xls')

    def convert(self):
        self.readExcel()
        self.writeExcel()
        return
