# -*- coding: utf-8 -*-
###########################################
######### input & output ##################
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
image = Image.open('1.png')
image.thumbnail((200, 200))
image.save('thumb.jpg', 'JPEG')
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


# ConvertUnixTime().convert([1340159970])
# ConvertUnixTime().convert()
# exit()
###########################################
###########################################
###########################################
###########################################
###########################################
###########################################
# LintCode
from lintcode import *

print('SolutionTwoSum')
s = SolutionTwoSum()
print(s.twoSum([6, 2, 5], 8))
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([1, 0, -1], 1))
print(s.twoSum([0, 4, 3, 0], 0))

print('SolutionAddTwoNumbers')
l1 = ListNode.listGenerator([7, 1, 6])
l2 = ListNode.listGenerator([5, 9, 2])
r = SolutionAddTwoNumbers().addLists(l1, l2)
ListNode.listPrint(r)

r = SolutionAddTwoNumbers().addLists(
    ListNode.listGenerator([7, 1, 5]),
    ListNode.listGenerator([7, 1, 6]))
ListNode.listPrint(r)

r = SolutionAddTwoNumbers().addLists(
    ListNode.listGenerator([7, 1, 5]),
    ListNode.listGenerator([7, 1, 6, 1]))
ListNode.listPrint(r)


print('SolutionSingleNumber: ', SolutionSingleNumber().singleNumber([1,2,2,1,3,4,3]))
print('SolutionSingleNumber: ', SolutionSingleNumber().singleNumber([1,55,55,4,678,4,678]))

print('SolutionLongestSubstring: ', SolutionLongestSubstring().lengthOfLongestSubstring('abcabcbb'))
print('SolutionLongestSubstring: ', SolutionLongestSubstring().lengthOfLongestSubstring('bbbbbb'))
print('SolutionLongestSubstring: ', SolutionLongestSubstring().lengthOfLongestSubstring('abcbadcaaa'))
print('SolutionLongestSubstring: ', SolutionLongestSubstring().lengthOfLongestSubstring('abcbadefgcaaa'))


print('MinStack')
s = MinStack()
s.push(1)
s.pop()   # return 1
print(s.push(2))
s.push(3)
print(s.min())   # return 2
s.push(1)
print(s.min())   # return 1

s = MinStack()
s.push(6), s.push(5), s.push(8), s.push(2),s.push(4), s.push(1)
r = map(lambda x : print(x), s.minValue)


print('SolutionReverseInteger')
print(SolutionReverseInteger().reverseInteger(123))
print(SolutionReverseInteger().reverseInteger(-321))

print('SolutionPermutation')
# r = SolutionPermutation.permute()
print(r, [1, 3, 2])

print('SolutionSortColors')
print(SolutionSortColors().sortColors([1, 0, 1, 2]))
print(SolutionSortColors().sortColors([0,2,2,2,2,1,0,1,0,0,0,1,0,2,0]))

print('SolutionLongestPalindrome')
print(SolutionLongestPalindrome().longestPalindrome("abcbe"))
print(SolutionLongestPalindrome().longestPalindrome("a"))
print(SolutionLongestPalindrome().longestPalindrome("abcbadcaaa"))
print(SolutionLongestPalindrome().longestPalindrome("efgdabbbbafg"))

print('SolutionRemanToInteger')
print(SolutionRemanToInteger().romanToInt("IV"))
print(SolutionRemanToInteger().romanToInt("XII"))
print(SolutionRemanToInteger().romanToInt("XXI"))
print(SolutionRemanToInteger().romanToInt("XCIX"))

print('Solution3Sum')
print(Solution3Sum().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution3Sum().threeSum([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]))

print('SolutionLarestCommonPrevix')
print(SolutionLarestCommonPrevix().longestCommonPrefix(["ABCD", "ABEF", "ACEF"]))
print(SolutionLarestCommonPrevix().longestCommonPrefix(["ABCDEFG", "ABCEFG"]))

print('SolutionBestSellStock1')
print(SolutionBestSellStock1().maxProfit([3,2,3,1,2]))

print('SolutionBestSellStock2')
print(SolutionBestSellStock2().maxProfit([2,1,2,0,1]))

print('SolutionBestSellStock3')
print(SolutionBestSellStock3().maxProfit([4,4,6,1,1,4,2,5]))

print('SolutionBestSellStock3_2')
print(SolutionBestSellStock3_2().maxProfit([4,4,6,1,1,4,2,5]))

print('SolutionPowXN')
print(SolutionPowXN().myPow(2.1, 3))
print(SolutionPowXN().myPow(2, 11))
print(SolutionPowXN().myPow(2, 16))
print(SolutionPowXN().myPow(3, -3))
print(SolutionPowXN().myPow(3, 23))
print(SolutionPowXN().myPow(0, 1))
print(SolutionPowXN().myPow(0, 5))
print(SolutionPowXN().myPow(1, 0))
print(SolutionPowXN().myPow(5, 0))

print('SolutionSortList')
l1 = ListNode.listGenerator([7, 1, 6, 5, 9])
# l2 = ListNode.listGenerator([5, 9, 2])
r = SolutionSortList().sortList(l1)
r.listPrint()

print('SolutionMergeSortedList')
l1 = ListNode.listGenerator([1, 2, 5, 6, 9])
l2 = ListNode.listGenerator([2, 5, 9])
l3 = ListNode.listGenerator([2, 4, 8])
lists = list([l1, l2, l3])
r = SolutionMergeSortedList().mergeKLists(lists)
r.listPrint()

print("SolutionClimbingStairs")
print(SolutionClimbingStairs().climbStairs(1))
print(SolutionClimbingStairs().climbStairs(2))
print(SolutionClimbingStairs().climbStairs(3))
print(SolutionClimbingStairs().climbStairs(5))
print(SolutionClimbingStairs().climbStairs(6))
print(SolutionClimbingStairs().climbStairs(16))

print('SolutionMergeSortedArray')
A = [1,2,3,None,None]
B = [4,5]
SolutionMergeSortedArray().mergeSortedArray(A, 3, B, 2)
print(A)
A = [1,2,3,8,9,10,None,None]
B = [4,5]
SolutionMergeSortedArray().mergeSortedArray(A, 6, [4,5], 2)
print(A)

print('SolutionMaxSubarray')
print(SolutionMaxSubarray().maxSubArray([-50, -1, -2]))
print(SolutionMaxSubarray().maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))

print('SolutionMaxSubarrayII')
print(SolutionMaxSubarrayII().maxTwoSubArrays([-1, -2, -50]))
print(SolutionMaxSubarrayII().maxTwoSubArrays([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
print(SolutionMaxSubarrayII().maxTwoSubArrays([1, 3, -1, 2, -1, 2]))

print('SolutionValidParentheses')
print(SolutionValidParentheses().isValidParentheses("()[]{}"))
print(SolutionValidParentheses().isValidParentheses("(})"))

print('SolutionWordBreak')
print(SolutionWordBreak().wordBreak("lintcode", ["lint", "code"]))
print(SolutionWordBreak().wordBreak("a", [""]))
# stack overflow
# print(SolutionWordBreak().wordBreak("cadeddgdafafdadeabecbcagaedbeacccbbecceebcfcaabfcefccfafaacbdffbffegeagcacccbdfcdceefadabbebdadagbaggbfcfdgdegdabdacdffgcgaegcfgfceedgffgeadeaddfedabcdbeadfcbdacfaafcbbccabagaefdgcebfggbggbdbddbccbfcfgdgcdebacdcbdgfbeccecadabefgbfcbegbcfcgfggeccdeedgabggadbecdefadcbaefadegdgbgebdfdggccgaeabgacbefdgbcbbffegcegaaccagdffcggfabgdaeddeggcffcagfddgdcbbacfebaabcdaegceggadagefbcfcecaedgabdefaagdaaefeedcgcdfbaadcbabeadccdbaabggabfbaabbbbcaggbgfaecbbebadbeddbaccedgadecaccedebecggbdcbfdecabfdbggfgaaebgbccedacfcdcgfecfbbfafceagadaagagadeaaggfcdabegfddcaebdfebgddgcacddbfdfefgacfeceadfbfaagcfffcagafccbbdbcdgbefagacgbegccdegggaabcdecaefaabgfbbacedddgfcggbccedccfedcbfgcbdfeacgaggfgaabgfgdbccfaeggefcbgabdfdfbfgaefgccgadedbcddagfbbecacffdcdacceaaabfdgeagaddbdfeaddcebadbdgdafaeeggdddgbcgeaaagaedfefbcebfabfeegbcccfaaddbbadfbaddbeaaeebadgdecdfcadbccbfdabcdefbaeacfefafadbecbdgfggggabdcefdfacaebfdeegfgbadgadaggcababbecfdcbbeaagcgcbdccbageedabdebefgedgdbaddbbgcbdfbeabdcdcfbbbffbeegeabecacbcddcfcbgabgedfbfdcgacccfdgebaddfbagcdbbaagbffbfgceegfagccbgfcdabdfbgfabdfegabbebgedeegfdeggeffgbcbfffdbbgaecagaedfdacfccgdcdaecafagdaffabaegegeafadedcdfagbgeeedfdbdfgbefdafgcedececcgbdfgegffaaaffebdabfaedefbfaddgdccdgcegcgaedbadadcfbffffadfacgeabcbbgcdgcdefbeaddaafbgeccbadgfbbdfcagcbaebgedcabdecfdaccgdbcbagfgbcfdcccdgcccdbeebddefeafgcegcddeadcacagfffcaagdfaabaebcdddcbageeffebcaddfgegbddddabcdaadefbfddddbfbfegefccebfagdcddgfcffaeggbefadfbegfbgfefffbfdacadcacaaeefcedgddaaafgbgbbfeffdcacfbbegdbeaccgecdabeagcebgegaacabbabdegfbdagebdefgfafgaeddbgfdbfgdcdbbadgdgefagcgbcaebdgddedfgdecaebdfgcbdeacaddfbddgdbcaafcfgfggdcadgcaadafaefeefdccgggcdbabdcfabgddbacafebgffadaffcddababefbdaacdbgfcgfcddcggffgceadgafbbdafecebcgfeggaecdfeddcbdbddbbddabadbdecddbdfcbegdgaebcbbedcdceggagdccdcegaaafffbgacagfgefbcggfegaacggfcecaedaafaabecfedcbadcdbedebcgbcbgabcbgebbdffbecedfegdafabaabbdfegadcfffeggdacdafcddceafcegccbbeafcefgagafdgeedgcfefbccbcdggfebbebcebdcgccfdcfdeededcfbcedcfbfgcgaebdcgebddegcaeabeebedaaegcgaacgbbbcgedaadgaacdafdbfcegbfgbadegeeeeedfaabfacbbafgcedadfgdfdaegfceegcbgeadegceeafdabacbecefeefgdgcfffcefcbfaedgabbfefadddadgfcbddgdbdggcbacfaebeaabebabadedcbbcccddagbagfaegfdgeabecgegaadcdaebbbbgbaggfbbdaebeedccgegdaacfffabaagcgefebedgabebefbaefadbegggafedaagfbbaeaegaaabbacaebdeebaaegfefbddbefcgaeeaebdfeagfeeafecefgcgdaeeaeadafbbacagbgdcaagcdbfbcgfbaaeacfegaedcbeaccggcfgaeaefagabaecbaeecadefbcadbebbaebgefcgfbbdccdbaagcfacdfaadecabggabfdddafgeceefeebfebebgeefafdcgcecgggfaadgcbgdgageagcecfcceaaebdgcabcdbbffbffgddecfaeeecabagfgbacgabbcccccaagcbbgdafabefbfgaaceeaceaggaecbffaccgfdfgfddbaadebbdfbgeeeagbadegddddgbbbbdbaebgddefgedbggagbgbafffdeebbbaeddddafceabgfbgfgdeggdfgdgggffegdbbbdcffeggfecbebggabcgcedagcdcfafeageededbafddcaccaafcbaffefgbafbbaeecfedagffefgabaaccdeeacffgdafdcefacadabbaaeecgeebgebgdfgabfbecbbfaafagdfabffgdcffbeffgbeacfecccfcbeddgabgdefggddecdbagfaagfdgeaffgecbagecffaddeccffebaaeebccfdeeaeedafcdcbgfdacbbdfgecagfeedbbbfcbbbgggaefdafdddcfcebcccfdddececcgdbaefcdbaaadcbfacdacdgdgaadbdcgcdfdbdebggddebcccdfbafabadbbdgeggeeddefbcgcfafaebbdccfdafcgacgcfgdbeafaeeddfeadfgdgcfcbefacdeegcaaedegcdbeeggcgababedfcfgababgcgegccgeeeeabaegcgfcabcccbaecdfdebbfbabdfeebbeccegcfbcfddgdeeebacdggddccgggcaefbdccecdgfebffaeaaeafddaaedebcfefgbgbeacgeebecccaedfadaacfcefgdecgcacgbebgefgcdfcafefdcgaegefefggfdfaegddaefgecbcgafbfbbgfcbdfgccdafddfegeaccdcecbcbgbgcfadfefcbgagdcgbgdaefffdfceagcdaeffebgadebgfeebbcbecdeaagacdaacgagaedgcgadefgedfacddeecfcdeeaccbcfggccafbfeacfcaagbegbggedddbbfbbdccbcfbgbcggeddbeaefcfgebcecbfcdaegceeeccgbgcffbcdedaddfceddfcdaecfdcfcbbbdefccabbaedgegeebadbggbeeeddbfdbceccbaebbecacbgfddcgefbaegacfbeedbbdaggfdedfdfcedffcccgdcbdgdebdfcacgefdbbcecdgdcafcdcdacfbgcegcfggccgbfefdcecgdagcgefbafedffaacdbebgdcbaefbbaaeefeeddfadedgdgdedgccgegcbdabgbfaddafcecaacdcededdeedbgfaggecdggedddcgfbgfbfdadedgdeccbfcadffgbedbcggaecgcdfacaggegebddddeceaddbgdcefdedgbbdcfbgfddccfcdefccdfdfcdbgfdfcgbeeeceeecaafdabbcgbeeeegfadafdfdgacgagaeaedcdddafdeafbcaggafgdcbfgbbgaeabgefefedfabcecegedafgfacdebbbffcdcgafbfccgecgcgfgeccgaecbdfbcgggbcgcffaeecdbcedgadafgacgafebbbdfcfegfecfacgddaegagfbgfeeeacfbefaegffcggecaccfcfbgddcaccbffbbfceffbdbffgeddfbbgaecfgcbfdfdgebgagfgaddaggcccccbcccbdabgbadgfebdegaaefffgfdgfbddgeadacgggbgfecccccfdcbdfdagfbagefagdfcbfeeebeddfcfffbcfcaddfebadbgfgffgbbgfeagfcbgcggebdbcfadgdbeddaaefbfgbdbcdceadbedefcccbfdgcfccgbaacedeafgfcffbbabbccfbfdbgbbfeffbaaegdgcgbedbcbdcfabecgbabcdaccffgafdfdfcedgcbgabcgfgcceegaebfdbegbdbfdcagdaddacdcceaageafcebbdgacgbgagbbdadbeeffcabgdeeddadcabgaefagefbafeegbbfadgcadgfbfbcfaededeegddbbdfcffggafaddaeafcfcbdebbcfgfcceegcabcffedgcgdcgabeeffacceeeabbdaaebgdccgegfbcdcdadceafcgbbabfffcdebgfcfacdecbcfaabdcddeefbgcaeadagcacegceegfeebffdacfefcccefafddfdbggcdabegaccadeccgadeagbefddeefgfdgeefcccebbdgebacaedgbdfdccfddbdbdcdfbcaegabafcgfgagcgafbcgadcbdcaadfcdbbdaegdefcdceabdccgdfdfddaadcadbdcecfcgfefbfbcccdffeeadedebababfbgfbfefddeaeaedfcabgdgfagccaccgadddgedgbbgagafbagbdddgacagecfdeeabceeeeegedaabbbgcbfdagbaabbfegfabdacefggabfbabgggggcaebcbeegbfaccbbedbdgdccffaaadfbcgaeeafgcffecbadgfcgaafadcggfddcfdagfdfbbgcadfbdecbfaaadddfccgbffcbbabegdbcgacdgfbddcdcdecfccbeeafaaaedgcfbebaadbfgbgdbbfdfcebegagaagddfcdbgadggafagaedfcabgbcbccbffdcfafbbdcbedfdbgcbgaddgcfcggdgdebdgegcdfeagfcfcefefabgaadbbgdaebbaddgggaaaffgaddbfecccfcdcddcfgfffabfgdfabeaecdfeabfgcdagffaeebgfgbgdggabgcfbecgeeccfagfabeaafgdbfcfdagbfgafcdgbeeegeecdeffcageafgaafcacfacegddccfebdecafgcgbgbdfcdddfaaebcffbgbgfbaaegbfcaffbcfdaabdaaaceebeeabdgbebabdfcfgfbeacaaegaacagacfgegagcabeebedcbedcgcddfefacdgfgfbegeefdbdegabcdegfdgfbdbegfeffbgfaaefdafgfbcaecffggegfbgdccfagdafcebfeadbbgggdgaagfdcbgadbgffcfgdbgcddgadfbcedgbefdbcdccdffbdeeeafgbfdfdgfgfgggcdaffbceabggaacacbgfcfaaefeccgcgegfbafcbaegefgcbcbacefdgddaaagcdaabbfdbgcebcgcfcdbdebdffddecfffaegcbbbedfbcbeedceaacefdedffggedgdgcgaaeabadefgddebeedgcaabbcgdeeabaegeeeaefdbedcaebbdaaaccfgfeeedgefdfgbcbcafdgbcabdbeefcgagdeacfgbfceddggcbacffgadedaagagcddbfdcedacecccdggfgecdfaacebdfgagaddefbaccfcdgeeefcfgggfdcbggcgaaggegdcfbefaadccdbcedbbcacbgadbdaagddffcfcfadcagdebgfbgacaadccaccfecbeebfcbbcaafcccbccedfeafgfgbfcfebbggagdgfacccbdgggdbaaccegaebcfgadggabaggecgaefegfceefgfgdfdaeecgafcacdebfbfbaefgeaefdgdccggbeagdgeedcccacfcbdcgefbbcfgedgefdcfbggdefabggcfcdeegdabbbdcgbfgffbdecaaffeebbcebffagagcggbecdcabccaafaccacfabcbbbgbaceebbbbfgcabeggdfcgccfgcccageecbebcfgefgafffefegecdeagfaccfgebedfeeaaafgeacbcffcceacfccbgfbegadcafcbccccbefbgcddgceafddedgcbefdfbbbabcdeedabdddegfdedgdaddgegafgefcfaecgcgdafgdcgbababdbbgaefabfdbgaedecgcgbbcagccgdaeafbgeeafeaecabcgbadbacggeadabebfbaaceccfbagbccdgcaegdcabbdfggfgfaaegcefggbaacddafdcebcfbfggdbfedaggadddbecfgaaecfabgaaceegabbcbdacbbadfdddgfcdcfggecedcffcffgdafcedbgafecebedbggdbcbfdegcaadbeegabgecfbfbgddagbfccegadggdgbdgfcdafaaeecefbaafeaddddgbcdebcdbfgcddceefdfdgfdggbccegcdacdabegebbdfggbbcddcccaeccafagfgdcggcagfggdffgbdadeagagacdccffddfddebedbfdcaffdcceeababddbdfeeccfbebgbageffdddggfbefdbccfeeadceafaabbadadadecdeafdcfcbaebeddbffebdccdedaecbebfdccdffdddgceaeedaccdcgggedacegfgaeddbegdfeacdffffbcdegccdbggdfefdcgebabbaaeabbeaegebabdafaagdebgdaagdcfffcbdccfcdfgabafgbbaffadgefgeeecdecbedgggaffacbacfcgageeedacfegecacbbfdaacaadccbfadafgfbdbbffaebcdaadddecdcgfcdgggbggcbbbecdcddedaccabgdgfaegfcccecdcbcbadecbgceeedaaagacccegbbcdgbceafgdddgedbbbgfcadcbebcfbeabbgebdaaeebaagcacaccaebcaabgggffcgeefbgaefcgfcbcfgbagfadbbbeeeegddfgdfcfafgdbeeddaceadeffebdabedgefaacfafffgebgdgcggdaagfdebfbgaecafefagbgfdcbabfeedegfeebaadgbcegbcbeeacceefgcebbacffaccaaeffgceagdcdefcadccebbdeecabgdbaffgecabbegcaaddcecbdfccdcbeecgdfadbbdgbfdadeegeeddafgbdbdafdcgbafcggbdegaeaegbbgeabcaefafbbdabebbddcfggegaffaacaabbdgcbggdgcaddgbaabgbcaadcdbgbebbcdagdcabcdcccbgbbadcabgfbcfcdffeggbagdfdgabdaedddcdeefgcbegadgeadfebadabaacbdabeefgfeadgffbecfaacfgcfccfgccbgdaaebbafgcgbcbgcgeffecgfbccafbdafggedfcgffdbbfafdddefefeecececefcgcbacfdcbgeebffbgbdgffdeegefffdefgbcegbbbbcbacgfecagdgfbfbfdaafbgcffcgedadafcbgefeeffgacgcbbdbgcedbadbeacadcgdecfbcgcbddbgfeecaaggaedaeafebbdadfbcfgafgfaafaaefebfebfdcbagababfcgbddadbddgcegdadfgfecedeafbaggbfbfafeffgeegdbfdfagaeedaagebfffcfedgggfdafbeafagfacfcbbbagbdecabfbeacdddceddcbdeaadbfecabedefcffeccdabcaecaddbfaddfdadfdgaacbedfacggfdgeagebeafgfedeaabdgbddbgcbbbfbccgeccfdbdcfacbbfffddaabdbgbeeffgbcecgbfbdgegabebbaffggaedceabccaffeadecbbcgebbaggbfeeacbbabegecfbbcfacggfabceegegdagfdddegagabgdffagfgbdcedbgdafadeabggbbadcfcdbdfffeecfcdbfdeeefeedbfbcbffbgcbcdfcagdbgafddbecgaccfegadgefgcafdcbcabaagddedaefccbdaggceabcbffcafabaacbeedcecgcdagbefcefddbcfbdcgdcedgcbfdgdgcedaeaegfdfefcefefbedgageegddcabgcdecbeebcfbgbaebfcceeffbbeccfgcddeeeaadgeggdgddabafcbdfbacbfbdecedgbebebfdcaecaefgggggfdgdbcgddffbbegcdbdbgeceefdadefgaddgfgfefffgggddbfdcdcccdcacfgbcbgeacbggfaeaeedcfedgefaffbeecdgecdgabaacabcgfdaadcdegccacfffgbaabccbdebbbcfgbeedbffeccedcdcfdfacggdafbdcedgbgeeededcfdebdfgdceacgbecggcdegggcccaadgdegbdeedcdfdebbgdeccecgfgdcegdcaegabdadbbbececdcfedgefbbffbbedafbfafabcdefbcafaafbbcagfaffffgbbbecefbdeegddgbffeeaagdbeaedagfebebagagcgdcbeggbbecgcacddbadfccgcdadgfbeggaacddgdgfgafbgcgdffdegdfbgffbaeffgadfdegbbebbdgdfebeeebfacgfbcggffecccffebcdcafcdaeegbeffgbcccbfffgdbafgbbdfbdfaddadccebbgaefegaaccbggebdgdggffbbbefdgaaefagegfecdfaeefebfcgccfffgaccfbfgbdecdefddeaaddfcbaaagaaadbdeacaebfbcdacgebfdegdbgaafgefbfgecdcfbfcfeffgdfdeebaadbfgeeddgaebfcedbcaedgbcgdcfeacacddecbdfabdbcbgfcbcacdbdgdbegebegebccdeacfbafebaddagafgbefdaagdbaacagfdbcdebfafgcggbccecbafaeeecfffgegaagdfcbbcdadegebdacaeadecfabfdebdabaeacacbfeedecebacddecegdgeebcgddagbacdcdggccgacefffgfcfacebcaabfagfaecadbddecbeddbffdgadafdgedccgfebedccadbefcggcadedabcgafgdefbbbdeacdffcdcdacggaaebbdffedgdaddbdcgfebdgbadacfebfddbfcgafgafageaffgcgacfgeffcbfaddfbdgcedebdafgdegcagecffaebdcfdedfdcagdagfdggagfgfbbbeadfdaebadddacfgdcbgegfbafeeddfdgbeafgebagfdgaeccdbfcafgeegcadgabcdbdcfadagbeagaffecggbddcdgaddgccfeebdfeabgcfgbbbddgcbddabdfdeefgagfeddbgegaabdebfacfbgfafggebccdbdecgeeccccdeagaggcedbfgfgfafbbecdbabbeddaeecfgeagbbebcbecgfdgeacfaedacdgfeebfbfggdgefceagdaacegdgbfaebddecaccacfegcbeebadgbedecdbfbffeeefdegdcdfgdbcdgdebaffdgadeaabbcceffffcfeefgffaccddggabeeccbccgedbfdgagdfbeeacceeaafaadecgcabcdcfaagegdedfgfeeeefcceacbbdacegfabcgabbefgbcdedcedcggcdbffceafaefffacadfcdffacdeccegagecaafebebfbcbaeagecebbbcfefacecccadceadecbcgeggagbaagedgfbgbccggcgecbdafddbaadgbcbgbebbagabfcedfefaefbgfagfcadaggbgagbaegcfaddagfebgagcdddaaeaababegafecgbfgfebffeebfbcgffaaefefaecedacdaccabcgfagaegeffcbfdeffeddbddecgebbebfgeaaedbcacedbbfcgccfagbfdcbggceaebbddgbaddfafaegcfcgdaggbaacabddbbdeegcecfgbaafefbcbacfdfffdcafbfcadacfdgfgcddabggabbebdabgeagddafdgcddgbggbfegaebdcgaagcabagbgbceabecggfbfbfafcbeeacbdfebaedfgcfdadggggdgcgfdbccgdcefabdegeefgcggbffabgaefaabeaeaacggdcgbfcffdfegebebbefadgcfaacfaaadcbbddffbgefdgefbebeedcfagcgcgbcagaegbcbfdadefeefegebfgdaedbegdaffadcceggfbagfceffegcddeebcbbeeeeadccaaaffabbbcbegbcefaecfbecaaaaeeaefgeebfgcgeadaedaefgacecfggfdbgfbdbcadcbddgbcgfgegedegfbcgdaabecbeegcfddgbdgebeeadfcfcadaegfcbdcgffaefagafbbeafdbcdedgegfaegfaaccefdcbgefgfaafccdgagdcgeddfcceeecbdegffdebdddacgagfgdefebgbfedagffeegcbfbbeagfagdfccaccfaecggcefcfggddfdeafbgbfegeccfbggbbcegfcdcccgegafdeabbfacddbcgaeddfgcbbcfdcdgaabbdabadaedccgafgagabbafbdgdfbeedaceeafdadggcbebbgebgaabdggcfcaedeafefafbeacacfdbdbefaagegfbcfeagafcffdagbcffegabcadgddgbdgffebegbfedccbbabffggdccagbeefgeddeedaefedaabfaeffcdbaaefaafeaadfbgcgbbbcaeagccabddbgffcaedbbcfgaegcbgbfeabgbfbebfgfebgbbgbcdgeeeabefaeedadfedbgbcbaeefbcbffddegeccbfcgfbbbdaabdgbedffefgdacegdcbabagecddeedeaeeagcgcbgdbggfgggcffedbfgdfccagecgcbgadgagbeafgcdafdadfafaebbaffgdegdcabfacaadegdgadbccdbdeddececgecgagfdcffcadeeadcgcfggaggcggbagedbgdfcfaadegdfdbbcaafeeccdaacacgabfedccbfbgegcgaggagdbgaaddebbdaaebbfgaagagebecdfcgdfdfabbagbfagcafcdebfgbfgbbccegbgcadcbebdffgggdafedbeaeaacecdfedgcadffcgacdgeebcgdaeeabffgfaabefabfbagedcaeagebabaabaeccdecbdcaebebbefgdfcbbcadafeadffafcagcefbagdbfgedcegbcfdfgeecedadbfdeeffgbdcbcabggcaebfbaacdbfcddaacacfabcbcfcdffaecebddcbggbedgeeagdeccgcgfceaggbbfadeeagcbbgdbbagcgfgbdaggebdcgafefdbacedagfbdcddefcbgfgddfebdfcfbdfegaggdbfcfacdbaedbcdfgfabegegbaefcccgbeebbdcgeaababggabddcbbbeacfgcedcafacfafaedggfcggdcgffcdecdddagcbbdbegggbaffafaceecfeafgggbdffbdbbfedgeebcfggfcbcbbcaabddbedebgagdcfeefcbffacddabecfgbebbbaebdbacgfegfbbeagcabdcfefbgbbfaceefagfcbccfcafcfbfaffabagcbbfdfeaegcdbdffeedcdddcddbfdggcfadbdbecggedccgbfebdgbbcfadccgcgacbbfaeebcffeddefdacafdeffedaeffafcegebfccbefcfdgefebcffaafgddacgagafgcfcecccfcebcedbebbcagfaebcabafagcgdfeadefadfbfccfffggeafcaebdbdbbddcfebfbdeacgeagfaebgfbgedababgdddcddfbbbgcaccgebbdfggcgfdfeagcebdeddggcfacedeceegeeecdafcgedcdfacggaacbgbcfcdedgdgeggfabcfedbddcdgdegbgcbfdedbacgbgcfegeggageabeaeabcfafcgeagccbffbcccadfcfdddegbcbgdbbfcgefbecgddcgdbbaeababecdcbacdbfgacafadfgccdfddeababfebefcbdgaceabgbdcadcafgfgaacbaacffbfbbdbacceegacgbgbbefedccbgceafbeecfcbfegecdbfffceegcbggdbgggedfdabbaagaefcfcfcfaabegcabeedagdfeaacfaafcddabbbgafecebgbdbeeaedagcfcffgggeaedebbbcdcfddgeadaabedbdcaecfdfadeecccbegfgggabefdecedfdbdgebcbebagccaffecefbcfbbacafccbfcaadbfdebeabdddbcebfgagbdeffdafcfddfffacbaeceabddddeccdebabcageaedbbggdggbegggaagcbdgbffcfggfagdbagcbdbbbafdbfedgaaaagdfcgfgcagacaabdbedeacggadcbgabgcdbffecafgecceegecfgcbaabafdabgagefccbaadfegdfcceeabccdggcgfbbeagfgcdcegagggeedfaebceabcbfadgeeacdaeccaeagccagfdfcdaagceageacbabdedbbdaacebgcgbadaegeggaaacfbeecccdfdfcabafgggdcdfdcecceggfdfdgdgfbcdcdfagaageacgffddccagdcgggafdefeaefgbdbdgdcagagaeabfdedgdceacfdfaeafgeaadegcgecbcbbgedgbgdadebaddbbdfaadbbedgcbcggdcceegbddabbbeaacaffdegaeafdgedccbaefcafeeeffbfeeddgeececbdeeebfgcgdddffcdgadaaebefafaeaaedgcefegagfccfdcgfdgbedgaefdeacacaeccfcbdecafeedbcaceebfcdbeeeddbgafgfccfgddfbddcbaggccabbgaaebbeeddfgcaeagbdcfcaccfbcbbgggggcffaafecbgaeabbddgcedcgeggdgabgafdfgagdbgbbccfgeeecebdeadgffebdadaaggbaefgadcadefdbdbdefaedgadfcafbgfdcbebdaedfdbeebddggggdaccggfegfaadfbagfcbbgaabegcggageagbdacdedebfgfggcfbfgdcbggdggaebagddgbbfgfddadgcgdecdcfeagcgegcedaddffdbegeadgdbfabaeeccddaceeddedccdefgbeffagggbfafgeafbgccabdcbccbafaccgafdbefgeebacaaedabcfbfbbegabbgbbaagaacbedgabegfgccdcbddbcedcdaffacfbdabdedaffffecgfgdadcbfeadcdeccfbbbaaacggaeebaddbcbfbgfabcbgegeaaggabffdfgcgbbcgbegfgafebddebgebedgefdadeebfgdabacggfgccdafbfagdcdfaedbgdgfeaadegdcaaccdaagcecabaffgcgbgacecafdadafeeadbbfbfabbcbggeeddcdgbagcbeebeaeffcagbcbccagbccdfbgeddggeagcbacfcabbeggabgeegabagecdfcacggaadababbggdfecddacefbbbbdccgagaceegbgadddfcaaegaecdfbdecccfcfeffdcdbbbaeabfcffedaeeeegfgfddfdbacafggfgfdgcbfddedbfggdfceffdfdfcedcbeagebacbgbbbfadcbgdbeagdfcedfgbgcbggbdgbedebgbgeecagcegdbffefeddbbeceffddfcbcadgfdbggbdfdcdeecacefffcbefffdeddcccabeaefdbeggcfcdccdbdfdeaebdegbecffbeggbdfaafadbdgegbfcffbfbfccacagabgbgcgaaffbdbaegffegcdbggeafcdggbfbdfefgfebaebbgcgbdebfgebdfafcbdabbffagdecbdfadabcdggdaedbbaccffcebcafddggabddfeabaaccebefeedcfgafdgfegefdffggceeageddddcgbadgdeegfagfbeegbefdeadegagbgcdeebcdfgdfcgcdefdadcdedefbcadaaebcggdeebegfaecfgafcaefebgagbbbdbfgdgdcbfgggbfbdegfaaadbgdfadefaafdgedafaedaedeefeddeaafggaefcbaagbecfdfcabeefbbbbabfcbebgadcecadfecfdbfdgeegagdbcbaaddafaegefebaddeecgcgadabfeadaebadfdgffbcgbefbaecaffeegagfadabbeffcgeeabfggbefacbfadfdcebdaedceaeffbaddcafagecaafcacfabfdcdecaagaafgddgcdbgdacbeddbbedbcbccbfebfcabcbdddffddaeddgfeecdggdccbffcfcgaddadebedacfeaabcfafdfgbedcfbgabfdffbebcadbdfbfbggdggccbfecbcbggafagcgeggefafacecdcbebadebbdgfcgggeefbedgabggbbgccfbeffabeabdfbgaedccggbbebaaegecaeffbgdgeeegaeegcddfaegdbdcaaadbededcgaggbdaafccecdgaaabdbggcdecccdeagadegbbaabadacaagafceefgadcdgcgcebbgbceabcbeeagaabaeacecdfdafgeaefedagbcgdcgdgaaeafffgcbeccagdeddbacfegadafgbdddefgbfeaefabegfgaaaabddfcgafaddddgbdbaebfceeddfdadaccgdadbacfggefadaabafeeaeddfdcaabagcbeggabdgeaffgfcgcdeageegfbffdgeaffgabdbgcgccbaacbdedeecgccggbfcgdfaeggcbfgfeacggddbcaagbcdaaaaadbfaafgbeabggdefffffggcgfcagbggbgfebbgfedaedeegefbfdggdffcfcaffcbaafaaeadcfbgbcfcecdgcacdbcgeabccaedaadbgccbcbefedgcdcdaedbcddegdefbbfecdbefadgefbdggdcfddedcbfgcffdffebebfcededbcbafgbffaeggefcfcbgegbffacbgcbcfbagaecffbgeefbbdbgafcggdaeeffccgdaffcggacbfabcggfbbeeefgbdgdecefgfagdbfcaagaegaffageeceegafdbecggdfdccefbcbccdadcedgfabebaeadedggedfgbbfgbffbefdcagdbddeebgfbbagebgdgeefdgcbdbfaecgddfcbfbbcbgcedcbegfeedcfcfceeccbbfdggbefacdfdcaabcedaaeacegdaagabffbeggbcbcceegbegcdfdffcfagdfcgcaefaafgdggcdbefbcfgfdddeadaaabdacfcfegfbgdfcgfeefbedaefcbdbeeafegcaeffefffbgdgffgfabebeaffgggdggcdgcgeebbcbbeagcgfgdcdefggbcfbfdgdfaabecggdaaeabdbgcbgfgeecbdfdfbbfecgeadgaaebaabcccaefagbadbedgddfdgeeabcffdfcccffbdbbefcbfgggegedgdcdegbffgcbgfccafdadceaebdcffcadbbefcbcgaeagfceabcfgfecbbfbgffafdaacefaacfdaagaebffaecaffeaedfbcebgcdaecgbfdgagfbcfbgfegcdacbefccdegbabbcbddffcdeedfdceabbafddgdgedfdcfaefgedgagafeccgaddabdcaabgcdcdbdfaefdbfegacbafccfdcfbgcbccbccccddbfcdedabbecfcaafacbadfcbaafcdbcagdfccedccadcgcfddbbdefbbabdfaedaagbgdaegfbfbdggaeecgdbcbdcdgabdafbgcgbabgabcegdeaefddeafcgbgfeadbfabgcgecbdcddddgdadgdefdfcbfcedgfgbdfgcafbbgdabafbbdebdgddgecedbeedgggadfgfffegcbdbccfgfedebafagfaadedggdfeadfbggfcbgdbeedaggabacgdeaecfcedfgagabfafdfbbcggaadgdgcdegdbfeadadcgdabdcdgbagggadadebbfaededddcffgaabfdeddefcgaadcbecbfffafcdcfceabdabedfbbbbbccdebafdeadaddbgedeggggefcdbbabaegfdgbfeacbbcdcaagdbfggdbfdfaabcdfdbeafgbcgebacfdecebeaeedgafedgdbbeacbbddebabafaaccbfbafaffabdbbddbfeagabbdbcdbfacabcdfbeeagcgeebceddagffefebacbagagcagefcgbadgfdbafbdedgfdbbdafbaabgbgfdfebaeeefgcecdddcfgeecafdgbdggcegfedggfagfeebeacacaebfbefedcbaffgefaaefadgacgfeefcgaebgfecgeedgefcffaacaaaaggfefbgeeggeccfgdegaadcbdecdfabbcgefcaddffbcdgbedfdfdcfeacecffaabgdaecgaacgagedadgdbebaacafabedagacbbfbfbcdbbadccdeeffgbdfagbcbfdfdcgdfgeefafafbbedbafacaffebdbcdefebfdbbdaggbgafacffgebdgceddaeeabcgecdcdfdcdeegefacafbfdeccbaacddffabfadaggcgagcgdaagbcbfdfgadaabafcacedaaeedgfbgebcdgefdfeeaegdddacaecfgdggbcccfbdcdaccddggfeegbfacbgcfgebdefgedcfebebegdbddefcacbdedaabcaadfeaagfcaeecbgfeccgcdbgabagccaddadgdbgebbfffddcffgagbbdebbgegacebbcbaafafdafagagdgafcaaegafbfbbabaaaedgbacddbagbacfdaaagdceffaddaeccffdebedecaddfbcdbagdcdgdbafgbececbeeecfcagbegcfbfdecfcffdcceadfaecgafeefbdfgbbaadabagcbddggeadggafbbfdbdgdbcfgcfdfgbbddgabeecffgfebcadcgedcfaeefdeddgfaecedbafgbgbadffbaebedbdacggfggcbbcddebdggeggaceabafbgdbfbefabadgdeecgababegbfcdcabeceecfbeggacagbgdddbbcabfgfgfgaafdeddcbceccccaacebbegcaafgecgdcfdfbbbggdeacceebdcecfdebbdabdabdegagefafefbgfddfcbffgdggdgababdadaggbfcefadbceggdcgfbacccggafbabccbffbdcaaffaaacbfddcabafececcdbafgbcacfffcfddbabaegeeeacgdaeefgbdabacbdgeggfacddfegdbfagbfaadegfaecfacdddfebccefgacccgebcefdfgfbagfdaaafabdbaeeecggfgcbceagccbffbdedgfadddcdeaacdbefdcaaegcccdgdgfccceddacdffggggeffdagbfbgaeedbgafbcecegafdbaedacfgegbbcdebaceafeebcgccdcfaccdcbdeefbecabffgcddaddedgffeagdfbecbegdfdceaebgbafgeffagacgafccbgbgdfceeedgcedcgfecfgfbcdbcedeabbcbbcddgebggdbbfecfadbddbcegfgaaefcfgfdeeeccfbbbdgbdagbcefdaddeacbdgbdbbgfdagebaecbcaaeebeebcdfaggdafgeeacafgddfggbggeefcdbgeabdeagdccafdgafbfadcdfddeffeggcacffagaaeafcgaecacfafgfccgbaeggdffbbfaggaagbfbgcgcabfbffbggeddbacgddaccbdeebdagebeegefgabedagcdeggdgggadebdgfgfbadfbddbdgebcbdddedacbgfdcfcbggdcfacdabbfbbedbcabfbadbbabbeaecdegeddgeccfbcfecaecfccffbgdecgaedgegdaeaaabgbbbbbdgacaaefefedbeagbgbgaefabggdgbaaffbedaeacefbdcagdceedcdgabbbfebdcebccabgdffcaefgbbbdeafegegfeebcfddbcfbgbgcbdfaeaggeaegbabdafgdgefagafbgefbdbdabegabbddcgbaebdbbaggfbafbbbaceaabbdfgabaeaagfcgegacgebedfaeeecbgaagacabdggagadfcffebcfdbgccadaeebdgfabfddffddccbaceeffafdggcaaeaededdecbbdafgcaacgcccaceafffbabdadffeeecccbeaebbgaaeccdfdfgbadfbebbcdegccgfgggebgabcbabggedbdfbdggbeffgagabbfbcgedfgbfdacbcdeaeggbecbddaefbbedbddgeabgdabbaecedbcfbecfgaaddebaeafceadcdacecagffefbcdfeccedgfcgbgbbdggfgedfgafddegbeacagfeebaacgaddcbeegadfebdgcdfabcbafbabgeddcfggecdgeccgbdefededaggefecfgfeecgbbgfebfcfbcaccfdbeddgacafaabafaccdccfaeacdddfcgdedgedffecedcgffefaceaadaeebedebbgfefaaedcegacaacdcaaaaefabfcaeabdegebbbfgcdbcfggbagacgbeccbcgfgfcagbbggadfddafeaaeabcefdbccdccbgdfbgcccbcbebbecageffbedccdfgcbfaaaffcbeebagdaeebcdbeaebfdebeadfefcagecgabgcaebbeaabdgeagbbbabedcbcbgggabddfaggfbabeggfdbebbbfedaecgfbdcedeccegfdfcfagagbbbeebdaebadabcbcabadbdgbgfebcdafebeaeaaeedadcgggefaaddfbgddbdbabgafgcbecbfdaaccagagcdeeafccfegabcfadbbaebffccbggfaagbfdeggfafeagafgfadcbccfgfbgbfaecaebfaadddfagfaaedbcfbadafdecbffbcbfafceceacfdeegfabedcaeggabeeafddfgbeddefffgaccdfaagebbcggabdgddfacgfafbgbdegdcbggggcdabdebdeffcecgcaeaecfefaeccbdfeeeggdaagcecdbeagccggddbefaccdbebbfdabgafafcbebdedbggdeffaaafaccbbedgffdcagcgcbefdccfefeaegbfcggfaafgeffdacbggcdabgfccafegceaabcgfcfcabaceddededaaecdcafbgggeeeebadccegdgagfbbffcedfadcegfadbadddaafdggebcedcbggefecafbbaegefadagcgacgcaeaabgbdgdfbdaadfaaaadaadfdeabafcdffgfacaabebegadbfccdcbeggdadbcdefeccdaeegeacggbccffgedffeeddacagdagegdagaaacggfgbfaaccddgfdebcaebbafaabcgdefacddabbaggbgedaaffcededbdbcaaedbaaeebccgaagbeaecgdfeffdffccccfebdabdcfcgffgbcacaaagaagcggefcgfddggbddbfbegbbbbbefgdbfacaffbffffbeceegggabdaagaabfgdaaabcbbfbcffaafbgdgdccabecgacbbbfbgaaaadccfecgbecegedcfgdffddbffgefegdbeagebgdaefbgdfgbeeeefbfadgeaaffbeeecbefcdeffcdgeeacfcgcfdgfgefcafbageaefadfgfdafgfefgcbaeebggcabbbebebgddbbadfbggadfbdabeecgcecbdbeeeggfdaeeggfcgcfafbagacbaeecaggadbaebebcaacbabbcgfbgffcbddcfgggaagfbdbfecaadbcfbbbegcfcgebedbbcgedgfbfdgggdbbagedeaadabcbeadedgacecaaaaafacaedffbbgcgbdfageggecbdbadcaeacdcfbecddgbbedcfbbgecaebbaffaafdbdafafaffdaffadaedcgcfccabgbdagecedcedgddabcbeggcbfbfefdafggfbefafbgfaddfcedcfbcegebacdacdagagdgbcefafbgebbdaaeccfcabdgecfcgbcaddgcbgcebdbdcdbcaeaefbccgbeffbadaaaeaaegdfddcgeeddceaeefbdecbdacbeadfegfcdecfgaffefedcedfbdeafccgegdfdgdddeafafadabbcfdbgbcdadgdebfgcffbbefdgdecbdgbccegcfdeddadgegefbfcfbfcggfgbgddfgbbcceegbcafeadeadgdabffgagcdfbfefccfcaaagccadgffbebggbfcebadabdffgdcaeaebececdagdgeaebbeebcceebabaddagfeffcaagdgdggggcdfaaeffecbebbdbdcbegaeaeebcfccgdfgcggfddcgeadcdfgfcfgfdcggefaegfedcfdgdbcfadbecfbeefbdcecdbdcfedafbedffegddfbdegaffdcdbeffcfffgbeacbeagbfaegeeddgeeeafcfddgaadgdfbfdgfdfcbabbgccfacgcbdgdcabfdbcbaagcdadcggfbfeeabcdadccbafcgcffbdbbfdbedaegecgeeaccddeedfacdbbddcefgabeecbfdaagafbbebfceecbfcbadfdcfdeggbffdddbdbgggefafabefdbbcecfaccagedgbebadegafcdcdfecbbfbeabfaagegbaaaedgbfcfgdefbaddfeffedfffegcagdcgaedbfdbeceefdgaeffabbdfffgeddggeaacaeaafcecebfgaacccfaaggfbebdeaabgaedfacdgfgdbagedaecaaadfbfcbebgddbagffgcadeggcagbdeggdebeefdfbbaageffgddaaefegggcbgfeeagdfeegdegcebgegaabdbfgdegcaddgabebegbdgeaegfcfbaabdbeggeaaaebdebgccbeedfgbcccefcbcabgfgbgccagbaabdedfcfadfdddafgabegbgfcdbcccaafdbegffaaddefeaeceggfedcfgbacdegdbdecdagbagebadcddagfbdgeegebedeggfbeafedegbfceedgcgfafbfbcdfdbfeecfbgbagabfdgdebbaeddfcdfcdabfeddabebcaecgfgeadccbdbefdgabdgcadcdfccfbgdagbeffefgefgaaddfbfbcfbbfgfgdcbfdacaggcdfgbafcgcfdeddfcdgbfgdgfbgcabgagagddcecgbeebabfdcdfececbggcecfaeefdgbegbgeeffcfgaddedcfgbagffcfecgefceaegfdfccdgggfffaabebaecbggfgcbddcecgaefbafdfcbbeebfccaafagfbefgcdccceeecgdadccbaaabfbedbbgggbegbgdcdceddgecfddbbadcebgabcacgefdccegeecagagbcgbdadfbdffcfbabbdefbeaceabeebfffecgacedccccaffbeddgfaacdeggcabgddddbfeeeadecdedbfdbegeebefaaffeafffbadeagdegbfbdageabfbfdcbeedfdcbacgdggdgbgcabdgebgabeccbbacgfcafebaafaggbacdacdefaabffbafbcbacgbedgfbaaeggcfgfbcddbeefbggefbacadegcgabbgcaafbabeaagfbdafdfgeeeaaafcgcaeggffafgbaegaecgceaebbfdecbabafafcgdcffafcgfbfeeggbacddbcbabaecdgdbgecgbgceeffdcbegebbfffbceefgecaeccbeafdgdaggcbcdcdeecfgeabfbabeecgbgdaabbebfeeedefaccdbcffbagdgdbeacdcfbaggggecebfecbbaaagacfbbfefgbbfbgbbcdbbgbcefebdgbbadbdcccfeecfcbafdcbbfbabggbcdgcgcdbagcgaegaggaeafccffffcbbaabdgaacbfefdceaadgebcbdadcfdfadbcdedagcggcagdccedaaaggegeagecbgcgfdebcbcffgbgbfbfefcdcgaecdggabgfdecgccbfafffeadbcdebecfcafcedcdacfdbggeaaecbcacaeacaabgcgdfeabdeddfdefcgcaeedbffacdgcaebefadegeeabgbfdegdbgefdebbbfeaaffafggfgagccdbggedggccaaafeegbefdfecdbaaaagccfdggeefcecafgddgcegbgfcgdbddadadcdbdgacdfacgceabfgcbbeecgbbceeadbaagfacgbbbeaefgabgabggggbgfcbdgbgbbcfaebgaafccaccffaaeeafgcccffgcgebdegdcddccefdeffecgcggececfgddaebaaagceeecedbdcgbcbagbaededcedbgegbfdcecaffcbgbbebdgdeeefdbdecfgdfaedacddadgcacfffdfeffagffgfgggegegffdaedgcedgbgcefcbebaedebdffgedbbfgcaggaececcceefaeegffcgacgffccdebcdegefgadbggfcdbdddgfbgdaccgedgcbfbgfcafaeagfeaageabffbaeffddgggcgdbbbebebegbgcgbcegcegdgaefedacbfagfdgeceadabdfebfcebedcedgafbbfcffbgbbbacedfgcfdgfffgfcddacegbegfbdagbafeedcagcgabcbdbagecdcffcdcadddegcfdbbecgbgfbbgeeeddgdfegcggcbcfbgacaggdgceegacfafagadabbaceegbcdcgbgbccaaeccdefeddgcgfdbcadfeagdadebbacaeebdbecbagfgaaadcaacbgabgaacadbcbecefggadbdbacfgbgcfeadfedcbagfgfcffbcgcadageabbggbdcbagaebcdcefaefffbbgdddedbfgacgfbafdcdcgdggbdccfcacddaddeaacdgcgfagbbaddaafeaegegcecdfgebdfedcgaddbebfdcdeggfcbacafbbbdacbcecgcfecgegaddafaafebeecddfggfbgbgfgdcgfceffgbgcecegfgbfadgcedfbaebgfegebedcfccebeegfdaceeedcfbdcaabcfefbbcbbdgefcfegfafdddcgdeaaedcdabccaaefdbabcbbedbecefgfagadefedccdcbbcccaebbedagadfcdccabdfcdgdgfbeeacgeecfaecfebfefbbfbbfabdfbfdbefegbbdbcafdfebgecbfcgafgdfebadcbbgcfbabdcbbaeaegbfffdcefbdacgcabdegadbbbdcefdabcggddddfcgdcbdbdcggaebeadbcfegedecagacffgacefcgggacaeebcbacaaceaefgfebcbcbbccfdfbagfdgcgdaaeabegbcfabadfgdgaecefbfebegaccgbegaeeeggfffccbefbfdagfeeabgccabedbabcecfcfbebacaadegcgfegefaffdaaddbgagbadbecaagbccgaaaaagfdccdbcacbbgfaaccagdeggefddcfecbgcfeaedabegdgdggcdaadgdggbgefdgadefecbbbfdgbbcfagbfdbeeebddfgafgfdddcdffbeeggagbaabbeefefaeegbgacgaedgfdefaaabcdgfcecbfgeeaafaaddbebgfabaedbdedcbcafcbcgfdbdabbdgbbgdddafcdagcdedgdbacgaaggccfebgfddgceaaeaffbbddbabfafbgfgaffdagaafbddgebafccebagaebgggaagafafacfbabfacgbcffdbdebeeffeeaaedefegbbeegdageeceecafabegfeabdfagcffegfecgcbbgcadggabaddbecbgbdaeaabggffbeedgbefeeggeeecccegbbgadfcffdbfegedaaagedebagcefbgdebdbafgebdggbeggaagfefggfdffgeecfdfeaaadbgggecbcbdgebebbbaacfdabgaaaaabfcfbcabdfcacbfbcagbbbacfgedfdedbfeadabddefdeacccdaedegeacagdeabefeceggbgacfbaddddddbeccfgcegaadcdaafbedgadegeacdaefdebgeggagefggfadbbbbdedbaegccdacbcfbbbbaeafccffffefdcgecbebedbbbgaadfdeedadecadddgfbabbbgaddabecffafgafcdbecagfaadefdcdaaedggedfcgecdcbagbfebcgeddcbeedfdbgeedbffbdadfcgebedeegggbffggdbgfdabfaggdgcdbffdcbebfadgccffdbbdgadeecbcddeagfcfcfbcgbccfccdcffgaaafgbfcaafdggebdbbaeaffcbdceabbbbebgegcbddgbdaecdfdbbafcgaeacbdeacfcbaebeeaafbgbfadcfbfegffgcfgcdbfcgdcgbebeagedbbefdedcecdcecbadbeabgefabgcdeeebafedbbfcfadfccdcbagfdecebdbafafdcafagagbbgaeabcgcaaggbfegceedgedgggceacbcebbfgadbbdeeeebfgeaccaggcgafgabgcacfdcbebgfdcfcedddbeggdccbgabefcfdgagggcgcbageecdabfggdfbaeagadaagadadcedcadacebfcbbdfabbgfagfbeecggebfbfagacbfdfffdcbffddddbbaadbfeeacbfebbafebfedaeacgabebecaeeggcgdbbeaeddcgbbgebgebgcfcadcgdbbecgadfbgbfefcfgdcfcbbbedgbbgfecdafcadefabecdebcfefbbgbbgegdebbcdggacdgccgebfcbccgegbbcfeeadgefgaafgfdbdbbcbfafafceffgfgebggdcdfbecefdgbeebfadfabcbaafceecebdfbdbdbcggdegdaccebecbfebgefagedefccddccadfbbfgacfbefdfbeabadddecfbaadcaceeagdaadeadcacbcgedabecdbbbbbeabaabdedcafedacgafbbccdcgdbffdcbcfedgbdabaadfbdccaagebdaeaegegcdddadgcabcgegcggebaddcbcfgfdebdcgaadeedfbggagbbgceabecabaggfgcccfggecffdbffbbddbeababedccdagdadcdfggcgcbegbfgcddcdgebeccfggecbfcceccdcdgfeaecbcccdcagfffcaacffbcadccgceeegabaabbbgefbedfefbffabbfdbbfgggdcgcccacgebfbfbdbeffcdcbdaedgaabcacbcfcagaebgagdccdfbbgeafdeadbbgbdfgffgaacccfeggfgbfecgadefdabegdagccedffeefbcagbbbdfcecddgcbgeeacbeacafabgdcefdfbeegdbgffdcffgdeafbabffccgffggdfdgbbbaefgbedefddeecgddcadcdgabdaaadfgaadcegeecgecceggcggbcgagdfcdfbccbfacgaaeddfcedeafgebabfedcdccfcgababddgbcaaeebdddggdedadcdfbafggagfeagacaeecbcggdgfaebebfcegfgccbfgdbbdbbbddffgadceceaeabadcgeaeccfagfdaeaeceffagbbbecdagcdabfedgaecfafgddffcfecacgcgafeefcfefdacddcbfbfacdaedfdegdcgfafabaccgfeeefbbcgceadbgbcceadafeffbfbegccecabbdcaegeceadbfbgfcgabbgbeeeeaddfgdcbeffdgdcgafddadaccccebddecfdegdcgeffdebdgcbagagfcbegegbaadcebfbabbadegbgcgadffbcabbecebfdaaadbcddededdbefecdcefdfedffbfabgfaabeafcddgaaeeffdeeecdfbecaffdbdfagagdgcafefbcbfdbbdacbebbccefbcgcdaaaeedccbfeabdabcdabgccadceddcbbaddfefdcfgcfggbaafdfeecbfaebdfdadbbcfccgdebgfefcacgfaagfbagbfadbdcegddgcfddcbeadgcfegeedgegeedcabfdbecgbefgcfecgdeddfabcfefefafcddacbcccggaabgegcefbdceagaeacddccceafeedcbeecfecbcfgbgbbceeccabfgaafcffefbegagdecageeabffgeebbabbfbegdfgagabdfcccegfgbbfedcfbdbdfefegcdgaeacaeeaadbbcdcebacbcffaedfcfabdbcbcadacdgbdbfbgbbecgcegedafbcfdacgccgfdedafeeeadebcbfebagbgdeffdebfbfbbeaggcafggccgcgefdecfbbdcbgdaababfbebgedcacaagacfcgbgfeaafecbafadbcfefdcccafbafaaddggaefbeddbbefcdcebdfbecddgeacbccdedfdcedcebcbcddcefccfbdebeaedbcfceadcfbbecbacegcedfdfdfbadgdfedeeeagcdbfbfadegfgffabfbbgdffagbafefegdgeecfgbaeffgddcgbdaccdgaggageabaebbedggfadefdafcbaedeababcafgbfcfcadeafdfadaeefaadbdgedgfdbcbceccaggafaeedebabacdbcgbgdgfgfbcabefbabcedbfgadbfgeeecbdefebabebgfeggfbebcgfdebaebfaafddaggdbbcgdgbfbegbaeddcacccgdfgbfacgeaabagefecdcccfcfgddddgfdgagefdbgcefbbcaeecggeaedcfdffbfdgbdbegaefdbefdbacbdgaaccbeffggagegedcdbdaadcbbadfgdbcaabbfebdddagbaedeeddcaadabgaebdcefgceaffdcfbbbgbadgcebbcccdbddbcggfgaceebgagedggdbgggcgdbaafebcaabgddeffbddfacgbaecgeadggeedcegdddaafagedcabefbaecabgfbdgaaebbbcfebegdcaecbbccffebegcfbbgageafcgcdeceefcbfaeadfbabgegcgddedbdbbfeggabaceabdfebccecggebfdafgccebdefgfgabfbdddcgegbgbgaceaaffaccbecddedagagggbdfagedfcggcdgcecagagddaccaadaeefbcadcabbedbfdddacadffdcddgbegbfabfbffeeecffeacdbeaaddgdgbacabdccebfafadbgdfbcbfcfceaefcaggagfefecgbbeeabgadcbaccdedfcddfgdceeceffdbdgacbggbdefaccgcgeaabggdcgcfafbgaebccgbfegaffecgedecbgedceddabdbceafdbgbgdddfedabafebgafefeefcedfbfcbbdfgbaafaggdgcbaddgadggfcagbdffccdgeadeaeefbdeeecbbfdcdgbeffcadfdafgcccbaabdebffgbbaabcabdecfaebgcaaeaffaeegcfaacaageccdfbdbfggbfcadgbgccbcdacaddgddagdadgfddaceaaadgcddgdfdfbcbadaceggaffeegdbggddgcddgcbgdbgebddeadcdfaffbgdgcdfaacfgfdbabcfcacbgbaedcegacabeeffdfcacgagaaaadfcaefafdgdafadcgbaebafccfebdcfdfdadabadaafgfegceedcgeffeadcfbfaagafgfacceeccaagegeadbfffbdfdcbcfebcaegbfcadaebcfbgcabaccdebeegdbfcgaecbgcfabfeceefedbacgeedfeedfcbddafedbgefacebbccdcbcdcaefbgggfdecefacgeggdabfedffcedfdfeeeafbdacecbeggccfacgfaaecgcdbeabafbfafaffbgddgdcfegacaaeafdcgcbbbcaadbgaagccagdaddaaedbadegbfaadddafggbeaaefdbfaeaagfacgdafacaaggggegggbdbbecebbgcbgfecfffcgdgedcaccdfcaadaebfbebceggbfceebebbgdeffaecfdacaggdadfcbgeeadafabgbbaafdbgdaegaccdaeecgffbaccebbedgfebffegegfbcccfbfbdcgacdgagdfadcafafgeagcdgfgfceagabgcfbbdaadgdcaafeggeafdddcadbbfdefebdafddabagfadgcfccaaeebgaeacdedebefabcbdefbegdgfcfgdfcbdfbgcdegcfafdffabbdffacffdaefffbbbbbgegbfbafcebacgbgdcccdcagggeadbebabgdbdcaagebfbbbabfacbfdfbdebcdebbfadagbgfcddfcceecgcffbdfccgebgfcafdgabcfeececfbcfgcacedeccfeebgbaafdfagdcecdceccggabddecbbcdcbccgcgbcgeeefcdfagaeebbggagbdecebbffdgfbecgddbagdcdeageefcbfgccfeeafcddecdfaaabaebcecgdefgfbfabgacdbdgcffageaaacgacabbedcebdfcbdcafddafabafgbaaddefgdccaacgeebffcbgfegbgffbabefacfdfecefeagaabgddgaaafdecgadafdbfaccgcefcedagcggeeccbbbebafddgacgedceddfddfdccgbddfedegdeeedecebagecefaeebgdgbggafddeefdffdfedfgbeddcadacfbfbaafdgadccfbdeaccgedaedbdabcegfcdebabffeddbcabfdegabafcefegfdaefbfecaeegeabbbfggcfbggbacgddegaafdedgddbgcfaeaacgeabccfbcgeeebfdcaddddgbedbcebfbdgbaaedacbbbcgeabaeefebdfcdaafgegfababgaadaedbfdgaaggcbfceabcbbfgfaebdfgfdadgeafbfecdbgagaabgbbaadbadgagbeadcfecabbebfbfggabgceafdfggggecdfecdgabdgabdedaddecgdfbafdabaggcgffffegefgffabcbcdebfbfaadagbbcbbcgcecdgbgbgdgbdddgbaffbgcbgeddeegfgabedgebgdgcefgbaeafgebfgecdeecfbcgbdaeadddacgbbbabaaacafeadfggccecgadfbcfdaebfbdaabeageacfdgcgcgefagdgafbddfddadegeadddgabbgddafeagfffaefgaabdgbedfcfceedfafcdgegfdcbfcdebacbdabaacddffdbecfegcgcfdaageaddeecegccebdfdfebccdccddcdgbbgaffccabdbfebbeeecaeaegcaddfedfddaegdfgaagdegbeeccdbaacacacddcfgbgfefddbacacbaagffdfgdbbeegfecacdgbaccgagbgggdbccggebddefcdeecdbcfbdgbaggfbaabcdgedddfacegdaadcefcffedbdbgdbabadedfcbfadfcafacgdeefbbbcgagddcgffgaffbabaadfdbgdadefgebeacfdbebbccfgbaagfadbbdedebddeebfdagacegdabbfdbefbdgcbfddbbdbbgcaggbeacccccbbegggedddfbabbcgcefddddgcdgabbegcgdcacfabgfcbaddbbfedefbcdaefgfeabadgbbbaeecedbeaddefdcdfebbbgecbaaebedcdgdefbggebgadcbegbeeedggacabaggaaaecgeaefaccdgbgbfbggedadacdbbfecdagdgdaaaeadbffcbbaeeggdfaddbdageggcbedgeeebcdcgeagdceffaacacebaffbeacbbebffeecdfcbeabcgbgbeeagccegcdddfgdcfbcfaaebafebadgabgdbadafgadcgdbcdfgbbeccgdfeacgffacdegbgegbedeaadcbfedfffeegaecdefcfebbdgabddddcagdcfagaegfddgdcefefegbefdcecbaeeegbdgfacefccfefdffcgadagbbacbabeeaefbadfccdacbfbggebfgaeccfagebddgdefefefcffbcacgffdefgeffcgggcggedafefafabddgefcacbdaaaffdeagdddcggebcfeebaedccaeaadcefgcgagfeebacffafegcgfdacebbfffbfdeagbfedaadagadefabfacceffefggdaacedgeefccgfgbbbbffdbddbfbeaaffbdcbbdgabecgcedbbabdfdbfdddaacbbeedgbdacabdebbbgfefcfaafcfgbafbbbfggddaddbdggdbggefdcacbbfadaefgeeagcgdbffdcgfcecggaadcbgfgcebgfgcebacaecddgggcggbbddgeaedfggagcdfedecabaabdadafgcdefbabaecggdcbbggcgffdbefcdeebgdgbaebcadbddbbfgebaggdefaacffdafdeebgaefcfddfecadfdgecfbffeacgeeadfeeddedggbdfbaffgagbecbfedgbebbcabdcfbbdccagbaaceacfefdebbgaefcfdbeefbfbbddddedefecgcaafagaabbdacgeggaaadeafdagabdgcgaadagecbcdbeeeccgfadeefeddaaadaggffdgdgggfedgbeaccgcaccadggdagcdgdfdbbegcdaccefeeddeagdedaffgcaddbefbebeddeebaaacdcbfbegdececgddbdggbdefdcbeagcbbbgcgddefcedcecdggcceeebcfacebbebcccaddbeffaefaeadddbaeedccaebecbebadgcbdafbbdacfbffdefgebeafdecdccbecdefebdaadbafbdadbeadcbdegbbbdeegffabfeebeeedfdefaegfbdgddbbaeebddcdgbbagdefdcacccbacgbfgcafeegbfcgbfaadgegaccbdgbadeacdffdgacfggdaacfecffacgddbffecgbaeacdcddceaeaegeebbfcecbecbafcfcabdeggbefffagafeaccgbcdedbfgeddebeagfddagggdgadccegdbgafcfceggdeeacdaabbacgfddbegdfgefgddfbeeaaebgfadfbabdfdfdfdbbfcddbdaddgfdebdbabaeeebefagefbfefbbbdbgceabebbcefddffaaafabedfcagaccdgcedcbbcecbddacceedddegabffededbcgaafafbbcfdffbgadgeeabgbgbfggcabgeeadadbddcbafgecaacadfagegdbaagaddbfcgcdeacaefaadbgfedcadabddafcfffddbbfdabbfcbfgbbgdaafcebecfecgeedceagfbdafbgacagabdbdeggbgedddgadegfadeebbceffaebccadabgbaabcbdcfegdecgeacccgeeefgdebgfegbbcffebcebacbdgacafbgfcgaeadadgafcdeaaadbdbdfecbfdbbefffcacedccfggebfebefcceecddcgdafggabbebacegbfadebfdfaacgbcfgacgfbdgccggeafdeegacdeaeaegcccdcfffceabddeefdcbccgbggbgfddcdebageabcdcdefdebbafdebeadcafdeegcbdbaeggbfdaagffbbdedbafcddddegeddcfdcfecccgcfcaecabfbgcgcbdcgcgegfdgcfaacfbffgfddddebdafcbfgdadcdegbcecedfbccbdgddfefegefaedcaafbedccgeccceefbbbeadaaegbbaaeccaaebcdbgdffbdeffgddcaeebggcbbdfbaecbgcaadfgagffgfdaaccdbfcgeeeaaafdgaaeebegccfeaaaedbbddegdccacafffgcbbcdcffdceeecbfcbcbefcfeecfgabeeecggeababegeagefaaeeeefceaabfabdagcaefeedgdecaedgcacbggcddbaegbddbebafcgbffdafdcgfdedgdecdfadfgdeacgebbbedcgcaebdcbcecbcfefbeadaggfgaccbeabadegdaagecadfecccedfacfggfaagfcfcggdcbcaafgecbedbddgbdcfcbeffefeafdbccbfbgdbfdfebcbdbecgdbadgagecffcdabfcfbegggfbcebfcgbfcbeaadbbdacddfccbgabbcbdfbedggdeefdbgdcfeefbgbabbceadcbedbafdbgaggedcdfgceafgfcfcbaeecfgdgaebggbgecbfcdfffeeeeabeabacebbdecbgcbebeeggggbbfgabegadfgefacbbgbdcaggaccffaffagdaeggacedcaeacgedaabeebgcggdaafebdebgecdaabedcebbbfaddbgfdaafgeeefgdeaeeegcbgebfcfccefaedaccegeebecbggedefcegaedfggcadgfdfdgacddbbeeddbgeefbdfadaeacefcccgddfbdecdfgcdffedadgddcgaagaabcecdcgbgfaebccbdgebdgbbfefdgadcdfafffcagdcfcbaaeddabagdbbcfaccfdaacdbddaffccaabadababeagedefcebaaedgbdaeegcfacccbcafefdfbfdfdebbecedbbeagaagfacbebagdccgbaeffbdccfabadfgbgefcffdagagfcgfcaebbfaceccefdggagacbeeabfgcebceebgcacgagegagfcgcagdgafacbdbgadfabfdfcadfbcaddedgdfbcbefbgffgeffdfaacfgeegfaceedfefbgbabacfddbaaefgaagbbaggcaafgbdaacgdadeaeaedeaaaedcdbebbaabbecfbgfbdcdcdcdabdfgaeefgbbaddggcaageeadacfagaedcafaffacbdecgabcccaafbcdecgcggaccededfddbdafffabdgaggbdafdbgccgggefedebcgeefdfgegdfdeegegcddeegcgfefgfffaacfbabecaaccecgaaddaafdbdddacbebdaccgbbcefcbcaggdbdaececdgcacgddedegfeacfaggffeebdfdeefebgbccgbbbddddcbbffeacgfcaaeddfddacdbbbeeebeggedebafdbcefdegbebfdcfceffcdffdcgaadbacfegggeddeagfgbgcebggcecefbgcgeccbfgdbdfcbaaaagbefdcacegaccgecbeaccaecbgeggcebfegadcaegccdaaacadbfddfafeebegadbbbggddbbfcecdggggdcbaecedbgdaeaegaafbacgabaebgceebcgfebdgeegbabdgaccdffcgaacgabcbfacdfgcbaeaeagfbcegcgbedagebegcaceagdccfdbfgceggagfbccabgfbcaaagbcbcafgbbecdbacgecbagcafaaefbdbcfbcbdcbadbffaedecabbagfdcgfdbgaacabbeeecaeffggaaeacaacagdgbefcacfeddcdedgabceecgegbgafddccaddgdfaaefbefdgdabdcggafedaebdefgbcdegcgafffbefdefabdfbdebdceeadcdfacgdacfcgdadfdbgabddegbbbaeafecfcfagdfcabbgdbccecgabecfccedcbfebcgdgddcfddbfddgffdfgdfdfedacebaeccaaddbebbbfdeeaeabfcaeecgagaabbfefaceebbefbcbddcbfbdedbbbbgcdbbccceddbdaaecgfbaddeacfbdbgdgbgaeagddgffcaecafaccfgecffcbeafbdffceedgfdfcefabdbbdgfbdbgfeeedabeeccfdbbfaadcgfddebgcebdgefdgedegaacecabcbfgfegbffggbcfecegeedgacgaabgggbgeedabedbbffcfcbefeafabaeabffcdagggdafbfefeffcdecdefbbegeeeafbgddcdgafbedcbccgaccfdcbadgccbcgbfceacgdgggeabcfddddgbbcdbfecdeeabgbdceegcbedfebdagefgafgdabgbgacfecgfbfefgdgdbeffbecgbbdacadceddcabeaadcacgacbdccebddcfgcbaggafcfdbffdfbfffeddacefeeagaegccagcfabfbbaadceedageeaefgcfdecbfgcggfcgggdgccgagbbffgbdfagfccaecgebbaegfeddfbecbabbgbffcfbgacdggeeeaeecebcfacbccdddbafabbdcgbagcgeedgfdeaeaabefbgcdfedgcccddcbgeagfgfgbafaddfbbcfddddfceefegbeacdfddfdfaecddebfddfcgbfbgaaebbbdbbdeaadbgbfbbeceedcbbafadebegeedfaacebcccdgbdbefdfdafafdadfcbggcaggccebfggaedggedacdeadaeeaggbffebdbbbagdeffdeabaeecfeaecfbggebcgcdbgdeaadbbfbbbccdceadcbbaaagedbbgfabgcdfbacbcagfeaadfdcddcgcacdbebgafgdeddfefdbbfbededegcadcbeecbgceedbcbfecaecadacbfebfeafbffebbdadaafdgafabggedcgbbeffggfdgebaaebfdbabfbfcfaaddgcdbfcdeefaaecdbgcegacbdgeedggggcacebdcfbbbbabcgfdgcgbdbgeeffacfefecggggaccgbbeffbefdcgdaggaafafegbacfgbdbfebaedfedgeefefbffdefabcbbgdedbggbfacgcdbebgedgbgccgfafebddddafbgeagfgggffgdaccdgbagfgfgfcagbfdagadfdfdbbgaagggceagdaccagadcgbaffbddebdggfffbggeaecfaffggdgebeebgbabcbdcdabcafcccdcdadecdfadbgdfgceegffdabgafcdfeecfddcbdbgagadfcbfdbcdggbedafaeggfbaggdbgebefbecgeefcfcgbdeccaecebbebbdaedafgffeebcgdaedfbgbbegadbbfbgbfbbedggecbcaecfbgbebafcagdbgbcfcaacfagfdccfgeedgefdfdageabefgdccedfeffecfgafgfeecaafagdfdgbbbgadffbdbafbaafagddcfgcaeeeabaedgffagacdebdedbgcefgggegcacecdecadadfdadfcbbdfacaeecafdecdebaeffabgdcaacfgfdgeegbcdcffefeccdcffddbcabbgacedbfcbefefegccbbbggcdeaegbbcgddgcdddcfadgdaefecacbabcddeedgecbeebgecfbdffcfadbabbbcfeagdgggbbbacadccgdacebabaaabgdaabfecadfbcdadfbcdeabbggbaeebfegfbbcfegbbecgggbfcfbcgfeddgbgcbfdacbbgbfcfccbggafaccaedaebgagbddaabaadgdbbfbafbcdfecffdbedegfcfdbegcdbcfgcgfbcedefecbgadaffcbbbfccgebbacgfdbceccebdabceebfffffdgaffbcbabcbaecagcgadegefddfgdccfaagefdfcabecgacfadeaafcgbdecdefgacaabbgfedaebcedbcagfegecgcafaeagbdfbadfdbfgaecgeedgcfbdccabgafegdgaeaceefeefcafdfgagfcfbbbaadaaeceffbafggcbbcbcegfadbebgebbecadaeadgafeddccfeddcgbccgdggadcfgcdgddbabdaefgdcbfecabedcedgbfbcdfgceegbbdfacbadecfdcddfeggbaeeecgffafaeaffcbfggecdaccecdffgaeabbgaeebcfcddcdfefeebccbbdbbeaefdcaddeaaffebbeabdbbggdfaeddagfccccebafggaecfedcdageecggbcbbfeffddbbefeeefgebdgcbfbaccffccabcbfaecagadgeeacbdagdbdfdacacagdeeaaaaddebgdgefbgaccfeggececfafcacegagcfbadgaccbdaadagcbbdafaacdfgedacefebgfgdfedgadbcaaeacfadcbebcgdfacegaadaefacfbfgaebgfebdcadcfaceaeagebbbaeccbfgbbeaaeedgfgbfgdeccdgfedeccgcgabcgagfgfaaeeggbabdedffaefgceecbgegbfcdbebacgaffbebbdcceddggaafabccggdaffecadgbaddfaabcgfdbaefgebefeaggacefecfcbcggcceacabggabaadcbabgfcccfcggfaefgbeddfbbadagededbecgccbgggfbfbefabafcbaggecfbdbbgdcffffbbbgdgfffgcfebdafedcdafbfbddgcagafcafcaccbgafgggddebcebgfgbbfebeacaggbgbefbbgccdacacgcabaefceeedcfgfceddadfbedcdcbaeeccbcbfbbfbgacbfgacedgadafbfgebadeecdcdbceffagfgefggbabdeccebffeafbbaabdgaefdbecabegcdcaafddafagfefffedacbbbdacgbccdbabdgdgeffefdbbgcabbcdbgfdddfgadbbefedddcggfbbgbcacabadggfeedcafgcbgdgcgfbbcddfbedeeeddcdfeaddbfbbgdgabfbebacgfgbgfdgafeebadcfbbdgeagbfbgefcfbbeebbdaacgeffffdccdedbdfgbacbdegfbdgbcebafgdeagdaedacdgcgabcdfecddgddadefaabccdafebggbcaadddcegcgffcgabgfecaceefefeggbcffbegbeddgdcgebafaaccffeedgafbggfecaffcbfadcdegaffdbbfcegcadgeacccbcgbebdefcegbfecfcebcdaffaddgdgafegbadgfddabdcebebcaebaagdegeegebabgcbgceddbeegfdeeffbgfdccfgefdgaaggecbeddadgdfeaaadbdecabeecfggbecaadbfebgaaaacfffcdbcggfabaecadgfggegedfbgacgefggbbebgagadadgcfdcdegaacfeacafebgaegdcbdcegcdddbgfcfdeacfefaefgdadfaeaccbggffaaebdfgabdgeadadefdeeddaedebfddbdfdbdbfedbccgdecffcdcdccdcdgagcfeaeecbgaffbdfebecgcfcbgadafbgfadbfcbbacdffeecgfegcgaaacegaddedbbcedcdggbgaecbggddacdbcccedaebgdbfgagbccacbggadfgaabfbfgfdffdffffaffcfacccbcbeaebcddbdggbbgcggdgggbagedccbbfccdfbfgfedfddgbfagbefbbdadddbfadfdagagfcddfbdbabgeacebgfggdeegecdacbgaddaebfacafgcgfbcdeafdaaebebdaaceaaecagfeaegafceaadeabcedgefecdfgebdaeefaabccbdgccbdafdegdafegdcadabeebgagdfabdgcdccegdgecbbadgecbbedccaefegcaddcfdcfdecfgebfcegacbgbdcceecgfcgegcaeefdggdedbbaacfagcbaecdafgagcbdcadfbffaecdcgacgeefgfagdadeadfcfcfbgfcedafdfcgebcgaabcebadabefcgdeaeccgadggdfageacbbcbadfebddcfdebdaafaaddfbcbgddfccccefcfdgaecaceeggbgdegedaffaabdedbdfbbbgefebbcbaeaagegafgcadbcacfegcagbfbgfgdfeecfbabdfecddgddaeacdaabgggagafafdfafedgffbeeeabaaccdfafbfbbafggfgbgaeaccdabadcbabbadbbcagceafbedadbfcccfagacbcfdgecggceedbcbdfgbacccfadefegafcegbdgdaebeecgcbfgeefbccgbdaceadaafgaegfebfcdfdebgeecdbedddagegcdgbaddcgaacegcecfefbfaababfffggefgfeecfcbgcccadedggceeeedfgaccgbdebdgfdcfddgggfbaaeffgbgffaafcgffbefgccecbcgbabfedgdddgadgbagabcefebcegdedbaeffdcegdcgefgbgbabfecbccdfebffggggegegdeefeafaaadfffdeebfceeecgcgfbbfegagcgeebedfbcdbgdbdecfdacbfdeffedgfaffeccccecdebafgedgggfcgcgaebeacgdaeccbedgccdfggdefebaaddebcggdggabfafbegfecaffbcdgdedgdcgbfdbbbdageeeadcafffbegegebbgcedfcfacefbfdgfgfbdeggcdeccdgdbgfdgedecbfaadbcbfgadedfgbdbgdcfddddbcgfggdaadaaddbdbfdfgbgaaaggefgfdafcdgcddgbgecefdfcfagbbafbaccfbeggefbfdcccgfagccfbgfgbddgbbfabeggdbcafgdbddbeabdbagfdbffcfedbfacdffffagcfcaegafffgcecceecbbgbbfadgbgccdaedcfdadgggdgddedgccecfagbccggaffedcfaebabefcgefedgggdcafdbgcgagcfaebgbgabfeebbaacfceefbbgebdcdeaafcdeffcdfgbegecdcgebadbfdcefdcaaefbcbfaebegggadfdafeeabeccabcecbgdgabbbfaabacdeeeaagfffbfcdcbegcdgggcbecfdbcbgaeagfaddcabcfaagffbcdecbfgdbaebacgagbdfdcadagbfcbfcfdbbeegcadebedadcaggegebeefdcaabaefecdeabfccgbffffffgdgecegfdcbdagbbeccacegebdedbbfafbbbddecbadgcagafcdcfcdgfdbddcgacbgfbacccebabdegecedgecfggdggfgfgcebffeceabbcbcgedgdggagafgeeegdgbbedbdeaafccbfgdecaabaefbbdecgggecafdacgfcacbededeeegagdfdecfdcbbdfffbdbedaabddbfcbdedaefcdgdfaafacdbfebddcgcegabffagfbbffcgaafdgbfebdbfccgdefcccbecfdfacffabaeaefbbeggdcagbecedfafggcdaedbabebaafdaeaffgdbcgggcgeafcfgdgfdcbadabcfcafbgecddababfffeaceaacaeggeefacgebfdgbedafccbfafebdgfggfeecefaaacbdgfacbbdfaddccfadbfddffddfbgdgbcfaabdbeaddeeedebgddfafaeebaabacdagacaaeeffdbgagfggeacedgdddeadgdbedbbgdfbbacbagbabeeegedgabbabgegbcefadadadgadgfeedgddeabfgbbdcdccdcebdagcbdddbdcecafdgdbcgfdcbeeedfdebbbcaeccgffdgfadfcfafafeeceedeaagggbgdaefbfbgaecagccfdacabebdcdcfeeddcgadfbgafadegcceeeggcedeeeabededcefcegcbgdbfcgdeaeagafdacebdggddaabeeegcbffadgeaaeefeebagcadcefcdbbaddbcdgfegaafbccfbcbbbffffbfdecfcdfgeeadffgcaeafacccegabffagbaggccebagefgeadcegdbgaeeedbfdfdeeaeefgfgeceddafeafecgeagcdgcaebgfgbbfacbbgggfdcbbeaegggdddbddgfdecaeddcbebeccbbegddefbcgbabebafgbebcfacegcdbgffdaafffgabbdaeaddgbbfabcgbedbbdbdeeccgfffgbfaebgedgbegeacadbeggcgaegbfgffdeggdbeaefdggfaedcfbeeccfbeddecdcfffbdaeedaaeabeecbcfafcgeegbcddfbegdcgcacdbaeabeadfdgfgfacfeacgfagfgggdgfgcbedfgaaccbdfgfcgaeaafgedafceeffdbfeafcgcdgabbddbaecegeccdgaacdgfgdcbgdccfafffccabccdfcggfaeeaggbaccaaddabdfccacdaegaaebbeddfeadfcfecgcdaecbdedbcfbabebefgecaeefcggaeebebgfgfbcbebgfagfccdbbfafafdcddfeeaadbafcfbdcbccabfbefedggaegaceagbdadfbgegcfbebbebbcabbgdefdaaaeebgcfcfbcbbeaddebbbbbgbcbbddggeceffffgeefebgfdgcgagcggcafbagfcaaccgcbfddfbadabdbdeccdgffggdaebfgdegdfgddfbebfcegefgaaacedfaccadabcgdfeffeccfeggdbbgbbafacfecefcccgbfcfbfdfafcddfceegeecdceacafcdcfafdadgdecffdbeaebbagdffcbaaaagffcfagfafeaabdaebfdbbdefbfbgbcgcdaeecagbcagdfddfdgeafedaacadfaddeaaabbgeggbgabbgegeaffdadfceadecdfdddgfecbafecbcdceabfgbdbbeagfagcccgafcgfeffedfdcgcgefaceaegbgffadfeebaefeegfdeaebfegcbbedfddabadgfdbgggcgabeadefdbafcgcaagfgacdcdeagadfedaeebcbffbfbbcfddeecfbgggbebfaeecbbcegccgeebceebaggcadddebfgcgecbfbebegbdbdedefdadcafeegadfgcffaaeaagbefbddagffdagaeedbecbafceecgcedefeaeedfedegffabdedagfdeggffgdfcfcffebgeafeadcaeebcgbebfggdbgeababaaffgadceefbeeddaffgadedfeffeebcbdbgfdcecgcdfdebcedcafebfcdgcfgagbafecbaeecaaccaaddgfcgebbgcddbagcgbfcfdbdafaefbcfdcdcgbffagbbagfdcabaaeeffcabcbaaecggaceeggbeededafacedcdgafgbdbdbacdecdeeeafeeeaafbadfggegfdcaggaddeabcbdcadaaadaecegefeaddbecaccagfbbcebdagdeagffbgcgcadadbbcbbadebdacaeeadeaebcdbgdbaffgbfdfagacfgaebcedfdbbdfebdaeedcbgaebggbdeegebafbaeggfdfaadcdfdaadadbabfceceafccgfbdaedbbagccdbafcbbfagegfceedcbefgaaegdbeadfdbbefabbggabafaaccfagcafecafadefgabaefgecabgbgdcgbgbfadedgdaccgafafbgcfabegabfbecadgafbababacfcbbbgffaacacdbdacfbfdbfbfbceffbbeffddebeeeebebfecfgcafdbebggdagdcfebceggcdggdagfdgaabbddbebdggfegaaggcfagcbbfegebcbccfegbbbacfgaddadefcgdeeggcddecacgaebdgbedgdaebeafedeeaddeabcdbecdaebdaadcedgafbaadbdbebfadfaccgecbeebaeadgcafecffgfagbdbfdggadbdegdfcfddeeeebbdgcfgcabdegdcgccfcgdcegaefbgadcadfgedacagfcegdcgfdacggggcdcdaaedabgcgcbgdbdcafacbfcgageaefaedeebaefcfeeeegfadcbebfeaafcefefeaebfaccbefdbdaedddcfacefcffaefceafcadefcfgcdabaafbbefafcgabdecafcfedafegbfdgfgdcgdbeebbaccfegccccfgfccbdgddccecaagccbeaegcaafgadbaddcbaecedgacgaggaebacdaeacadaccafbffafdgebcfbbbfgdeegcaddgdbcabgaeceeacfdagafceeaafbfcfdbccgfdcfaecfcafcddfdddfbbccfcbefbdgbecdgbafcffgebdcdggaagddfecffgdfagcaagabdeccdagdcbcgacafgacdggdcdeccagfeccddbegfbedfgabgffedfafecgdabdfdeddgbbbgcgcgcfacgeeffdabcfbgabaeedadbcacdfefebafeecgedbefaeedegcfaefbdbegdbacccfgabeddbgabdffaacdeedccgfadecdbgegeaeafabgdcfgeabcbgbafdaaecgebdggdecdcgbebgggcegdeaebffacbffcfccdgadfdfebeedabebccdafaffdeggcdacdbeegbfdagagaebffgceddafdeffageddfabdfgageccffffcdefbffebgffgccecbffefbfbcefaeabdadacgecgacebgbbfbdcabegbeebccfaagebdgcbfdfccdbaagfaagffdbfcffggeeefabbdcbgdafdeaafgdggcbcdagfdgaeabbegeedaeabeddacgbaggcaafegaebfbffcbbcffdgfaedbdgebcdfeedggdbbacgecdefgdebfcegacbccdcdecccabbfagdafcaaeddefeeddgffbaeccdeggbccbbedgdcabaebddgegeabfdgdgaagfeaagdcggafcbecgaebdbbfafafacefcabbeceaadgffcbcdcddbdedababagafabgdfadgbbdcefccacfagegfceggccgfaggbbcceccgfbgdacdadbbfagfeaddcdcfbcacfceabdebdegacdeffgegdacfegdafgbafeafcfffbdcbgebcffabgeedfffcgegdaecccddfadbfgacdbdedcfecbaeafebeebfeggdefcdffgebffagdeddbcgcdbccdfbagfgdbbgbcdfdbgeadbdbbaffgbcbffegaecaefdceebeagedefdebbbceaadgbcggcgcgeadgcffgbcefgccfaadeefgbcafafbefecbefgageccdadefdgbgeaaabcdgfcbebaaffedbffecddaadafgcgdcdcedefecgagbbbcgedaddgbdgdabcbafeebfggefagdccadefgdebcgebedcbaeddgfbdaceefggccdcgfddefdbbbadggdeefbdcgbdfgdabdgcfdggbffddegffffcbdgaadeggeedeafdaaebcgafcfcgagddgbbgfbgaacaeceebgfdggcfcdagdbbfffgfddbcagagdgbfffacebdbdbbebgcgadeeeeeggafbafcaebgbaeggfgbgedgfafcfdgcgabegfcecgcddgdadbfdcbbgaagacaccdceaebgddabaebbdddgdgafcdbddfbgbbafcfbaebcddcaeadbadcegfacbacbfaaebbbgdbgadfdgaagbebafaddadffbgcfafeccffgdbceggbbfgbcgdfgdfcbfacaegbabdagfdeeacegdccfbdbcdbbacgefgcfcaeeccbcfdbbagddcbgcfaefdedgfeadeebdcfbddffgfgcfeagffedcefcccgdafacdfebbgcgfabbcfgeeebaacggfddfgefabbbcgdfaedbbbebcgededbeecfdgeeeccbfbdeefbfebbbeeebecdcdgfcfbggbcgdaadaffedfeccefbdbaddfbddadabcdeefeaaadageadbbfcgccfcebafdbebdcgcfgcaabaddedfagdbbdgcddgfgdafacfaebacfaabdeaggfeffgdedcbbedeaacbagbaffacfdfcaadcffbcadgaafecefbaddffbfbaaedfadgfgfeecddadgdfcdcbfffedbbaeeeedgdccffgddbbdbbfdaedcdaceegbgddadedaefdefaeabbgaadgdgcbdgdefgddebfaeedbedgeefdbebedbdefagbefeefdacbdgabadbcgdbagdecddfafbggbbgfedaabbgfbabddgbfeeebcecaacdabcgfceafafegfebgegadecgfgeeeefbfdgffabggcafeaedgcbafgbaadegecgefgafdbgdccadbfffdbgfbcedafacebfbgfacbbdgaaffceecaegffdcbfagdfffffgcgbeccdccfadddcdegegdfgcaacddgdddefadcefdcdfgddfeddbaaaadbcacaeababbadcegfdgcacffgddcbaacdceffbgadgdeefdcgcedeagafadfbeacfeafedaegecaggfagbcdbddbcaadacacdacgfdbgdaafegcecfgabdedaedebdbdbdagbgdebdebfdbaabbffdgdedaebgfaffgefdcgddefccdeaagffbfgfaacbebgcbcgeadgfabcacdgcbafcedeccfbdbbfbdbebdabefbeaeadagfeceaefdfeeacbccgdacgdgfbcbcageggdgdgfddbebbedcddfdgdceaeccdecdafcggdcbegbdcecaaabdgggcdegdcedeceaggbgcbbccadgfbfbebaccbefbffaeafabeeecacfdgbgfagdegecdeeeaebgdedcbecbbefggeeacacefggcgadbcgaeedbabdaeegdcdcfcefbgbeaeaeadcfcggdeaeaffaggdggagagdgaagbfcdaccdegdeefbabcdaaegbfgegefdgddabaebaegacgcddefdafdbcfdgaafbdedgbebcgfcacggagcbdfbafgaggecfcgefbfbfbegadabagdgdggcebccdegbgacfeacagfdcdfcfebgfacfcgaecfaefecgfbgaacbfeegecdbbffagdegdgfeafcagffeefafaeadacadagecfgcddfbdfefadcgbbfdcgefcdegaafebdbddgcecfeggfcggbceageffcfdabgcdcgdefcgfdddbgcgegfgddabgeefgedgdegdcfefddbccefbebegfcafbdafeeggeagdfffbffcecbdfecgcefeacccdadgaeffdgddabefegecgaacgeeadefbgdaecbabaabfecdcaegbdbacdebgadbgaffdadffcaedbfegffggabfdfffdgbbegdbcgbdebagacbbgecfffcfdedecbabgeeafbfgggagfgecfaceabfbaafcgegcaecfdafgfecbgdgdbefgffbefgebbaefecfgdgcfgeefdbegddbdabeccbfadddacdeecgcdebgeafgfbbfdbeeffeaeeagdgbcagbdbeccdedgegdacbfcfdbffedccageccgceccbdcbgedddefdcaaebgabcebedggdcccdfcegafdffgcbgfbgeaebfgffeefceffeddgcfgcbfedeaebdddddcddedbgffgbcegdgbeebegfggaedbfgfefgddebcdabcafbaffdcfffegeebdeccbfbbeafccadedacdeebedbbebbfgafdbgeadggebgfcfdbaggfgcfcfccccbfgeafcgafbegaeaffbddeggfbgfccdcfbgcddgeadfeeabfgdgdebdbeccbfggebagbffbceadcfdbdaedeaabebdceebdffdagebgeeacaefdefcagdcddbbfbgcgccdggfdbefbbdfacaafeadcededfbagfbdfbfeefgbbagadbcecddcbebdebgbfbgedbfdaegccebfcbcfgdabbbafecedadgafdbbgbggcecgcaggceadebbgcddgddcbaffccgdedefgaeeagbadefaeggbcfbaeadbcebegafcagaffcfbegfbbabecadbdegbdeecddaedddbdebaaedffcccffadacggecgbgbeggfgfgggbcgagbcdcddegffgdbddgbgaggedfcaddbbdagbabdcgadebcfcgaeeagdbaacfbegceddfbdgbbbcfbdcaggbdcccbdabccadegfabccgccbffebdeaeaegffacbaadcbcgagdbfdgfcfcfebadccdbfbdbbdcbfafgdedecdaeedebfbcfbeeafeaacgebbeegeabcbfgdcaaefggafageccdcbdcbbcfeaeeccaebadefgdegecefebgcebdccgcdbcbabeabdcddadfeecebaeaebadaadffcadaagcedcbegdabaggfgeeefdfbebaagfaffadebfaggggffadggacgdgbdedfgedcbdabcaebcabgaacdfgcdbdcbadegbgbceddgecadbfeabdbdddgdfdaaadedgbcaedddaecacaaeagbgabdbefaegcfecabgfgfeegfgccfabgaggabgddadbfdgbeefcgfffddbbeafdaecfbeceebggbbfdfcfacgfeeegeecdeedacbeeeeaabadeebdddbgegefbbdbcggeeeadfagbgadfagdgbdcdgaddcdfagcfgadagcggffefgddadbfdaeaebbadefagdbfcaedgcaedgbagfcfefebgdggdcecfdfgfbgabeaagadebcfdbfbagfedacgcedbeebcecfacfdabddefagdgecbecdggfabcfdcgaeeacfcaebgbgfbeacfaeeaebbcdfcfbfbfaeacfbfdbgccggfgegeegdegaeecebfcbfcgabfbgbgcgabeadbcgdgbfecaacaedggcaggadfgefdbffcegcccgcccfgbagaaedbbdaagfbaeegaeeebaafbgcdgcddcfbddaaccdcgdbaccdgcgeaadeabdffegbbafebggabecagcfdgdffbgdeagbffcadcbbggcegfdfffgcbcdgfedbceeafecbddcbdagceccfgeacdgabbeafgabcbfcebafcgaadcdfababbaegdafggdcfgdfdabgdceaddgffgbfecfegfdacfgbbgeegfbcbggaaedaagdfcffcabaaaggcbcfdbacbfefdafefadcgcfefdffdffeccfdgcbfdefbaaagfbcgcedcfedddgecbegceabfbdgdggcdebgbddafdcdcbffffccadfbgdabaggdgegcbfecfcfbfgcecdbaacgcfbeadbcgcbgdgfgaegbbcadfdegefggebbfeadeggaagcacagfgbedfcadgdeeecddaeadfafbfbbbagbcdedagbbbeddcdfbfgegbdcdgcgcegggbageagagbaebfddccageaddfcfabagbgbcaddabdbefbggfgdebecaaddbebabddaadafafdfgaaccebfgadgacddccbceddccddbbcafgeecfbbgfgbcabdgbfffffdgeggcdggdfecabefedcabdfffedbcffgdeceggfedbgdgcadacgdgbbgafaebfegbefcffggcfbfegadcbbcadcfdfdgfaedbbdbagdcdbbcbbbacaegfbaegcdcbaaffgdfecceccecccbegggbdafacagbgacgaggffbddbgaaafcaaabeecdbfegdbdcbdfedcbcbafgdcgfaffaaaegccagcagdbcacfgggcebebgdfecedgfbfgdfaebggagfggdcbccgaddbfagdcedbcaffgdfebbadebfcadggeccfbgcecacgadbgfcfaeffedfbgebegdedeagcafdcfcadfdeaageedgadfgaedaedgdfcabacdffbgfbdafdefbbeedfgedggcggbaedbcddebabgcfgebegcaagdaedbfgacfcbdcbdabdfagaegdcaacabfdedebacfbgfgabdddafecbbgfaecaaafcafefefgfbffdgfbgegecbcafffcbgbcdecbeeccaedefgecgggbaddbdcdffaagggebfcdacfccgfadfadfagaddffacabcdgaebgabafccbgfgbcgcgeegbeeefefagbfefedfffcbgccabfbfddfccgabefeaegfaeegagfebdebecdfgbcfgcccdaafedgeaedbgcadedbabdfbgeefeadfbbbabggbaadggfacccccdfaffdeggdfbaadabcfbeceabebedbbefaeecgdggfbdceebdbfcefbgdddaacbadfbedcfaegabbeaacfbddgcfeaecaffeadbgbeddcabbfaffdfbabcfeaecggeaabadedgcegaggcacbddeggdabfaabfcebabcddcfcbgegbffgaaagfdegbacbeafbfecgeeacgadagcdabggdaccbcgcfebaebedbedfafdgdbddecaecceggcbbeaebadfafbbccddebbfbgfeagfafddfcaaedfcfcafdaegcdededgbacfcdagegbaegeadafbgcafegcabdagbfgbdfafbcbgbcgbfcedeagabdbacdefbeefgddcgcdabedbcgdbafddfbfbecddbcgfggbegfeeafbggbefggacegdcedfabfddcagefafgcgccdbgaagbcccgabfcdgdbefcgbgbcbfceeabedaaccabdgbgabdeccgfaeaedfgeeffbacfffgafefeaggcgfefbgdaccbcbbefcdcafbeacbeafbagbabceagbcfgbgabbefcgbcccegeafeceeeggagaggbgegdgebaebddggcfafdebdddfaeacecbbaffbgbaagbeeadebbcfcfdedcbgedbfbceebfgefgggdcddbcdfgbedfdggaabffaaffcgdgbdcffdebecfdgdcegdececacfebabdfbegeccagffffdaagbfdadfdfaddagdbceacbcecfbebeedcgagfaggcadefeabbagacfegbccefegfcdcdededceefaefefgdfacfceebggacddaggddfddffgacccfffcgfdgdgegfefbfbbeeceafdeeccccaaedcfagbagffgbddeeggaefdgaggedecccaadadefadabfecadfaccgegdbfdefgdgdgbedagfaaededbdacfdcgadcceedcceddcccccefadbfgacafagfcaagfbaaafaagacbcbcbaddbecbdcddfbbdgcfabbcbfdgeafgceggagccfgcdgdgbaafgceaccegdgbbgadgedffggdffdbfccggebgecabfgbddegdgbgbgbacfcedaaegbfcagegecbbfaeeefaacdfacgebadefcbbbafdeegfefbabafgcedafbeggefgfcedfgadbdgacgdaegeecfgcfadcddegeabffcaadagaabegbcedeedfeadecebbcbfgabdacabfgcdcccafadgcaeefgegfcfdgefafdcbgeaddfcbcbdcfeabdbdabgfgcgbecbaaaegdfcagbfggabbabdcggggddcceccbaddfeggffegcbgbddgeebecfdfbabefdcgabgccdfgabbdfcfbbfggcdcfdcffdfegegafadaebdggadbagaafdaecbfbabddedgedbbabdedaadbgdcbeebgffagfdccegbecdcadgadcaacbegffcgadcgdacaeaaddgddgbbcbadddagggddgbdgdbgcdedecdffecdcabccegffcagcadbgacfeggbdegagacaedgfgbecgacfcgecbbbgdfeedgggdafadaaegegcgdadcgdbgdadffcdggfddgafbcgcgcffbagfgafebdacgbcggfebgdgcbcedbbffbfaegacffbcfgcbgbgfffbfbbdadfdbdagffaegfdcbcggefddfgccccddaebcbffbgeadefaggfffcbbcdbabbdebdedgcgeccggdebaecdeagebdcgbdffgegcbcefeeggdadafaeeccbbaebbdfgfegebefgffbcfacbaaefgagbggegeeadeagabdacccaaaabbcaabbbfbgaadadfbdgggcfbcefgdagbacaccgcgdaeafgbedcbcagfafbagaeaabcadfafgcegeffadbedbecgdegdgbaaaegefebgaccdddgcbfaefafgageebeeadgcbebdfafgdggbggcceeffaefcgbaebecfbbfgedacgdadbafbdbdbaafccecgdbdcfggcdabdaddafafdebeacbaabdcfdcebefbgbgcaaabfddggdeggbgedbgagdcefdfcgfgafacgdabgfaggffeafffeaabadgbgebgbbbdbfggbefbddfedggfbfggbbcbfdebbcagbfgagaagfgccgccbedecebbdebefcfeeddgdageffgdcffbacadfgaabdedcbgaaagdeefceadebdbgfaabfegcafeadccfdfcadgggddeegfcfaegfacagbdddbgcbaecdbegabefacgffcffaddbccdefecaaafccbbgafbbcbggfefbeabagegdfcagggadebdceecffgaegdeecfdbdfeeeeafdcgaagdfcbfefddbgfdecdbacbafdcceegdffdgeddegfdefbdafgbefdafdcbbeeegegecbgbgccefdfaebcdbdbdfbagffeffccffbdccbabcagaacdedaaabfdafffbbdeaccbfabgbbcddfaceebbdbbdfdcbbbdaggdcecffdgffdceeedfgaegedagcccadfacacffggcaffgcbggagcfdccfegdabafggaaaegbcbfgadfdbdbafcgebbagecfebcbaceagegcaaecabaeadacbaccdfdfcbdddccdgeegfgbbegfcegfaedbgedafagcdedfcdagaabdfdeedgbbafgafccdfcefgeagebcdfababbaafbeebegcfbcefdbeedbccddcebbfagddaagbgecafffbbgfeebedcbecfacdbfdbccadcgaccdbbafbcdedbdceccafcdaadbedgacbgfgeebcfdaffcfgcdadbdggdaaabfbacgfbffcefbbbddeadcgeccefeagadbcccfbadbacaegccgbabbaegbcdfefdeaaafecfdaacaeabbbdgfagceafbfggbfcegbdefabeeegadbfgfagbdaebbededbcbbggfcgfedgdeaefebgbebabcgfcbbdbdcbbceeedaaecggagcbgfadedfddffcaaecdcbbgcdcgbdcfacggdegcdcfcafcgfggcfafffaacecgabacfagbfaeegffbgcfcggffafgddgaffdaacgbbeeaeedeeafdfegaaaacbbfgcfbeageaagecafaffffccgcbgeadebabdgbdefceabbfdcbeeefcadfbcadbgefebfcedffeafbaeceacaabdgeaebbfabeddccdadbbfddfageggaecgcgffefedgdgbacbcgbfffeagadcfbddgbcfbggabaecfbbfgabdgfaacbfaceggacdfdcegecdgcggddgbecffdbcbefbbfgffaedbfggdddafefggedgedccbdbgedcgcggbfgbgdbbgbebcdaeeeefabdbecdfdbgdefeefbegaabacabbcfgafbggegdcfcecdecdeeegfaecffdadceggecbdbfcaegdeacbagbecegedagbdcgfffacgdcgcfgbeeebbaabbfbggedabgagefbbfafedgabceegadedbcgfbddefdaccfdddcaegaecgeedegbgcgdedcgdebdecadabbdeefgeeaeddccfaggbadadegaecaggaacaecgcbebgdgdbgbafdgbgfafbffdbfaecbfdbeeeagbfacgafccffgfccfegcgdbcdgfaecbabfafdabaaagbacbeeeeagcggbbcabcagffaeebfgabgafabgaadfabdefafbadgcfbagaaddbeegedbfcabedbfaaefggbdgcbbgcaabgefegbbfgfdcefbgabgdfbgefcdggecebcegbgegabccfcedeaddbeffgfcaaggedgeddfbdfadbafaddcggafaabcbaeaecgdddbfcadfgabdcgegeabebgdfefdccggdbbbgabeacfcgcggcefefedbbcfbbcadcbdcdedbcggagccbdgcbceffeedfcgdaeecfeeafbabeeeabdfefeadegffaddaafbfebgceaffggdbgfefbcfafacgbebfecfebgffaaagebbgageccggcebbgeebbfffdedbcbcadcfefddededabeedbddgafdbfddbbcccggcgeegagebggacaededacgaafcfbbcafdeeeeggeadeecgfbaccbbeggbbecacfgaeeeabcgcdadfcffgbbefdcbdaecegebdbadegffddbfdbcgedfdbcaaegeaafaeccfgdcagadcgfefcdebbffbcgdadegafebagafbabegdfbdabfcbcbdfeeccafffceafebfadebcdbafcceaaedaafffbegadacgdgbdefcefdadbcbdefbebgebeedfcabbacdeedegfcfdgcdcdagfbccbagcfdecafedfagecedfageabadcaacfccbffeeegcdbbeaadbcbagfbgfadacabddaggefbbcdggdbcfeggaaeeddecagbgfbebgbbdddfefbbfcbfffbegcafbfbffeebafgfgcaffadadceaegebefbeeagbdfcdfcgecdbbdeffegagagffgafadfcdfbefecdaabgbcbefeeacabdgaaecaedceacageadgcgbfebdcefggabbbeggbcacgfccdcceccgagdbgeggcedcegbaedgfcbbggagagdcbaaggedbebdfeddcfcdgfdfdgcaecfdddfbaffebfbgadafcfbccfabgfceebceacafaaacbcfdaacbbdbcdcbfaadacdcfcdbfdggfgbgcgddaaaccbbadegbgddeafadcgecedccebaddcbbcegfabbbcedbcbbccggdebffgaaccfagagafdgabbebaeabddedbggdbbfafadbeaggbfcacdbadddffadffcfggbabgaeaddfcfdaabgfeagbaadcbadcfaaefcfdcfaefgbefffdfgfgbbffddbaadddgfbbfgagffeddffefcggdbeegfgbbfcdabcgccecbedbaeafeggfegbdabfcbfcaecggcedcecgbaeabeafffacceagaeedcfbgaafcfbccdcddaacgdcbeaeeacfgdagaebegcfaaagedfecccebbagefdeeeabcdbeegbgbgcagbbcegfacggdfdedfebggagafbabgcaddaebfaedbcfdbfgbaffefbggeebbbdgcbedfcaecgfceeedagcdeegbfaggabfdbegbaecfbccagebbdbfdfedbaagddgffabdbdcdgdcfgecfaebbfaefgbbaeaafagbgccabfdegdaaeecfddfeabeecfedgafedaegabcgcddcfcfgegbegggbfbgabcbeefcfeebeebacdffefddgfggaagccdbfccdddcafaedccbgdcaaecdddacgcfcbcbfbcebeecfabddddbddaabfedbbbbegcecbgbaacfcbbbgggfbacedbgaefgebddfcgfacbefebegcabeddaedcbaedcacbfbdefdafggdbfcecaeegddagbffaffeaafcbdccdadcgedagefbacdcgadeadecggggcaeeaffbffdffdbdcddbdcfcdddffgfdgaaafgdfddgaeffcdgfaffacbebaeedadeadddcaabbedecbfcdaafeggdabeafcbadafbegadfdgdcgcdfgdcegdbbcccdbagdebebffaadbfagedfeffgbdcccebagdfbefbeebedeafaacdbedafdegeeeafbagdfedfbagaabdbcfdfaaadcbgccbebfdgebaecabgfcddcedfcgaeeceeagccgfddcafbabbgedddddceffafegfgbgagdgcbdaecdbggadeeegbgcegadbdfcedfggfggbfafcdeacaffbdfdaaddbdfbgebabadgbaagddedccaaefaadcbabeeebccgaedfgfabdgafgbfacbdbefbaaacgdaeebcbgaddbebfgegcaddacegbeafgdgeaadacbafecdagafbdgefbbfefedagggedafbedgdbeddedfbeadgebggaecacadegbffcgadcbadbdbcegdecfgcfcfffafcdfafagffedbaabgecdbgadbcafdfcaaececedfcdgedadacfbegfddggabadceafbccffbccedfbddbgdgaafddgedbbgebcadfcdbbedaaadcfgbbeeddafcfebedbdddbbbdbgdfeeebfgfbbedcabfffcfgcfecadgfeebdgccgafacedeadeecdgcbdgdgeddffgfefbadafadecceffbfabffcgfabbaaebceddfgbdcbaeacfebacagdbcggbecbefefgfgbdgdefddcbbcdgebccdacaffaabdacbdcbbcfbfbdcafcfabaaddaccgaggcdgcbacbbfddcfgdgbgdbafdafbggfdfaagfggffbcecbbefefdcdcdffadadaceedagddabfgffefdfgddgbabaaaaagdegafbbdcegcffdefbdabddbdbfefegeaebegcafacbdbdgdfccaabgbegcecgaacagcabedcdeccdgeceafgcdcfebfaeebffagdaaaddbbcffaffbddgfefddgccefaegegcgffgaccfgegbeegbdceabgfaeacggbeebfeecddeefeaecfdaacbggccfdbegggbcdgcecccacabacafgebggfeaabacdcecdfffbcebbacfbbgcdacfgecddagcbcaddbdagaeabgbgfbfffaeeagccdbbbcaedddfgcdfcgcaegceccbfcegfcddfefbfffegegaagaefgbbddaaebdabfeecaafcbcdcaccaddbedgdfebcbdagedbagadaggdaedacfcafecedfcdafgffdebafgafffegbbagaabccccgfddcgbgcbcdfcfcfbadffgcaecbdeedegfbaagbfdbadcfcecfgadbfedfebffbfdaefdfcfgaadbcgegcccbcfecbgcfbdcceddgbeaeagadbdggbgdgceddedfcgcafcdaeeebgbebdaffebbcbgffgdggcceabcgbfcbfafaebdebaegacfbgdeddcbecegadabaebaffbbaeeeceebgfgccbbeagfcdeddaefcdaeeaagecgadfabeaebbbbebfeacgbaaafaeaaacgdcgcbfedafcdebbfacdcgecdgcbcfgbdfdaceecacddegebegcgeedcgfceafcgecdgecgcfgecdcgfadfccbcdcgaaacgdabcbeegedaeedffabfccgbgecbgagfedaecegaecdbaagaegdegeaeaceafebbcgfebgddefagebadcdaadeafebfadgccffegfeaddbfgcfbfeecfdeacbecgbcgdfeccdegcbffcadbccddfcfbbfdefgbabgafddcbfcbeacafbffdafaaefecfafdabefcgbbbededacbaafagccfgfcebffbdggcdafgcgcgagaafabdgddfecfcfaaccdfcdabefegaccfcebaeabbfcddbdfbggdfedgabcdadcacbffcaccbegdgdbbcgcdagdeefgafddcfaebcaffbaebdgdcfdggcdaaagafcfgcafcbdcbgacedgcecfagggadfgefabegdccdegdgafggdeccecbagcfgcdgeafdagbadfgbfcbcgedcfdfbgffgaddcaaefeafgbbgedabcaeegcfdcbgcabefgecdgbebaagbbcfffedgeffffaaggdgdegcafegcfebadgbdbbbgaacaacaefaaagcfcffgcgbgdgffgcfceggdfbabbaebbfbeegebacfabgecgefdafbdfgaccfdcggbeacebdbaefbcgbcegddcbffedcaafgdgdacfdbadcdcdcdgbcfeeccbcgabgddafeddeddcebbffeddbfecadgfefgdccceefbbfeffeacgddbcaeafdbgabgebfbccabdffeaeebceagegbadabeebdcggcebbcddbcfaacaacbefagbaefagcdafcbbfaeecgabdfcaeaddfccfdagefdffaacedcggcbfabcgdgcagceecedfdgbbdbbadaccagdgdaegagadcafecbeacbcdcgdeadbggbceccegceacdcegdgeecacggfabbgfbaffeaegbdfceefgdeaddfgbcdcbagdddgceagabbebefebdgfdddaegcbacggcacecbcbcccgdbbaefdcbdccfeabecbaeabgcdeafgdfeggeabfaaefdcadcfdafbafdfdccfggbcgcbcagfdbeadcaabbfabedefbdcfbcceabggggcefeffgfdgdecdabacaccgbfccefagfebebefceagfcccaaaeaacfeeffacfbbbfdcdfffccadgbecebgbfefgdffeegcedabcgeeedbgdgdbdgabbbeedgbcfaabafcbeeffcabfbfddacaebgbfdagdgfabgfgegcabfedgfedabgdgbfcaaggdfdbgegcecaagagbccdabbbecegeeebfbgfgfdfeebfddaebdfdgbbbcebedbcddeeecgfdabbebegdbcffcbdddbbfdbfcccdccdebdaccaebfcaecdbbecacedcfcdgbgaddecbffegbbgaefacaadcagfdbefgffecbcedacbfacddadabagcdfffbdcbcbgcaccfddgcfggdfggbgadcgcddadaaeffgbbddffefbdagabcfeafegadfffggabcedbeceafdebdgegaffcaefacdadgfbffgedcdcaeaccfbfaadcbcdgfcdgfdagdbgebbabfdabbacfbcadfdfffeefcdabadeaefbggddggbfgggecedadaadadcdebgeecdbdcfbgebefbacaffbeeagfdfagfabgcgfefbgfddgffdedaefgedffbeacadbcbdfagaddbeedcggdceegbeegefgecdgagbbdfcffgddbcebcgfedcdecgdafaedceffbgeeacebaaddgddagbagagaafcfgbaaddgcdgedbebfebdabaegaecadfaedcdeabbcgbggabegbcdadffaadgfddegbefbafgabefgcgddagdecffbadbgdfecdagdgbbfgbfbedaddacceagbeebaddcfbdfdaegedgagabbbbdfccabgbgfagdgfcgebgbceecggfbbccgfgcbgbefbacdcccefafgdfgbdaegeegegedebfecadadgfgefebbfffdfcefgaadbabeabdcgefcggfedcgebcbddcddcdcbccdaefddefdaafbdfeggfagdceadegbegbagbaeabdfdaagadaeecgfaedbebcefdcgcgfbgbebaggefagefcfbafdgaaebcdbfbbefdacgbfadbaadffecbbaggagefbdffdedgbeebcdgbdbfdaaaadgeabfeadefcfccggeadaafacaadegbdeacegdedfcgbccbeefadcbdaddbbdfceefabgffaggeagggebcagcddfbadfgfbbfadcgfcddeadfeaeeefecebeefgbafggcgabcabggggbggabaacgegadbeeedegcdeeccgedafafcfgcfebageebacafgbfedcbeaadbdaagggacffcafefegbeggcdaefgagfaecadccdfgeabfeafeabbbdafegebcffdfddeefffcacabafcccabfgadadbdccdaabeeegacadcfdfegfcgbddgbffgbgbegbaceageeaedaaecadbfedbbgaecdcafffgedfcbeeacdadacdgeccddffbacfbadbaedbcbcddgaebfgbdbgggfgbeecedcdabcgebcbedbgcafbccbfdegbceecgddfcgbbbafgbcgdebcfbacfcbcfdegcdddgegbfcbebeeefgcbacededgfeabbffecgffegbeeeafeeeacbddeeeaebddeddbbabdefbaeegccddgcgefgefffgfgfcedafaabeaccffdbbdaaceaafcacbebcfbcfebfggebeagbffadaddafcbaagaggcgdcaaedgcbceecgfcggecfdbadfbbbddceggaaebffaaggbabdcegfcagcfbfegbaegbcdadbadgecaefcbdcbdffbddffagfbgafeccagcgbfbbcdbcegaccbccccbdafcddegfgdeeeeegddecaggfabcfafedcdagdbfbeaacgagfedfggbfaegcdcdgageeaafggcffdgadgfcgaegbfbfadbfbebfafcbagcgccgaagdeacdcfbcecgeddaecceefebcacgafcdedbeecbcbcddcfedabccgeafffccaecabcfgabfceaadafefegddeeacffedabfgebacgdgdfgccaacggbfaeacegefafefdffbceceefddcfadceaggegbcfdagfadgfdedcefebafbdccebbcggacgebffcdgdgeddgadffaaffaedefbfgggeebgfaffdfdffefefebbeabaegadbaecfccaaeffdgagcabgbcgacagcddbgcffeccafeaabebeabbbefeaffbbfeddbbcfbggfgecgaeaegdcaddbfcfbgeceagdffeagggcgdfcddeffbacbebefdggdcbeabfaacfebaegfbaebagdageedfccagacfdbaecbcddgagdcbecbefegadbaaebefccaecffgadedecbefdadcbgabcbfefdabecfdcfbcbabggefgfdgcbdfabebabedagfbccefgggcgacbgdebadbecaagggdadafaaedfbcbfdedecbegecdbcgbbdagcecggabbgbfdgdcffeaegbbgfaebdfdedfgabaaffdbfgaaeeagcbggffdedbgacdgeaafbfcagccfbadgeebffedgedeadddaedegcgecfeaeeegfbaabcfccfgbfebbbeabeccdcccebfggdecfbbdabgcaadgdgbceeaeabcadaebgbdbfdeaafbbaecbeffdagbdgegafdbadfefcabacfacaggececebffgedgdefaebgcaaacdaadgebddecfaddfdggdgecgcdbafgcabagebecaddfadebgbgddecbggdfdcfgafcafgdcbfgbagcaacffdecddbabfeabgecgbgeeecgbgabgdgagbefaaacdaeaecefaecbecfdegfecegbcgdccdedcdefcefeadaaedbfdceaafefbdccebbcffdebagccbdecaffddgdbffbbbefbdfdbbcdgfecbbdacgfgccagaecggegggdfffaccaagfagdafedgbffededaebbfbdccfgadbcegbeacdfdfaeacgebccbegcbbfdgcfcdfaabaaeggcaaedfgcgfabcgfedgegggggbdcacgbgdgcabbdbfgbbfeegdeeebefeadafabecfdafgggecddbbbaecebbfaffeaaedefgceagbdadaccaafcegaacfcdaeaddfbbbadaadebdgcgeccgaagdbadabbecadffgefecfbafgcefcbbfaefggbfacbdfgdgffbgcdfbfgbadfbgfbfadbbdffcddeefagccaaacgfgcceabccaabgcdafgbdgcbefaggedcffbbbeaedfafagdcbfbfagcegecgegcgbgadgcccbgdeagfgbgfebegebffcfcbgbbgdbeceaaeefaaffdgdgbgfaggbeegeeebecbcaafggfaecfeagedcbebgdcbagdgafdbcegbeeffggaccdbbgbaefgeabcgbbcefdcceadbddecgagaedcdbabbgcgdbbcegcgadfbggbcefdadgaafgedegeeeadefcgccccabaccgcdbbbebfbgccdgbfgbegbfdbdgbbcaeeaegbcbeffdebcaefdaeccdeeegdfaaeeeaafcdccbddggfaefcebcfdecebfbcebaafgcgeegdfdgdcebaeaggbffgecebccfgcbgcbgfafbgeeceefaeagceecfcdffffccabeeccebdbgbedcfbcadffceafcbffegaccbdadbcgdbeafeafaaaacfbgfdaadcgdabbaccffabgabadgbecdefaccdaadgfbdgaccbfcdcfbddfaeaffbggeffgcceddcbafcaagfafecebgdacdggfgfgbdefbacbaebcddceedfgdgeddefbecdbceacccdeeefebgccggfbfgdbcdbcgcdfeggfcgbebfcdggadedgggdedgcfcdfccgcgbbaedeegadcbdfcdeceaagbdfccabgfedcdeaacecaebbecegabafdcbbefaaadfeegacgebbggfcfbbbceeaebabfacddcacefabdebdbbbfbfdcfegbddgbeebcaaedfefdeddcfbcedgabfdfegfeffcbcccefagfgcfgfegdbbcdcggdggceecdafaedgeaabgcecgbaggafddgccecafdaeaebbagdfdgfdeaecbggedafcagccfgceaefeafddbgafgbfdgedfababaefdceeefgefbffbfdedbcffbcbdacdcefedebaebagddgeafaaafdgcdgaebdgddffgebdfgafedagabgfgcgbaeagebfbbcbgdccbfffcacfgdacbcfcdeecafdefdcadbaeaadgfeecfcdebegfdagaggdbgcfegeaeadgagfccacdccceagabaegcfdfcffeabgdagbedbdaagadbbfgcdgecgbbdeabfdagdaffdeegdfcfcdffaeddecgccgaaebaaceaacdadfceefdfddbgceffaaceceedcbffagaccdfceafabdeaggbeegfagcfeagfcegdcecgdfadfdedbebfgbadcdgggdbfeaeabacfcaeegagbbaafefadafcdffaggaddeegefefcbeefbbgbaeedbgcaceeaceedgceebcafeadbegbabacfgfcabfedbgcebceaegdgcbeebddgaeababefdfgdeafcabbbdgfdabfdaaaaaebdgbfcfafffbggedebfabbggabcbcadegcdabeadfdcacedaccdgcacggadccfeggeacbcgbaebbgdcgadgecefcgbacaeecdaeadbbeafgffdbegddaddbddebfgggdaedbafcdedccfgddegcgedccfgabdgabcccbgegddddggagggdcbacbeaagcffcdcffgcfccegfbbfcfbfbfaggdeggbgagdbcadaegaegdegabgcbdafceadffacfaeeacdgffafceaeeffdeggfbdbdaeffgebcdgcbcceadbcgdebgdcebdgdcdbgadgbfcfeegbfacccabggbefbeffggacccaagbadgeddfbebdffbgebeccfeaadafebfdabaebggdfddafdacddgdaaddbffabbadcfdfbcecafcedgccbbcgcbeaafaeedgbgggbbdaeadcfcacdefgbcgcedgffaecacaeeggggcabgfbfcbbbafgcbefgebdfbdcfffafdefgbeaeabeebffegbedcbeeggdceeddfgccbeecdeecdeefgfaffaagfdffedbegeabdgfedcbfaacddgefcgecfdfcadcbffgffegbbgabcfefggcbdbgcacfcgecgeeeffefdegbagdgacaagcgaadaccebcbccgccegdfbbcdcefdaaeafeeeddggcbcdfcdcbbdfcbabeacebccfccecgffgbeagbccddacceacbedfefbefffgceaefafdgcdgbdafegaafdcedgaabdddcadcfedffbgacgfecfgfbbefdgafdcaaebccagbegedgcaggcfddafcccfdcbefefbagbcdgebdabgffgfcbbgeedagbadgeddbbefeaafebdbabcdcagbgdcdegfaccdffgdbebcbccbaacedcbgcabcfceabcgfedfafdfdfeggebagcfbddaaaaacffcagfcebfgecfcbgeacfefgcggbbbggeedacbddbaffecffdceffdfecfcbeacebdcgeggefgefcegcffbdggdcgecccbffbeacfagccffeegfcefbebacgfffegcbdfbceebgfgebgdafgffcdbafacbbfefcffafgfffgfedgcbfdbbgbgbcecbgacdbcbbagceefcccaddeaaegebfefgbgaeagbcfbcdfeacbaedfdfbfaeddddddeefegdcgbdcabcccbgfafcddedaacgcbdbadaaeeaegfceaefafdegcceaccedgefagfbbaaabedfgfaebbadcgbdcdecdgbeddfbaafafgeecdfecgcebafaacdacabbbdbccegcceefbbaefggfcgdcdaaadffbedgbfdfdgeeagacbgaaedfdbacdaccaagfaffcagcbcfdbagebgggaaddaegdefgebfdfebadagacgbaadggbbgdccbfefgagfbegadbbaegggcddggfccaefaabageegagccgbdafebabaadfegfebfdfbddagbegfcccedfgcegacagbacbabggddadfffdbfgcaccgbbfbbfcdfaeffebfebdagfgeecgebdbgedabfdeefbebbeabadggebeafcedbdbdbegcdcacbbbfadgbafbbedcbccebeegcbafdceedgdebbagacdadfgbbfeadefeefacggcacbbfaddcfeefedgggbdeccgfffdafdbeebeecfbbcefbcgdeceaaeafcdgfdefededeafbbaagedcaccdcbcfdcfacbceccbbgccgafebdacfgccgbdcgbbdggdfffbeaaffeefegbdabfceeggagcebaeebcgdcdcgfgddgffgcgefaaggfcggffeabafggaagddgabcdaeacdeeebgaceafddbgdcageaddagcdgedadgdbcfdafggdcgcbdacegaggggaffcegfeedfdbafcaacadcebebbbfeggaegffgfbeedeegeeegceadedeffbffgbacadgcgbcdbeegaadbfaeececafbcfbadgbbcbdcaeadccadccdagebebecbdbdgeeafgadbagbdcadddebdeebfecgcgacgaaeefgegadgadccfbcefffggcdccabbfbafeefeaddaeaabegfeafgedefegfbfgfdabbagdcdcbcegbeabbaaaafebdfdcdcbfadfdccaccfbddcbefddcgdbdgbgaegebbdcbbgabfgbfcaeabbcbgeadaecggddgcdbeaccgacbdaffgcbacegbedfcacgbfdfgggbedcfefdecdfecbeaafdbaacedcfcbbdgcaaafeeaafebbfffacfbbfaaaggfcdcfeddgegfdcgdbegebaeegffeefffbgfcddbfggdfdggcbfaagfcdcfcggedcdfeebgcebdbaabbbfgfbbadbeefeebgbbdaafeeegacaebeabbgcffegbagfgddbgcegfegfggecaafffegedfffaddecggebdfafdcggeccbbggeffaabbdgdddbeegbbcdbgeadeddddbgdebfedgagcccffgdgbbgfdeeaedffbcfbfeggdbfcdaabfbeddeceabedaceagebbfbbccfecbcebdagfgccbdcbefggcababbcafgdfcaegdcgbdbeaafdgaedabedefcgfbegfcdffbbbdcfcebedbgebdbdfaceccddgfaadbcfgccgfcdadcaccccgffadgdgbcfaebceeacefeaggcfbecggbbfeddedgdeaeaggdfefaacffdacfacaaddcbegfggdafbgccffbaedeaebdbaadgbeffddbaggfafeddagbeddbdceaceeebbdegefgdafgcabbcccdefgdcaebgaeggcdafgdbabegdeffdaecdeacedbgcffgdfegefagadedddcadaagabedafgbggbgcgeagebcgabfcabdbcdedegdfcfcfbgdgceecffbgbbgeecgdabbdbgaeeebfggaebfdcbcgcffbgbgacagaeedcdeaadbbfaacgdgaeacgbadgagfdbgbgecdaacgabeccabdefeadebcgfcdafdbefbbcfbcgfgedabbfaabedcdfedbbgcbcdcceedceaaeagcbedcfcbbgcdgebbeddgaafafgdaabgdfgebacddecgaccgbdeefcdecfecaebgfcdcfeaaaefffbadgebgccggagadbfabdefggdcadbeebaecaggebcefbagfgfacgaebeffcdegbacafebbgaadcfdegbafaebecdffgaeefdddbbcbafabeaacadfeddgcbgeeaceggdbgecfddaffeeggcadcedecbfgcccbdfdfbegebbdbeefeffagbbagfafbbeggcdbfbaaffffabgcbfadbedfccfbgacgcfdefgafaddcfbagceegbbbdcceddccaegdgacdeagcgcbccgcecbgfdccdggdbdfbcgafafecfbdecfbffbacebcgebdafedfbbegfaafeebdebaeacddeeebfdaaabebdebceeabbcefagbafbcbedcaeeaeeeffbacdfgaeeafecgaeebcecdeaeabagdfbafcafecfebafbegfccebbafcdaccdebgbeefcccdecfbfgdbcedecgdgceebegebgafggddegafcdgbdcaabbfcgcabebagebbgadddgebfffcbdcggcccgfdfaadabbbcfadabbffdaeecebadgfaaecgddbffgecgcbafaccggfcccgbabbebgedaabdbdbbgfeecbgfadbaeggbfbebbagdedagbcfacgbfbfbgcccdeeageabbbbfdccbadcdagcbfegbddffgbfddgadebfcdfdacecbdcaffbaafefbbedgbbfbaaceabffagebcagfgagbbeeebaebfbfcacfbdbabgcegfagfcdgcccgfcecdgcabdbedecgdfdgecddgadgbegcfadeeeecbcedbgdgcbdgbbdcfgebbbdeccceaddfbbadgdbddabdbabcafceagbfaddgcgffccageaccafbagfgdegcfabdgeddfcgbaecegeebafgdfbacgdafaefdbbfefefbfcbeecdfacbaffdccgbgcdaddbgedagfebacfbccbfffbdcfcbeegdgabgbcdfaaaccecfdefaccaaacdcdgafggcdadefggdgabddffbgbdeedbaaadcegdecbaeafegadagagggbfggbgcdfadeadacdgaaddadcecadbbegfbfgadafedadaeefcegebagfceabbecegabagddafccbefcafbffcdfaefcfddgcabfddcdcgccgaebdccgedfgfecdgbcdffbfdeaafbbebbaafgeffcffbgbfeccfcdcgfebgdgdfbgbdbddbdgbdedgdgbdeefegbedgfcecbceabeaaegdceagcagecfbgfggccaaedgaafaaaaacafefcaaddbeaabfgbadcaagaagbfbafcdfbabafeefbdacddeccfebabfgfbgaabcgbaeffdacgbaggadcfdcgcgddaefggadgaadefabfefgfegcfbebeaaggddfdedgccgaggcaaccadeebfcefbcdgffgcgebeffdfggdcagefbdcdccafgcgcfgfceadccececfaaebbdegeagabdaafaeegbebaecacecadbedgdgbbfcdgfgeebgdabdcefcdadcebgabbfabagcddedfedagefaagfddfdedgdgegdacccdbbddeagbcecdedaebebeeedgacgffeggdfbggeebbgfcabfbegcgefdafffeceecffbbbccbgeagefabfeeebddcabgbfedfgbefgaebabbebgefceeaeegdgcfbagdbeggadfecaaaceccbdaggfceegbgcdfgdebbfgcaddeacegeegbgbfgdgfdegafbfeaegccdcfdeeeccadggeeebdfeafggbafbedefaacgeagedabfggeaecbadbcbeeafccbdedddfbegcgagbcaafbaefgagaggcfegdbcfcddebbfacfdadcaedbcfaabebffcaefbffgbbgbcefgfgefecfddgdgefbfgcfafagfbcdbbeacfbaffefabccbdgcecabgcfecaefefdgggdfcfegcadgaacdgcfedgfecfaafdfdbegdbdbbaebbbbfeacdefdgbeafffbcdbcbdgbbffbaccdbdbeacfeedbdcfdgcacaebfedabdcdabdfebcfdbgadcacddeecgcbgdcaafcbgabfccgeedecgdgcaecafedacgeabddfdacgdafeegaaeeaagbgcgabgcebccbdbbfcgdcbgbfbaggaecgadeccgedgefbabaccdadgdfeacdefadgggcedabcfaebgebbgcfdgcgfbaafgbbddabefcebeeagbcbecffcaagadeaccgeedgafaedfdegadfcgddbgefafccdbgcafdeedebdeadagccgefcefdfbefdcfbcgfbfbacaaaaffcacgfaafgfgbfbdedcfgdgabbcafebbfdfbccbbdedbdgebfdadbaaeggdaadcgcgdaecbadagcffdgaeeaafdecegebbfgbagcacecdgfgdbaccgdbgfbcbdgdbdadgggdcbfcgbgbeccadcbgbbfbeededbdbgfedefeccbegbfdegdcedfdffcgfbebcdacebebbdfagbfaffcecddcdaabeabaedbgeagbedbcggbcccabbbaabecgaacacbcgdaeggaddbabfcggfddffbcgdcbgabbacefccacbefegffffcgdbcadeggdgdfebcbcfbbedeaafacebcceacafcfecgefadcgdfafegfgfbfadbgddeffegafeddddagfefgcegdfdfbfadgbdgagdgafgcfefdacfdbfagcaddadacbgbecggfceacbdgaegfgfdedcdbgbgffeadggfefdefeegeegegbggaecbefcbdcfcgbefgffbgbadfeeaaedagccffeecfefaebddffeacfdggcdfcdefddgffceaacgbccbcabegecaaedcbagfcabgefbegfabcfgbbbcfcfagbbgebdfbfbgeedfedeegdaeeebfeddeggcfgbcfggcgadecdfcgecfcacfbcagabgabfgcgbbcbgcbabfffaaeacdedfbgcfbaegdcgeffgfbefgeegfcaadgddfgdfacgcafabeafbgdbgcccbgedcdfafdfgffcdbbeegbbcfcgddfccedbadfgdgdcdagdccbgcgdagadcacddceeefdggeacfbacgaeddfbdecfdabdefddaggbacbbgeedgacdddbeeedbdeegeadfbbefaagdbegbccacagefagbgcbgadbbgcbafbcfedegdgdfdbfdggadfgdbaeaeedaccgcdfdefcdgfddfabacbdbaacdfedfbcccbcegdfaebbbefgcbfdbbacaafaeeebcbbageggfagggfedbegdgacaddbcbcefbfedbefedbfgcgcbecbafdaeabagfebbdffecfecbgdcgfdbgcacgefafdfcedgceegbaccbdcgbfdcdgfceabacefabaaegbebfabcffegccffcfcdgdggefgaegegccdffebeggecbgebbcggdcagagcfddefbaeddggegedbfeaefeaddcgfbbecfdbeeggdgdfgcddfabagbeebgacedgdbecafafabcfeeafaefbdfebccggcbdagfcefgefefabdcfgedeeeaaccfgacgdagddgagbcbecagdebbbafcdaedcgfgaegefafeabdeegffccebffbacfgabdgdfacadcabdgaceadeabbfdefdaafbbfacacbfbaccedeeecfdcfabadgabfaddefbgfdbdfcgfaeffcebefaadfedbaeecffbfgcbcdgegbagdebeacaaagaegebfcecfffeedeeaccdedbaddgecfagbebcbdedfbddaeeeccaegegdbeaafabcfgaeeabcdbebgafbeabfagbdbbdecccdgbdgcggcggbbfdddebegadgadabcccaggabdeggbegdebefbgbgfdbdfgfgaegcaagcgacgeeccadfbfcbfdgegdegacabgdbgbbcefbdgeabbedegdaffbdgdcccabgagacdfdgcacecdfcedeacgaggecfcgcadedabcdgebdgffccbbeadbfcceggacbgebdfbgabbebggcecdgcbbefbegegdacabeaebebffcbgfddcgfbedddddgedcfebaefaffbefgebbgbeaececegfeeccbbgfdfcaeegeeefedefcccggfccgfbbefabbecfeggdcafggdegbdacbcadbedgageaeaeffafgedgabgaacdbddffgfadeaceffcebbbbbeeefebdgedccbdecfafaccbgcgcbgeeccbefegagfddfcadbfgddefgeaabadgefcdgdefecbddgddbaeecfeegffdddggebaaeebaeffddageecfecceeddeacfbdfegbdbeebgefedfaedgfcecfbbgfacfgdgcfdeecdegdfbegdbcggedbdcgeadebdbbcddfcggfcfgdcgegebccbgdadfgegecddbdgceffcdcafefedfdfcccgcagafgdfafccgafgfggggbcfcgfdbccedgadaabgfcffgdabfbbegfabdadfcbbddgcefdageafefdbedfbadeggfcgfebafadcgdbebgbfbadfggefecdfdfbdabfccfegabfcaefbgaaaggbgbcabgefgdgaegagfcbbeffbecggbdbbbbbdfcdgccaaagbebbgfdbbebgbcbggfcbcecaebagfdggfbffaadcggfdfabdaefdgggdbfeaccaeafcacdacgfgffcbfaccdbcbgefcfbeecdeggbdfdgdaacdagbabfcfecbaeaaccaacdcefgebgecadfcfbccgefcbfefcfedbddddgfebegacbedegefdcdfcafagcccfafaeafgdgfbfeedgcccfafcadaegegggcdfggcfabcaeefdcbfbggcdcfgdfebacdcabfbefegebfdagdgcdfcabadfcadgbdadafcebabbbabceadaadagbefbeeacdaecfgccfbdfegdbgaaeggbefbagaadebfefdcadfacbbdgagedafccaadabfedabafcedacggfdacddcaegaecfagabdegebabdaceaadbcfaddbddbcfbfbfffaggdggagbgfacfbbdebeeaegbacgcfggfccbddaggbfgceadbdcgfgcbcceggddacbegfbdabegcbefgbcefbefcgdgbgbgeeddegdfggfeagbgedcfddbaccfafedbgabdbbfadgcagdagbaedbegbfcadcabceacddacabegedfbaagfddffedgggfcfcbegggdgcdageeaeffgcdegebgcdaefecbbdfdcfagcaebbafccdddfabbgbddcgdbbefacgcaccgebcegcdefabdffebcgaabgagbedefbbebecbbedeegbfddfdbbcbeacfcacdbdcdbadddbabfageaaceaacabaceeadbadgdaeeeeccbgcccddbcddbgdceaggcbeefbbebeabaccacddfgbdecbaggfageaeffbefgcgebgegcfeefgfagcadffaccfgfeagcddgcdcdgeccaggfcdgcccecgdgfgeadbgcaaafbcgbcbbecgabbaaaafebacabgfdcefdeacfbeecdaecgfacfebcgabdadaaagacfgddcdacbabbegfgegefbdabdbbfafdgaagcaecceefeafdfadddfcgdfcccaegceggfecgdagbgafbbfgdbeagfefgbeaefadbefccecffccffeeaafbcgbafbggdaecddedddbadbbbdcgdegeedcdcggdadcacggcggfbbccfebbcdeeeecacbgcffeafdeegeecadbddccbgbbecfafcaaabdeegfcgeaceeggdcebeefcbgabgggcgdddbadgfbbgfgedddaddcegcbadcfaecedecedccfdefegaacadeggfggdgeeecdfbdgabdcebeagcedfbgagceeacdcdfdefdefcgddfbdbdedcfdfggdaeecaeaacdgedbfcbdffdafeefaccceegefcedfbbgfedecbdcdaeafeefcfbgfaeabfcebgggbbeacbfceagcggbgcccefedbbgbabedabdcbddfdbcfbeabfbbdcfdbecbgadgggabfaeagdfcefdgbeadbgcdgbbccecaabcgfcebbcedgbedbgdfadafggbbaebfffcfcgfccfaffdffdcfaddggedgddfcdfefdfeafegacbcbdcbgcabbbaefeccdeegbbgaaacbfaadaegddeaedabcgfcbdbbggbbccfgaegfcddfafeaefcggccgcffeffacbacgafafbacfggagbcebaaegefbbcgccdfdfcaefcabcbagbceeceddfcgcfaegffcddfccgfeabgbcaggdbfgabegadgagbfecdeecagbeagcegeabgfefagaegfecfbagdecacdcgaddgdcefebfgbcaecbbecdfcfegcdefbgddeeaebegbbfbecggcgdfcfcbdfeaeccaagccagebbfbdadbbaagdfgbfdaeffabgfcfgbccedfbecgagceccdfebcggcadddeddafcgccgbbffdfgadcdcdbggbbgeadaafbbbgcbffeafddfbbadeacbcgfaacgbgbdaacgcaafcaaadaddbdacaccefceaabgfcdgaeaggdcfeacbebbbfcdcfdfgceeeagfcbggccafffdgafdbbbadcfacbgffdfcdedgcfagbacggaebfaeaefbagccdcbeeegfbdgeecccbgaeebaabfefgcafgccecfecfcbdcfgcgfedcebcbcdgdfgfcfbgdebfacfeaecefgaebedbbgfedfeaaadfbfbcebcdeccgddfafceeaebdcffdgdbgffbfbbccbcccdeecgddcgbbadffegefbbddbbdfcegceadgfffbgdcabffcgegfdabcfdfdfabbbgaaffaccaeaadgbfdbcgcfbgcegdcffbgecbfccecafeacdbggbgaacabgedcfaffbffcccbeafbccdcfabdcdabecbbedgeabcbdbcbbcbdbccafdabdecbacdddfgdagfbccacgcgbadbebgfegeaaegbedcggededgfcbfbbbfbaabfcgbfgeaaccdabfaeffbeeccbcabgaaefdgdcecggdgadbbebeabdcedcbdbgebfaeedbcffadcdcfdcdgcbbcbedgfegeegfaafbeeddgabcgdeeggdabbbaddecdaedadaafefcabgcdbdbbgccfecgdegabggegagfbdgdeadabgdeegacbagddecefdcadeeaadaegfagdcgfgcefagfbafcfgbbcdccegbfcbffbfffbcgeedceccafgfecfaffbfdbbceccdegbeedgebggecffaabgabacbbbbcegaeceeacfbadfgcggbfbaafafaffffbdbaebececeeafaefbbfccdcaaffbedegegffaabfeababdebbbebaacbebaaebagbgbcdcfagdbdegcbfddcgbacdegabbfgeedbedeccgbgcgegbgaffgdgfcdccgeccdecbecgbfddcefgggeaageeeeafcfbccbcddaaegeedeeacfadcdfeeacggdabbbccbfbbgecgedeeaebgadcgbgegbaggdedgcbegfdfegfgadddabfgdagdfedbafbgbgbgcdgabeadadcgadbcfdedegbegaefgfagfeaacbafdeaacedbfagdfbdeffcfgdgfgaddafegcabbddceeacedefggbcdffdcgbbeebbeebeedgcdagfdgfcfcbgdcdddaaeggefdbdafdbbdfgggadbebcgdeffdafcgbdabefcbccgeffgcdggefgeefeeadgddeagcgacgcegfdggccacfeacgecgagbbfccfceaagdacagaabcaggdgcdegbcaaaeecceedaeddegbdcbgegafgeffagebgabcfgcbfabcgfbefbgbcgbgcbdfebgbbeaeceafaffgbdaeebaaccfgeegebggefeegegcbdefdeacebeagfdagedbedgeaceddfedcggbdbddaddgfabbeccegdgdeacccabgggafgffecfcddaafaadbgbfcgfgbgdcfcfafcgfefgcfbgdgbcbgeaedaeadfbcgffdceceggbaafaeebecfcdggacagafagfdgfgcdeegaabbfeccdafafgcfeeffddgfdeaaedacfacfbgcgaaababfcgeeaagggbebebbgccaagcgfffacfddcccdbbfbbgagegfbeaacbgddcdcdfffgfdccffdcecfbdbbcaffeceeddeaccfdgdbdggegeeccdegdedeaccdgfadcgefeabeedfefbeaeacbedbcfabbbeffgfagdfaafaccdfacdbeegedcdbfceddbfdgbbabcecbgcabdcgcdbdcfafebdabdcedbedcbbebcegecgfffafedbefadcdgdbffbaceffabffaadegcgcabdefcbeeeecgccccgfbgfeaacgdaggafdbdebedbbdffgaceefgdafdfcabbdfebcbcefdabbgagbegegaffdccaaaacafaaebdgfdbedaegafbeffcdabebedafcgagffgfgcbadgffgeacfedfeefedbacacgcdfbaafagcgggcecedaggcdfeebbacdfagegaeaaegaabgfcffgdfaegfcebacbbageafebdbfdfgggcgfbacfeacbccebadbaaffbgeabfdceacbdeffceaebebfddcdbbcccbedbcccbgbddefcadbacbcfabgccfgceaceggcedaeffgaadbcdgdaeggbbafedbgbgdfcedebfecfcgdcdbeddddgbgdaggdbecadffbafcbbegeabdbgbeebecfaacdabcbgagebddegebggbdegedgecdeecggfcgddfbfaafageeeffgfebeaacbfebccfgagdeebgdgbeaddfebcadgbeaacdddecbdbaeebfcgeffbeffegccadbfabfaadbegebagccdcgfebfeadcbgbbfddcbcdbdgefbecdbgdffbebecbgabgdbdccfagdebfddfefgfddbfdefdgfgffcggdfcbbebdbaeadbeacdcffbcacdeegccgbbeebacfcafbgcafafebegdacdgbedbebcebggbfdbabggacdbcefcbcbedabbdadgfaacddedfcccccedfbbafgeeabdfbbdbdbdfafefbgacbacagadgfbaeagddcbfebabcegbbffdeceaaggdcaacgefbdfafaadfcgafgegbaaaeggeddbedabbffcebbfedcggeecfgcgdcacegfbdbaadfdaagfgcefdcbcfdgebbegadcdgcddebgacbdeaecbcbcdbdfaafaddgadafdagdegcabbcfccbfgbedeedfebafgaefgebdacdgcgdaddfbgcdccfdbefcabgcbdcfbeddafebgfbgffbfebebbfgcfdaagddfdfecbaabefedcddgeaedfgdcaafaabceaefeadfdgcbccgebgebeabdeeebdddegdcfabbgfeeebaabdgadfeegfdadabbbaagbdfeafbbgafcdbdbcfgcaefdcdadeefeffebedbfdcccfeegebacaaadfdbbeageacbdggecgdcfegaffcdcfedgbdgaggebfdaceffagabcbbgggeagdfedfggbadaedadaegbccfbdccacdgdfdfcebgccgcaeccdfcgggdbcbfdbccdfgdfafeaadgabcfdfeffdebfffcbbfeadceabeebfeeadadbacdfbeadadgaagbcdfaegbbgcbbafagfeadddffdacffdbcgggedcdbgefbeaggacaacafeeddccebdecbcgfceeggedfdceacbagbffbcdfbbaaaggedggagfbeeagbdagadaggffcefcgcbdccegggbdegggfgbfdfdaedfecgcccafgbdedgecccgggaebebddfcdddceadbdedbbgfgbdcdcagdfccccgbeffbffaegagagfegdfgfcbbcgbcffabbfcbgefaadaggccabdbgaeeeabgbffefgeffbffcebcfabdebddbeaagfdbcagfbbgfegecbcfbedeccggecddbefcbgadeaaabaeaafbegdfdffdcadgedgcbcbdcbdccceffbeccagfaaagfecbadcaebdffaagcffeebbfadefabbcdbbabadfgadfdfcbbabdeacgacaefgfggbdgacggbefdeggggdbgffbefgggdbbeabgfefgaagbcefgbdbffegegefadbaaaefgccbdacgffdgfadbaaafecagecbdfbgafdfcddbbfcbececaabedccbdgeffdcccadgefagaegfebgaacbfagfcfagebffefebababbgafgfgdgddafeddcdbdeffcdbbacgegfdedbcbgfaeeegebcffddgbcecbbfddbcegcfdcbdaadeaaeadbfbcbaacfggecacdgbcgdggaegeebfbgeagecebedbfeeggfefbacedegeaggcfafaafeafbcgaabfdcbcfeabdadegdcbccdedfbfebccbecfgbbabadcbfeacgcbddgfdffafddadffadafbfbebdgcgdecdbfbggabbcabebfbggggeefgabagbgadadgcadbfcegafabggefggbgffeebfefddggbadeeeadfdbcdcbggafgbgecefgcfgaebdccdeddfbggecgbgefdgcegabbecadfdececgacgeabgcgdaacefcgaecdbgbfadfcdaddfebceabeacgcbcbfafgcfafccbacedbebcecedeffgfeacggagfeabaacfgggbggaeadadceegbgddcgefccfedaefaecgfceecgfcedegdecgfgdcdfefgadeafadcdegcbefeddaagaagcaffdfafgfgbfgcaagabgebdbaaffbccaebfcaedeebcefegbecfaabgaabbabfebgbacffefccfagggbefccadcdebffcacgaeggfcafdcdgedddcccdbaffbdfdbfgeeeaegbfgadbbfeabdccdbaeaecddeeegcddedfbeaeefadfgdccgacebeaggcabadcgeabcgbgdfedegbccbcdccdbgcfegfgcadebdgeebaefccddecabbefcgggbcdcdgbgedcgedbcfgegdccecddfeeffeaeaddefaggbbfgacgbfgecfadfcceeaffeeaecbdecacggaabbfbbafabfebfabgffddeafbagccabagbddaeafgffdaabcgacadfafcebdfbfefbabcadagbggccafcfgbagfbfbdgbfbfcfcfeeaebgdcbaafgcffceaggdefgbdcecgddgfccebebeeffdeagfbbbacaeaaaffafgeeeafageebdadacddccedegbdcbcefcdddccbbgcbgdaabgfafadgbbfcfbdfagfceaffdedcfcfbcffegebbagbfaebcfedgagaefefcccaebcffcbadedcbggfdfbadaceeeecaabcdfgebagefcgefcgfgccfbecgeeggfeecbebedbfcbefcbcbdaddafagedeeacgbeaeggfdcdababegfacefaedeagbbgabaedcfabggaffffaeeggdabfbdgabdfbcbcgagdgffefagcbfbaaefgfggfaeffbceceeecbbgabgcdccgbcdgbecgfaggbbegaebcfdacgadgebfbbcdgcabeedcaeacccdbbbfageefafcccfcgabeddfgaffdgbgcdebbbdadfadadddffbcgcbbbaacabgefgbbefagccgfebdcddcgadcabgfeccdcfccafaecafgcabfgefcbefaafeegfgbfbdcefeedccfaagdfgfaaggbfeggfdegdgdfagdadeeaacdgecfdbbdbaffaaadbbbgbaeefefffdadabggaaecedbagegffeeececdefdffecgdfdfbbbebegdabgcbeedcbaffadafcgdaceddeabddcfeeebdfaeeaagcafedcbfgeedcdfbcccabfeedgbfeeafafegdbedcadbcaddcccaecabgfagbfbbddbcgegafadecbadadcgdbgebffaccbcgaadcdabecacdfefgadbcgadbbgbebgaggagbageefbcgcdggafdgceabcgcbfggbfbbbgcfcdgfdeaggbdcfgfeeadagbcdfgfdcefeecdabfgfgbcefcafdaeabeegdebgfefegcgccgebddabcdeeagbafcgbbdgdacdadbdegacbcccdgdgdbgfbbgaedgagdcecfegadedafdecagbbaaaefacfabcddffaccaeabbgffabgfacgdadaedgggdgfeecdfcbgbfgdegeeggggfafdcfafdeeadggegabcbageaceagfcgbbgefcbacdeadcdcfecfgaccecaacadfffecdbdfgdefebcdeedcbcaaedafgbggceddebgaacgbceccagfdeabbafdaeeecedecdececgdefeeaedacbafgcbgfabcfbaafgcfdadfacdgaecdebadcabcfgaggcadbcfafcfadgefgaedaedededgfgbfgacacdfcabefcbeegcbebbgecdaafegfbfcbfaegbaebbgacgebeagbdbbfgbcabcdbfbdfefdcedcgabeeeffgcgggeebfcdcdgdceeffbaeagbgdbgcaddbgceeabfcgacfgcdffbabbdceddaaggdeegcafcbfcfcedecggdegdgbebabdgcfedafdgegafgfdggcdceffdacacfcfgaegfcdbecaadbgggbgdaaaagdfgefbffgcfacbeadbgggccbgbegfccdafafedbfedfeegeeaeddfggdbebgdebaggafaadedffgaebgdfededcfbdbggfcaegfabgdcaaecafgcdegagcbbdgafbfeefdebaeffebegfcegadbgccgbedffddcgebadfbbfefbgaaaabecgccaegcfaeeabbfgacefaabbdbegafabgfbcebdcegbdagdgfbgagffbadbgebbebaefaaffdbagaacaegadgfgdbdgcaccdfbabeebedecaagfgfgcgfgfabfcaffeabcffgbcbfbdbcgafdcfabbfccfagfddedcaadaaefdccfcbefcagabdffafbgffabagfedcdgggbfaagfeeefcgaaegecgfegeffddgfcefegfbffbfddfaffafcafbaggeedegcacecddaadbbeccfgcdddgffbeaefbadagbadfabgdcbfeaaaeedgegcdcdagcegfccggeccfcdggggegcfcbegfcgabefbcbedgbcbbgbbfccbafggeffddafdbbedcacegfegdafafcaacfbgaegeegcaccgfggdbcffcgabagdfddeccgdaffecbcdegcbadecebcgfafdefgbgdgaaeabeebfecagcbdfcaggbgddcbgggcabcgccdacdcgfgcadffbcebfeebdfcefgfgdacebadfadbegfdcedfgacfaaagfbaefdbaebccbggaaffefaabbffeegfaefebbccbcfdaaaebggecfbebcgcccgbedbdfgcgfgcbfdaaafgfdbgagabfefcfdgffbbecbabfdgffgdbcegaegcgdgdabfabafgfcfafdcgaebegcgedfbcggfbaccdcgbcdgbfcggdacdegaacaccgffeeebbdcdedgbedbgefdcbagdaabggadfgggdgafcfdggbgbabdfddagecacbcfecacadbdfafbccededcfbcccbgcaccgcafacgabdaegabcefefggbgfbedccdedaadceafddeeeegdecebfbfgbdfeefeffdcbgdecccccdabgbcbdfecegeacfbgdgdgfbaadafgggfgfcfaebgfddfceadbgbceedgdabfbcbbffbffccfgfaagbbbefcaefccdccadbeedaadfcfcgcbadbccgaddfbcfdddbdfagbabegagdaggdccecggegegaagbfdgdgbfgadfcdfadagfgdecbeebbgdbeegdcfgebbefgcgdcccdbgedabegggcgdccbggeggcaagcccdcdffefgbedccfdegdeefafcegdgcbfaecagcdagafcafcebeaadcgaabfbbgdcgdabdbbgcadcgdadcacacbfegbbbadfbddfebefbececefgafdbaaedfbdeagegfaggccfdfffdbgefebadeaafceabfdccddccdedcbddgccceffggcddcfddgbdgecadcbdeacgcacadbdbebbeccgcfacbgdgdbfdcdfdecceefbecefcafadegdfadgceffcedbbfeebggcdddbfgbbafeefcfgbdcbggbafgcgbdgffgfgfbfcdafdaafacgabefeadddfccfgaecbaccdeddcgedcbbafdacgfbgcddedefcggaeeafddeeeaegdgeecccdbeedfdbefdfadggecgffcebggebgfddccbafebecefcfagacdgfddccaabefgdbafeaecdbgedagaaeacdfcgfabeefbdgfbcgfffcgadefbcbbcfdgfdagfgdafdfegdcgfegbafbgbafcabgfbafeaaeeafdfdbdccddafafbeffgcfgdabebaffdacggabedagacegccfgbbaabaggbeeadfecbceeegegefafgcbacfeacaegcafbgcdabecfdceddafebdgbdbgcabafccffcegddgdgegbcecbeagedafebgdaaabadadbbfedcfaebbbcgfbbggccgbaeegdceeabggaagadcdggcbbfeagdaedggccdcebgabcefdebgacecbfccgebegfdbafbbdfaeaafegcagffegafcgggbccadbdafcgffcbfgdcgegeecfecbgadgbfgcfggebedegagffdfadeadddbaceadegdadgeagbdcccbcfdefaeecdccfagadcegebfcdfedfdgcebeaebgafafegebfbdaebgeccdgcadfdegddcadagcbccefdaffebcfecdabgdcecbagdeegccegccagfeebfbcbcgbbddcabbfgfdacadcdacaabggcdcagbacdeceaaecbfbfcadgcfbgcaegagddcbceagbefgabbeaffbefdaeddbcedacagceecbfcbgdaacdgagedfcbfffddacfadcbbcaadgggagcebaababgeebfccegbgadcaaeegafcefgcdfbgbbcddaedbggbdccdbaaffgbfbddfbcdggbgaagcafebdbcbdafggacbgbedbdfdbgfggbacccdcceegebbbdcdddfdedcbfebfffgcfbfedcfdabbbecceaabfeffcadceeebcefgaeagegdgfgbfdcaafadadceacccfceaadfbfcfdaeedaaaebccddbgfccffdbgfeefaefddeedecgbddgdbeffefcbccedbbaegbfgdeafcgeabggecgdecggfefgfbdegfcbeafcdabfagdceacbggceaggddfadfdegbddggeffdfegdaefagcaegebebdfgaddccfaagggcbdcagbggbeafgeagcfcgfdfefcbbadecffaeafdgdcgeaggaaeacbgccabcbafcgcebgeddgfcdeacdadgaffbbaggbcefbbaddbcgfafbfffbbceefaeccgbfbefbbebggggccabdecgdgfbaafcfgdedcdffgeccdegeffbebdecddagffbaefadbefefabcddfedgbcdcfadbggefgccfbeeabcgaeggdefecaefbecffgfagffecbbcfcdbggfgggbfdcgcbcfbbffbabdbfbefffacfbcceaddedfcecfbcgcgeaddefbafgcbedffdcefccafadcabceagcdagdceagbdfacggdfbeacadcgadecgeadfbcfgbdffaadcggcfdaefcccccfadbfcdgbaaebbcddfcfagfeceffggfabeccbfdgaeagdecceacageaggfabdccgbfeedccfbdcccefgdfagcbaggefgddbfdddaeecdfeaefcefdebbegbbbafabgcacdfeaggfbdbfdegfdagggeegfgcbcfcfcaccfefcdfbgbfgeebgcbgceabdfcaacgcffafecbcbbbddfabceggaagggafagafbaffbbdcbeccgbfacaffdaeffeggbdfbgcdeadadagacaadbeegfgaggafgaadagagebbbbeadcbecefcfafefddacbdfcgfgfgccfbbbaagccddfadeafbfcgdbcagdggbbbbggcafbfecffcgagdfafbgcddacffgbeababbaaddcbagffebbffagdcacafdcbbcbfdfdcgaccaacebeecbgffadfccbfaadgfdebcgaedfadcbdfedbdacggcgafbaeffadbefdbdeeeegadecfcaebebfacfeacfcedgadfbdbebdagfceacgaeegefgdcffgbfbcdbffafcdaedaadbbgceaeacedgffbeffedgbdgcbecdbcbfgbfabgcabcfcccdfaebcbggdeffddgaaccgbdgfdedbdeabcgadffefecfgdaaegcfgfbefbcbggagggdffgaegccbdeegeggdcacaffcggegeffdaecbabbcfgbfdcgdgggfdaceeagdcaccedegfdeaaeccbaedgcefaffeccccgfgdagebagccdfafbgcgdgcbcaafbaeebgeffgbdbaaeagaebedadafdfccdaaacbaceddggaadedggegbdffabfffbaegcaffcgaeadeeaffgfeafegcgcefegebacddgcdcecdacfbfbeeffcdbdfbebffgfegebgecadecbfaffdbegegadbdagfecdfbadbgfceacddaceeeeadadbebabcgedgffgbefbedfbgadcagagfaaeaadbebfcgedggcggcccaegacccegbfgcbagcdccecdecdfadccaceaebbbgbegcffegggfebgcggbdebegacadaffcaaafaefgceedgbgaadggcdebcbfefadfdedcgagbcfcdfdgacbegbbddcdccbaeafeeddgbgdcdggcddgdcfefddcacbbbfgadabfddabdecfgbdbfdgagcegcbdfaffacacfcbefdacfbfcgefdgebcfececagaecbbafgfgcfffeefccedgfceaafefffabebbabadagcgdbecegebgcgdccbeaedagdcgadfcgcadecbgbaeggfafbabdebgfacgccabdfadcfbafaaegagbccfcaffbgfecbfdfeadfbbcdedcafbbggcegeceefabdaaegfbeacdbbadfdadfaabbafgagacbgafeecebefgdfbccdbcfefaedggeddgeebafgdegebggcbefgdbeffaggecbgceeecfafadadcbaadfgfccaedagfedbfbgfbfbffgeeaeedefffcbaecbcdgegfbbcaebffaafefbcgfcbefeeagaagegcgfdacdbdecffcbbgddbecfdfabggbeafcddgaedcbfadabccffcgcffffbbebccecfcffebcacgaafbabcbbecdfdebgabbgfadfffddbefgcdcdcfbdeacfcgabggcdddeabfbeabecaafeeagcbbefcaebagfdfdcebgfebgfbgbdafcdgcbafeaegffacfafdcbeaacdebgcdgfceagfdcadeceggebgdedbddbfcbccdcaabbdggcdecgefbaeefgafddcfbeeecbabdfdaaedgcaacbfgffdbeddfegeeeedbgcbccadabacedebcbdgacbbaaadacecaadddaggceadbcegefafcdecebgaebcdabdgbaagdcddfffecbgbggaeaafcbbabeabccbaaaccafeedgaafgdaaecgabdacfeegbagcadcfadcacfgfbgaaaedfdcfefcbeadaadbddfagbcbcccdaeeadcgfdaccegfgbdacgdagefgdgcgdecbdbfeceefgaggccgcdgdeceagccbggaafdaeadbgbgadfddebcggbafcebgaccbbbgfaadaebceeeagaageaadaagfcfbaafabeebabccgaddadggffggafbfgggcdcdeafbegggebdbfefcbcgbdacfcddaddcbfdeccfacgeacdbddfgbfacfgcdagffbbgeaecbbbedaccfcbfdfgeagbgcffdfdcaeeeaaebgdgbbcccbceebggfedegggfggbbadbbbcadabfaaebfgaccfecggeeeeedcdbfbcgdecafbfedgagfbgagdfbfffaeggacabadfdfcbcceeaacccegcfdaaeaacegedfbadecbfgddcbbedddabdccecabgddbfegdbbggefbcefacegabfabfcbeadcgdbcggaegbageggaegbdabfefefffbbaaeadaffegadeddccbbcbbgaedeeffgaeedceafdgcecgfceceaeffbbaecdcaadaeaggbcgbbgfbgfaegcfbegdaefafaaadgbdefgadfdgggcgggabgadgfbgdfadafdgbeddeafbafgbgbcffgdegbfdabcagabdggecbbeccggcbceddffaedcgfebbeggdbadbefbgefcadcafdcfaadgabddadeebcacbfbbdgfacegdacbeaccfdagdffeedgggfdgcgfbdddabbefebaddbeedcfdcdafgdfbceffdcefcggdddadbfefdaefdebbfccafagafacbecededcgdebgcaedfgfdgcddfecbfbbfgfdafgddaebbcgbccfaaeegfdgadbgbgcfbfbbgdcbfagfedgdagbggfdcdeaabgbacfdeecafceafegeaecbacgccefgeacbdfgegfbbfdbgfdfbdbddabaebdabacedeffcfgfccgeacddagfcbfgeecaagbcdgbbegdfedggaebbcddfecedefecagcabebbecgdbfageggbcedbgeggcfegbdcbdegfefabbgbbfacedgbdecegaddcfffgbaffgecfbdcfacfccdfaaebfeageffebgbbbedbbcdddcbcfbcdfbdfbbaebgfecdabfacdfagaebbafbcfdcacgcbffbdddgagbbcacaebadgadaacdgdfabcbaccdfbfbedcdfacbeabeedcddebdadebbgfbdgeefefcabaaeegegdceecaabfcddddbcdegfcfccddecadbfcfgbccbaeebegefcacfadfdabfgbcbgffdeabaeegcebdgcacbeaebeeaggfbgbfdgdcdbbbgeebgafgfdeggbdfeededbbcbdeeafagffgedfefcgbgbggdbbfcegabafcfbfdcegggbebddadfdabgbgcffcffdbfefeegeefdbegfgdeacfdfgdaadcbebeefeefacebcaeebdgfdgegddecgbcfcbgaedbfgbdcegcagabggeddagbddecaabcacfcfbgbdcageeedecbaeccbccbfaeedbaabgdaadcbbgfgcefgdbbgegedffcafbgcdacbdeagabafeggfgeecabdggcgadgcbgccebfeggfagcefegaefaddabagaabecdbbfbgefcgbddbgbffbffdbdedbeacaddgfgdbbacbgebgbcggecfdcgcefdgdadbcgcbcgaeaecbggggaaecffdeeffaaccbdaabggffgfbeabfcgcefgedcabbafbagabgeegfgbaeebcbafbfedaeebbbcgcefgbgfeeagdcbgfeebgcfcdfeeefeaecacfebgcbcafeadfdeffdgbdbffgceddbcbcefgfbefgfefecggcaegdceabfgcadgcegfagggdgedfbadefbccaecagbecfedgfaddgbdfffgddfefccbdafbdgadeedggccggagbgfgcefgagbegagbbffdeffbccdgdageabagegddbabfcbegceedbccdaaaaegabefggdagabcdfdcfcccgebdebcecdcbgeafceaedfadefeagfebggfbfccgabbcbcaafacefccccfcbgdedffaaeabgadcabffbfgfaegaaggdedgfdabeffdebbbbdcddaaadfabfgbefcfgdbfdgfdgegacbedccdffggfgafcbbedadgggecbcddgfbgfdbebccbebfaadffgdcdaaffcaafbaegfabgegcfcgdcbedfgdfbfcdeefgbegbagbgfgabdfacbbddfedbccgbecgfbdfgadcegffbfgfdccggffdebfgffgcecgbgedbdgbbccadcefcbbbeacaacabggfcfecfebgeaeeeccddbcaagbbgaaefbgfbffcafgcfabgcfgebbbegabdgcdcdeaecabbbfagafacaacffcdgaeccfbgfgffdgecedgdgfabfgdgabdfebfgdbagaceaeabggeaacbabccbfebacbdfdbgaceebggafcdgdbefgccbfaceaadebfbfdadeafbbeefgdggbefbgacdeaegbgaeadafgcddbacagdgacbcgebaebbbagffbedbbecggdfaedcegfbgfegbbdgdbaacgaecggfddafbbaedfcdfbbbcfedgbfcffeadcgcggdgegccegbffebgdgcaeefbgaaebbfgafbfgcgdededdefebebcbfdbbaceaagcgabdaadfeecddaggcecbgbdaceggdbedgcebfgafcceddgfgeedeebdafeeaccdbbgcaggdadfaeaacgfcgfafgbgafddfdcbedfaggccafafcdadeadcdddaeggacdaefdeaefafcedfafgfdcfgccegdbcaegaddceafdgcggfccefbgeefdabggegeccacbfadcgfffdeddgeefcaedeacgbdfgaadfafdegcccecfcecefbbbgdgbeaecddbebbfcaeefcdfddbadceffcaadaafaffceegfgcaeecgdccafebffeaabbfdcggbedcccaegagbfbgdeebbgabfcbgfffbggbdgdaacbfdgefcecdccgcbdgffafcfcbecbffffffegadegecdfcdbeagafgdcfdbbgdcaddceccfeggbggdcfeeagfffbgafgadbgadbdddgcffcabgecaegddbcdcegcfcdgbdfgaafdccbbggeebabdbcfbcbfafffbcgebbdbgeadbfdefegdbagdgfcddccfafdecgfbeaefcgbgecdgfcddgaegfgcgbbbbbfgcggbdgcfdaaceecegeeefcebaecdcbdfegdeaddbgcgecbcbddcgcdaacdafgdececeafcecafadebeaceadbabegfeefdfebaddgeafefagcbbabgeagcbebffdbgdcceecbafaadgdggecfdaaedeabcfcgcgebdcdfgaaeadfbbecgbfagfgebgggagfddgbfbedegbbecgeebcaedgffdfeececfcfggagcfegbcddefdbdaeafcacebdfgdgdebeeacdfcbgfdfdcbbadadacecfcefccbdffbdggeeaegceafgffedfbcfeafdegbeaeeegabdfeffgcbafecfabbggffddagfggcdebdeeeegaegdfbddfaebbfdbcdabcgfggbbaebbdggcddfagddgeefebgcbccfggfbcefacgdeeafbbddccgbgddaabccfdfgeagcgegbedgadgfcaddbceeedbbaeafffabdabbefffacaebffefdbgafdffddgadefgceecfgccbaadegdccefbffafbdadaacdfdcaccaaggcccbegfbaeadcegeabbcaaagbdbcbcdaagegecdegcgeaacaddbdfdceeeegffcecebbgffgfgdfgbafffgaadfdbaadaaacbedgdbeaggebacbbabdbgaadbegadbdfgcacbgbgdbcgadbcegeebgfcafbeedeegeeeggggdcdaggbdgeaggbgegefdbbcgfgdffffgeebabbgfeceacafgdfafabebgeafefbfcfdfeabgfdbccbcaeefbacdagefefgfecdbcdcbcefabfbcgcgbfcgabgefcagfegebggegfbeegfcdcccbfdebcbbfefaedgdgcedgaecbbefggbdddfcggacefbgacbgbbdfbaabfddecfaabdfdgddbdfdebagedccdcddaafgdeadbeddedadcaegcefaafaeagcfaddeecggdgcfddbfgfgaddaagbdbcgbeffbdebbbdfgagebbgcfecgafbdbcdefdcfgeceedegaffgccadcacbefgfcbggbcgggfebgdfcbcaaffbebbefeecbagbgdffcegacfebcbegefddabbcbccfagfbbdebaefbegbeddbccafbeecdcfdcafafdeagcccbccfbgegcbfedgddfddbdccbccfffcfdaefedgaegeaabecbgbddcebdaddfgeebcbcbeececbcddaefdfgdgeggacdebfbdggfbfaecccfaffefcfbgaffbaagbfeddfdgecaebdgedagabbgaccgdfddbbfagdbedcbdcaddecbccecafafeadcegfbggaaaaffegbecgffgccaceefddcafbddagbgdbbfeebcgaagbcdddgedcabgaaebcgacabggcaaaecfgbgbgegegccebcedgddfbegdedbebgddcfabfdageccdffbcbafbgcdcaafdbaaaccgeagdabdeccdgdfbcefegbgebeeaddbcceabcegaebeaccfeaeceagbbdfadggdgabcebbcdefgddcacaaegebeeegdfcddcagbfafegfbbedbfgbfgcafcaeccabgcafdgfcbgegbagaefcdeegagedbbcedcdfbbdcbbaecdgdfeecageeaagbbcfcgcgbaaaaecfedcbcgdeadcaffgcgbgfecddgagccdbccecdaafbbdeeecbffgcgecbcabcbgccadcecdfebafbgggbaeecfgfdfffbbdgadfdfebdcfgefaedgbbefgefgeadebddgedgceeggfgffdebbacadbgafdabagddfgeggeacfbbfbedafeedeedafdcecfggfeffbgbbagfafaabffdeggaagbcabebdfbeacdccgecbccfagedfafaccgcgggbbeabgddcbebebgebddaeebgdbbfgbgfafeaggccgbcdbcgdfdfbaaddccfbfddggfdfcdfgfccfbbcadaeedfagebgcefabceeddebbbdbefcdcabeadfccadfgcaabecbdgefafdaffeeccgcddcdeccabcdefcgdeecgbdefacaeadddcagdaegedceceacbggfefeaagebbfabagbdbagbcfbfcfdagfeaaeggdgbafbggabbggcbcfabedgffagebdageggfaffbegedbfaeeeggdfddbgdccecceaaaccagbcgacgcccgcagfegdbfddgafdfeddgbcadeeedbfcbbaffcccefagfdfgaeaaddfabccgeggaaabfcafcgbaacddcaebgcdegcafbbfbdgcadcbdfdbdfebaadgbebaadegbecefebeffcecabegdbfffbecdgdaccfaacadbfaggfecfcaggcdeccfadeaaafaggecgacfabgceabfdbgadggecbffgaccedfaadgdfgdbcbdbddfgacafffffdgefdbcacaecdeebaegcedeebdebgagffdeafeaefecafafbeeabadfabbgeedebeagafaegfcfccggdebffcedgafceaabcgcdgbcbgfgacaddfgeceegcdggbecbgggggaeaddegdaacbaacedfabeafafcedeccdeegdcfefabcbbcecbccegeeefgabbdacegcbadbddegacgdfgbdgebgdeacfbfcdefcafeeggbdfbabfedecdefegcefffacgdabgedbcbeacagfcddedcgcgadbgbcddbfcbbbdbfffabaebfdefbbfegfdedbeggbebbefbfadedfbgaebdagfafdfggbadfaceebbbcgacacccgggcaggedbfccadfbabdbgdgcegbecbcacfecdbgbfbbbdeddacafgafddecfbdccgccagbceaaedeecdfdbdfgeagdbcebcdcgffaaedfdgeadegbefcbebdgccbebgdabdacfebfdfecbfbecdbeefbfaffccegefacafbbedddbcggdbaedacgddafcfcaeecccgefcefaccdfdcbgcabagfbeaadcfbdaadecfegddedfcbgfcagabdbgcfgbbcdddefabfebafffgfecfefeeecbbcfcacfagbaeeeddbdfgacadcafbgefeebbbeggbgfaefbcadedaabgagdefaaafgabadfgdaaadbefbadddfeadefbeegcccfcfgaeffaegfcabccdafdcacbddabedfegcfdggccbfddeddfbfdabadccfcefgfbffgdaebceggdbbfbcfdbbbafeefgdcaededacffdgbgdggbegggbecffgdfeeaafadcegbadedddfgecbcaaacgdddaefcdebdddadaebcbefbeaefefcabcgffceeccfeddbgbbcbddafgcadgfcgbgdfgbgeffeacgadcbedgcadaegefgfgbgfaecacaedbcdbfebdadceadcdgbffgdgegaebeebgafafefgbageddgccaccaffdaddfcgcecddecggdfbgbfcbbgebeffgebfgbcaebfdbfefdbbfbeacacgbfeedadcbebfegcafcafbfbegcgfbebdbcagdgdbfdffbeebfcfbffdfagcdabacfgbggcdfgecbgaeabdddfeebeeadfdgeebbebbcceceafgcecebggbdggeddgeedggbfbbebfafdcafdaagceegefbgebbfecdacbaaffgaffafggbeceedaecacbeaabgaeedcgbggebefbadcefbdcfaeefagbbbfdgbaagfebfafecgefdebabgcafgafcggedbfgegcbegecfggcaaeeabeddaddedccaebcegabfcegfccbebfeffcaebccfgdabgaefcbfacggfebbbefcacbagbaedcffbfccagfaeadececgcfgdabdgbgegbedgacbdcafbbeaeafabafecdddcbaabdfbcgcegebaffdbafgeeaebbecfggdegegafccggddcffdecebacdfebgdegaecfebbcegaefgebebeabdefdbeebfddbbgfecgegbfegaeccaddcbfdageeaedefdgggfcbdbeacefcdgdfbffebefaaacbdbfbcceeffbcdecdbcefgccdcedbeeffdaddeagbfbbefgccfgebbdcbaegafceecbfaddbacgeeacgfdegbfcgfgbaebdgdfgdcbddbeafcgccagbcegaadedeccggeeacfgeadegaedcegfggfccgfbffcdacbbdcfgccecacccfcffeabecdbdbebbdabcaefdgbbdccdgfceecagdaceedbceadbeaeaaaafggeffafdebbeefddcbgebdadeebgbdbcddeggebedgebgbdcagfffbbfccegcgebgbdaecdaffffabdaeagcafefaefdaaeccaabcfababbdggebcdgfgedbffcdgdgaedbdfbcaggbecegcaaadgdfegefabacbdafcgcaafefdaaefffccdcbcccbddfdbdcaeffegacefcggdfgdgfdfgfebggbebdacfgcebcacafbgaaefdddfdccfcccccaggfbfagceabaffgcgfcgaecagdfbcdcdegededbefcdeecfdffacdegfefecbcdbfcfbbecfgdcegdagfbadbadfgcgcebaebafbgdggabefaceeadgfagecgfgffdaeeefadgdcfgbaebbfgfdbcfeecbdgddeccddebeccebadgagddecbacaabebbgdbcacccgffabaccaaadeadfabeebcgbfgbbdccbbdadacabfgeggadcaebgbfdfaddfagfgabbfdcccdafggggdbfdabefcecgcfecffdaffefdfcgegdgaadgdefefbcabfaggdbeafdafaedgedfcabfdfacgaaafcdfffdgecdfcddagdbgfaadabggaabefdccafcegddadcecbgeecggfacggcaeadgaacebaedccaabbebbagafcbfefagbgacbfbgdeffaedgaebbbcaccaffafbfbbfagecabbcbedgefdccadadfebagdecdbecccccddaeagcbefacgfefgaeccfggcfffafcffffedgfbgfbbgfaggggfgafbggebcdfaagcbfdfedfeecdbeecgcfadbaabfbcdggedcaadbefdafeceaafgadbgagcebcadcbbgcbafeddbbfbabbcbdefgaeabdggeefaffagcdeaggebgedeeaceadabbabedfdafeefcfceebdebfcebeebffddcdgadedgdcefefggbbdgbbgbbeeaafabgeabcdaegaafffgcgbgbdagcadafdbfgcdbadbgbgcfegbbgfacdcfacfaefcgcdaabdbdcafabdggeeadbcaefaffbeagdbeccbffcfgdcbgdafbagfdfbdedbfggeecgeeedbefcecccggegebggbgcdcaacccefbbcgeabcegddgaaaffbacdeaadeadegfdeffgffffgggffebcdcdgcgabbabeagbbcbeebcefedeedbcfbdedeabaafggccfgcedcdcefebgeebdcedegdgdffagcdcbcebafcfddaedbccefagcdgdgacdebffcdbafafaabecgacaeafabgbcebagagfbdbfdcfeegabdedbcdbcdacgcbgdfdaccfbbfebcdcbafefdfgdbdaegeafcbgcfgccaagecaecgdfgddgdcfggdddbcgfcbdbecbbggegeeaaeeadgbefegcdacabeegacfaggcdacgdagcadgefddaaggccadgaefcbaafbbccbdgebegbbddfgdbfedegedbdaddcbcggdbabeabfbbfdcdggdceccddefdbgfacbcgdgaegbfabeccddgaggggaecfebffbdafggeffebedbfdaafbddafgfafcfcedebfgebbabaeddaabgbcdecefegdbfbeebgdagbgaadcdgegegefddegegaegccgddbcbbgdbefadgedgdffbgfdedadgaffeegbcfeggbbfbcdbagcgcdcgdecaafeefabbefbfbcafabeddadbbcadccgaffgeedaddcdbaagbdcfaeegfbbbdbegafccfcccceabffeaefeaaceadcdcebcdgbfbcbfadfdcffbabdcbgbcgfdfaecbebcfeabfeafeagbeefbgbbcfcaabbcfabcaefbcgabbdfcgdedaagbfcdabbagggaeegdfafceagbbggbfbedebdfgdeccbdedcebdcebbbegfbegbbabggdcfcgabagabfgedcbgbcadbabebfabebgafgdddaddgddcagabegfdadfacgaeaedegcbefagcaabagcdfdefaaeecdddgbfccgfaecacdeeaabfcfgccdgaababbaeccdagcdggeegcefdgbdgceaddccbcagagabgeaacdefeagceaefebbfdbgbdbfebddgbcdcabbcffgabegfdgeeceebgcffbabecffbegbfeabgdfecdfgbbagcegaagbdecbfffacccbagbgefgfacgaddabddcaaabafddeabbcfaaeeafgcgafcaggbcdacadacfcefdabggcfabbccedaedeeaacdaaeaabbcaebfcbaegfccbeedabgbgffdfbgadecdbfagcceaeaccfgdaecbbbdabefafbfbbegdeaefefffgefbeggccbeffefcfbabafbebaecedaeafgcffeacccdecfcffedadcbgfcgaaafbfgcfegcdbddfefgcdgddbfacbggeegfebefggfgefcbdaabfcgfgcdedebegdbdgcabbcgdgagecbfecegdbcadbeebcdffebdgaebfcaefdgdbbbfgcaaggcefacgcaefdfeaebefgdefgfadeddbbggbcbbcbggcebfcaggfggbbgfdfecgdccgabdffdbafdgfcaaccaefefadbbebddcagdbfbbabacccffbgafbeeecbdbaddaacbfcaefacccfdccdfcfcafgcbeafgadeeeadbaegcbedagdbccfaffbbggdffaefddbagcfgfaeffbagffegabagcbagaggeacagabagafeeddbfcaggfdbffdcdegdacbfcababcfedggbaegeaabdfebedbdbfbecabbfcaecdbcaagdddcabbeadgebfbdcagagedgdgdgddcdcdagbbcadbdecgdadgffddgggbffbgbdgabfedcdbefdadecgffbddegcbaaaeadgdcgcgadefgegdedgdbbdbbcdfbeeeaacfbecfbdeedaadbdfaccafdegbdbggedbddgagagefeacddeefgeggdbaaedadbbcfbdgafgcdbdbcffcbafegeceagdbabaeccebfebdgcdgcbddgdcbcdcefegcgbfffgcfcdddaddcbgcdegfdceccggcdgdbbegddccdcdaacadgfeabcddadaffegfaafdcbfgbggfbaabcbegcfcgccaebedfgdcfgdgfbfbcbbgcafdfgaagffdccddcdgaagggdbagbafcgbaaggcfacegdaafegbgcccdecffgfabcefbdcfbedgdbfdefeegfabadddadfbagcabeagebbfdcebccfbggacaabecaaagebffcedfbaafbegedfbcfbagdgfccefbafeeegdafdddddceefdadgefdcfgfgdegeaaccegbgeddebadcfaegdgbcbfbbdbgbbbgdgdbeffgbcdbgeecbedbcdegadgccbdebfegfgfggabdafdcaaceagbedadeceaaaggdabgdeagdeeabeabaccdaaefdebfggdagdbcegcaaafdceaebffbadbedeccfdecdcffffddggcggdagcaecfgbcbabeaeffdbcddebcagcaecfcbegdbggadgcabdbabeddcddbccgdedaccdfabbcgdaafgbdcabgfcacbbdbfeegfegfcbfdeacgfefgbbbagecddfddfbdgeaegfdafcddbffaagebfdgdddaadegagfeegfbafbffedbgcacbbaagegebafaggabedaefcggaagdefedafeddgefcdbbddaffgdccccgcecdabeadbagacggcddbgefgffbfgfaeebefdbbddcddbcacebefbbcbggggadeceaagaeccebfdbfaededcegecafecfccbecbaeecccfdcbaeabfccbebfebbeaaggegfcebfdefdcaebcecfedbegebgefbgbbaabgfcbefbfbgbcgfbcbfcagcbaeaeeaeeadebfcacbbggfaebaacfbggdeaacbeedabegagfbbbdecaaabgeeddeeegaeacefebeedgaeebagbbabeccgbfdeegdaagggddfbdddggeccabffagdbbdddcbcffcfccafdadgccggegbeeacgdfcdadfegecdceafgffbcaddegdbcdgccebaafabdabgfbeegfbgbefbcabgccdgcbcfdbbbdgcecefdgdeggcecbfcdfdebeaedggbbefceggdbdaadefbaggaabgffabgeadggbcefbecfbceaebageadgaebafebdfabadecfcdddeafdadcacgebdcfggeaagdbdgfcgefgfeecaeadceadbcccfeccaebdacdcbegaadbbgadbacaebaedfcgbedebccgebdebaacdadffebabaadbcccacfbefecgcgdbecbdaabfcacbbcaabdebeafagebccgbfcffcddefdccfbebaeefebadaeaafgbdegdffcdbcggafdaccgecgefcbacdbfdgdeegcdbabeddgdddedecbcaddefdcadgfbeffegcecbgbeggedeefefeddgbecadcgbbdfdddbdbbffgcggceccfgdbdcbgdbgeafgbdggdfggbefaggegbebdcfgcdeaafcadeegbddacaccabeabdebcfcabfbcbbbfacfeaegcadgafegfcfffcdgefdfbccdecdacdbabdcgefbaecbbbcgcbfbbcadbbbcaffcccbfgdadcedgdbbefcgegedecgfdbfgdbfccecggbgbbdfefcagcceadegggffbbbcegebcgdddabgdccfeeabgcbedgfgacdecgcffdfeacdfbgfaeaceddcddbbceegadfddfffeacdaedgfdadebdebddbfefbggeeabfgacdfcdaegagffbaagcggfdaccdcfbdgecbddgaafcbbecgggebgbgcgffdegeafeeaedggdegbgcgfgdcegecdfceffccfbbddcbbcgbcgcabceceegecfedcggffgeddggcdebeacacgdbfgdbbafeefbagaecaaedbfdaefadagbabggafbdbbedefeebaegbbaegdgfbcaefbgggbaebbbagdfcfeeeafgfbcdadggefbbebegbagacegfaadfaafeageebecedgggaceffaccbcdffdbdgggefaeddcbacagcedcbgadaeaefbbfcebbeggeegfdccaaafgbfabfeffacdbgbeddedggdcfdcfbddafdgdafcgfedgfeefccfdcgfgbeccdgfgfefdceabdefddcgafabgecccfcbdgddebbgfcbcdcadggafedcefgfgageefefgagbeefdaccgdgbedcaggaggfcdddadegefbedgaebefdbceccffacgbgddfbgfaggcdadggffcefcaacdbadfcdccdbgbcgdaeacdeedaccgdgefcdbaaeccadbbgacbfcagcadbaebbcbfbfaggbdcfeebacdbabeeegeffebcgbedffdffcbbbcacegcfbgfcedcbdggfecggcbdaafbacabfgbgfgcefgaadceeeaaeabcabbecfafcddecfabedbbcbeaacaabgcfbbdaebgfcbfcecadfdabfeaacdgfbedddbdgbdbfaddaegedeagebcgeagafgabbgggddaagcdabdeddadcaagbbbbebdgdecgeaeaccecgaccbebggdddaabcdfadadecedcbebgcebafbgfdebeecdcdadfeefbefgffeaecgfcbdaagcegaedfbddbfbagcgdbcfceceeedcfaggcabdgfacggcgaafggacgedfagdaeabdfbcbfdcgcggfbdbeacgeacadgfdafedegaggbcddgfggeceeggbdfabcdfcaggedaecbeecagdgeabedfbgdfbcbbeeefgdgecceefccfgdddeaagacdggbgdbbcgaccbfdfbadafecddbeeaebcbacddeeefdfedfcbcdcaeeaabdbbggbaafedggdb", ["a","b","c","d","e","f","g"]))

print('SolutionCountAndSay')
print(SolutionCountAndSay().countAndSay(1))
print(SolutionCountAndSay().countAndSay(5))

print('SolutionInvertBinaryTree')
t = TreeNode.treeGenerator([1,2,3,4])
t[0].left = t[1]
t[0].right = t[2]
t[2].left = t[3]
print('before: ', t[0].treePrint())
SolutionInvertBinaryTree().invertBinaryTree(t[0])
print('after : ', t[0].treePrint())

print('SolutionMajorityNumber')
print(SolutionMajorityNumber().majorityNumber([1, 1, 1, 1, 2, 2, 2]))

print('SolutionRemoveElement')
A = [0,4,4,0,0,2,4,4]
print('%d: %s' % (SolutionRemoveElement().removeElement(A, 4), str(A)))

print('SolutionHistogram')
print(SolutionHistogram().maxArea([1,3,2]))
print(SolutionHistogram().maxArea([3,4,2,1,6,1,8]))
print(SolutionHistogram().maxArea([59,15,23,55,30,47,61,74, 25]))

print('SolutionHouseRobber')
print(SolutionHouseRobber().houseRobber([1,3,2]))
print(SolutionHouseRobber().houseRobber([3,4,2,1,6,1,8]))
print(SolutionHouseRobber().houseRobber([59,15,23,55,30,47,61,74, 25]))

# print('SolutionContainerWithMostWater')
# print(SolutionContainerWithMostWater().maxArea([1,3,2]))
# print(SolutionContainerWithMostWater().maxArea([3,4,2,1,6,1,8]))
# print(SolutionContainerWithMostWater().maxArea([59,15,23,55,30,47,61,74, 25]))

print('SolutionContainerWithMostWater')
print(SolutionContainerWithMostWater().maxArea([1,2,4,3]))
print(SolutionContainerWithMostWater().maxArea([1,3,2]))
print(SolutionContainerWithMostWater().maxArea([3,4,2,1,6,1,8]))
print(SolutionContainerWithMostWater().maxArea([59,15,23,55,30,47,61,74, 25]))

print('SolutionSetMatrixZeroes')
matrix = list([[1,2], [0,3] ])
SolutionSetMatrixZeroes().setZeroes(matrix)
printMatrix(matrix)

matrix = list([[1,2,0,4,5], [15,0,1,4,5], [1,2,3,4,5], [1,2,8,4,5], [1,2,4,6,0] ])
SolutionSetMatrixZeroes().setZeroes(matrix)
printMatrix(matrix)

print('SolutionMaxProductSubarray')
print(SolutionMaxProductSubarray().maxProduct([2,-2,-4,5,-3,4,-1]))
print(SolutionMaxProductSubarray().maxProduct([2,-2,-4]))
print(SolutionMaxProductSubarray().maxProduct([0,2,-1,0]))
print(SolutionMaxProductSubarray().maxProduct([2,3,-2,4]))
print(SolutionMaxProductSubarray().maxProduct([2,3,-2,-4]))
print(SolutionMaxProductSubarray().maxProduct([2,3,0,-2,-4]))
print(SolutionMaxProductSubarray().maxProduct([-1, 99]))
# print(SolutionMaxProductSubarray().maxProduct([1,2,-1,-2,2,1,-2,1]))
print(SolutionMaxProductSubarray().maxProduct([2,-2,-5,-3,4,0]))
print(SolutionMaxProductSubarray().maxProduct([0,2,2,-1,-5,1,1,5,-6,2,1,-3,-6,-6,-3,4,0]))

print('SolutionFindMinInRotatedSortedArray')
print(SolutionFindMinInRotatedSortedArray().findMin([4, 5, 6, 7, 0, 1, 2]))
print(SolutionFindMinInRotatedSortedArray().findMin([7, 0, 1]))
print(SolutionFindMinInRotatedSortedArray().findMin([4, 5, 6, 7, 8, 9, 0]))

print('SolutionIsIdenticalTree')
a = TreeNode.treeGenerator([1,2,2,4])
a[0].left = a[1]
a[0].right = a[2]
a[1].left = a[3]
b = TreeNode.treeGenerator([1,2,2,4])
b[0].left = b[1]
b[0].right = b[2]
b[1].left = b[3]
print('before - a:', a[0].treePrint())
print('before - b:: ', b[0].treePrint())
print(SolutionIsIdenticalTree().isIdentical(a[0], b[0]))
print('after  - a:', a[0].treePrint())
print('after  - b:: ', b[0].treePrint())

a = TreeNode.treeGenerator([1,2,2,4])
a[0].left = a[1]
a[0].right = a[2]
a[1].left = a[3]
b = TreeNode.treeGenerator([1,2,2,4])
b[0].left = b[1]
b[0].right = b[2]
b[1].right = b[3]
print('before - a:', a[0].treePrint())
print('before - b:: ', b[0].treePrint())
print(SolutionIsIdenticalTree().isIdentical(a[0], b[0]))
print('after  - a:', a[0].treePrint())
print('after  - b:: ', b[0].treePrint())

print('SolutionAddBinary')
print(SolutionAddBinary().addBinary("11", "1"))
print(SolutionAddBinary().addBinary("1101", "11"))

print('SolutionAnagram')
print(SolutionAnagram().anagrams(["lint", "intl", "inlt", "code"]))
print(SolutionAnagram().anagrams(["ab", "ba", "cd", "dc", "e"]))

print('SolutionUniqueBST')
print(SolutionUniqueBST().numTrees(0))
print(SolutionUniqueBST().numTrees(1))
print(SolutionUniqueBST().numTrees(2))
print(SolutionUniqueBST().numTrees(3))
print(SolutionUniqueBST().numTrees(4))
print(SolutionUniqueBST().numTrees(5))
print(SolutionUniqueBST().numTrees(6))
print(SolutionUniqueBST().numTrees(10))
print(SolutionUniqueBST().numTrees(20))

print('SolutionEvaluateReversePolishNotation')
print(SolutionEvaluateReversePolishNotation().evalRPN(["2", "1", "+", "3", "*"]))
print(SolutionEvaluateReversePolishNotation().evalRPN(["4", "13", "5", "/", "+"]))

print('SolutionSearchTargetInRotatedSortedArray')
print(SolutionSearchTargetInRotatedSortedArray().search([4, 5, 1, 2, 3], 1))
print(SolutionSearchTargetInRotatedSortedArray().search([4, 5, 1, 2, 3], 0))
print(SolutionSearchTargetInRotatedSortedArray().search([4, 5, 6, 20, 30, 0, 1, 2, 3], 25))

print('SolutionCopyRandomListNode: test case 1')
head = RandomListNode.listGenerator([5, 2, 1, 3])
head0 = head
head1 = head0.next
head2 = head1.next
head3 = head2.next
head0.random = head2
head1.random = head0
head2.random = head2
head3.random = head2
head.listPrint()
SolutionCopyRandomListNode().copyRandomList(head).listPrint()


print('SolutionCopyRandomListNode: test case 2')
head = RandomListNode.listGenerator([5])
head0 = head
head0.random = None
head.listPrint()
SolutionCopyRandomListNode().copyRandomList(head).listPrint()

print('SolutionTrappingRainWater')
print(SolutionTrappingRainWater().trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))

# def cmp_ignore_case(s1, s2):
#     m1=s1.lower()
#     m2=s2.lower()
#     if m1<m2:
#         return -1
#     if m1>m2:
#         return 1
#     return 0
#
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], lambda x,y: cmp_ignore_case(x,y)))
# exit()

print('SolutionLargetstNumber')
print(SolutionLargetstNumber().largestNumber([91,90,9,92,90,9,89]))
print(SolutionLargetstNumber().largestNumber([5, 1, 23, 20, 4, 8]))
print(SolutionLargetstNumber().largestNumber([0,0]))
print(SolutionLargetstNumber().largestNumber([101,1]))
print(SolutionLargetstNumber().largestNumber([10, 10,1]))

print('SolutionHappyNumber')
print(SolutionHappyNumber().isHappy(19))
print(SolutionHappyNumber().isHappy(0))
print(SolutionHappyNumber().isHappy(345))

print('SolutionSingleNumberII')
print(SolutionSingleNumberII().singleNumberII([1,1,2,3,3,3,2,2,4,1]))

print('SolutionLetterCombinationOfPhoneNumber')
print(SolutionLetterCombinationOfPhoneNumber().letterCombinations('23'))
print(SolutionLetterCombinationOfPhoneNumber().letterCombinations('2279'))

print('SolutionWordSearchIn2DBoard')
print(SolutionWordSearchIn2DBoard().exist(["ABCE","SFES","ADEE"], 'ABCESEEEFS'))
print(SolutionWordSearchIn2DBoard().exist(["ABCE","SFCS","ADEE"], 'ABCCED'))
print(SolutionWordSearchIn2DBoard().exist(["ABCE","SFCS","ADEE"], 'SEE'))
print(SolutionWordSearchIn2DBoard().exist(["ABCE","SFCS","ADEE"], 'AK'))
print(SolutionWordSearchIn2DBoard().exist(["ABCE","SFCS","ADEE"], 'ABCB'))

print('SolutionDivideTwoIntegers')
print(SolutionDivideTwoIntegers().divide(-1, 1))
print(SolutionDivideTwoIntegers().divide(-1, 0))
print(SolutionDivideTwoIntegers().divide(0, 29))
print(SolutionDivideTwoIntegers().divide(9, 9))
print(SolutionDivideTwoIntegers().divide(8, 9))
print(SolutionDivideTwoIntegers().divide(18, 9))
print(SolutionDivideTwoIntegers().divide(100, 9))
print(SolutionDivideTwoIntegers().divide(100, 2))

print('SolutionIntegerToRoman')
print(SolutionIntegerToRoman().intToRoman(4))
print(SolutionIntegerToRoman().intToRoman(12))
print(SolutionIntegerToRoman().intToRoman(21))
print(SolutionIntegerToRoman().intToRoman(99))
print(SolutionIntegerToRoman().intToRoman(2199))

print('SolutionWordLadder')
print(SolutionWordLadder().ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"])))

# print(SolutionWordLadder().ladderLength("sand", "acne", set(["slit","bunk","wars","ping","viva","wynn","wows","irks","gang","pool","mock","fort","heel","send","ship","cols","alec","foal","nabs","gaze","giza","mays","dogs","karo","cums","jedi","webb","lend","mire","jose","catt","grow","toss","magi","leis","bead","kara","hoof","than","ires","baas","vein","kari","riga","oars","gags","thug","yawn","wive","view","germ","flab","july","tuck","rory","bean","feed","rhee","jeez","gobs","lath","desk","yoko","cute","zeus","thus","dims","link","dirt","mara","disc","limy","lewd","maud","duly","elsa","hart","rays","rues","camp","lack","okra","tome","math","plug","monk","orly","friz","hogs","yoda","poop","tick","plod","cloy","pees","imps","lead","pope","mall","frey","been","plea","poll","male","teak","soho","glob","bell","mary","hail","scan","yips","like","mull","kory","odor","byte","kaye","word","honk","asks","slid","hopi","toke","gore","flew","tins","mown","oise","hall","vega","sing","fool","boat","bobs","lain","soft","hard","rots","sees","apex","chan","told","woos","unit","scow","gilt","beef","jars","tyre","imus","neon","soap","dabs","rein","ovid","hose","husk","loll","asia","cope","tail","hazy","clad","lash","sags","moll","eddy","fuel","lift","flog","land","sigh","saks","sail","hook","visa","tier","maws","roeg","gila","eyes","noah","hypo","tore","eggs","rove","chap","room","wait","lurk","race","host","dada","lola","gabs","sobs","joel","keck","axed","mead","gust","laid","ends","oort","nose","peer","kept","abet","iran","mick","dead","hags","tens","gown","sick","odis","miro","bill","fawn","sumo","kilt","huge","ores","oran","flag","tost","seth","sift","poet","reds","pips","cape","togo","wale","limn","toll","ploy","inns","snag","hoes","jerk","flux","fido","zane","arab","gamy","raze","lank","hurt","rail","hind","hoot","dogy","away","pest","hoed","pose","lose","pole","alva","dino","kind","clan","dips","soup","veto","edna","damp","gush","amen","wits","pubs","fuzz","cash","pine","trod","gunk","nude","lost","rite","cory","walt","mica","cart","avow","wind","book","leon","life","bang","draw","leek","skis","dram","ripe","mine","urea","tiff","over","gale","weir","defy","norm","tull","whiz","gill","ward","crag","when","mill","firs","sans","flue","reid","ekes","jain","mutt","hems","laps","piss","pall","rowe","prey","cull","knew","size","wets","hurl","wont","suva","girt","prys","prow","warn","naps","gong","thru","livy","boar","sade","amok","vice","slat","emir","jade","karl","loyd","cerf","bess","loss","rums","lats","bode","subs","muss","maim","kits","thin","york","punt","gays","alpo","aids","drag","eras","mats","pyre","clot","step","oath","lout","wary","carp","hums","tang","pout","whip","fled","omar","such","kano","jake","stan","loop","fuss","mini","byrd","exit","fizz","lire","emil","prop","noes","awed","gift","soli","sale","gage","orin","slur","limp","saar","arks","mast","gnat","port","into","geed","pave","awls","cent","cunt","full","dint","hank","mate","coin","tars","scud","veer","coax","bops","uris","loom","shod","crib","lids","drys","fish","edit","dick","erna","else","hahs","alga","moho","wire","fora","tums","ruth","bets","duns","mold","mush","swop","ruby","bolt","nave","kite","ahem","brad","tern","nips","whew","bait","ooze","gino","yuck","drum","shoe","lobe","dusk","cult","paws","anew","dado","nook","half","lams","rich","cato","java","kemp","vain","fees","sham","auks","gish","fire","elam","salt","sour","loth","whit","yogi","shes","scam","yous","lucy","inez","geld","whig","thee","kelp","loaf","harm","tomb","ever","airs","page","laud","stun","paid","goop","cobs","judy","grab","doha","crew","item","fogs","tong","blip","vest","bran","wend","bawl","feel","jets","mixt","tell","dire","devi","milo","deng","yews","weak","mark","doug","fare","rigs","poke","hies","sian","suez","quip","kens","lass","zips","elva","brat","cosy","teri","hull","spun","russ","pupa","weed","pulp","main","grim","hone","cord","barf","olav","gaps","rote","wilt","lars","roll","balm","jana","give","eire","faun","suck","kegs","nita","weer","tush","spry","loge","nays","heir","dope","roar","peep","nags","ates","bane","seas","sign","fred","they","lien","kiev","fops","said","lawn","lind","miff","mass","trig","sins","furl","ruin","sent","cray","maya","clog","puns","silk","axis","grog","jots","dyer","mope","rand","vend","keen","chou","dose","rain","eats","sped","maui","evan","time","todd","skit","lief","sops","outs","moot","faze","biro","gook","fill","oval","skew","veil","born","slob","hyde","twin","eloy","beat","ergs","sure","kobe","eggo","hens","jive","flax","mons","dunk","yest","begs","dial","lodz","burp","pile","much","dock","rene","sago","racy","have","yalu","glow","move","peps","hods","kins","salk","hand","cons","dare","myra","sega","type","mari","pelt","hula","gulf","jugs","flay","fest","spat","toms","zeno","taps","deny","swag","afro","baud","jabs","smut","egos","lara","toes","song","fray","luis","brut","olen","mere","ruff","slum","glad","buds","silt","rued","gelt","hive","teem","ides","sink","ands","wisp","omen","lyre","yuks","curb","loam","darn","liar","pugs","pane","carl","sang","scar","zeds","claw","berg","hits","mile","lite","khan","erik","slug","loon","dena","ruse","talk","tusk","gaol","tads","beds","sock","howe","gave","snob","ahab","part","meir","jell","stir","tels","spit","hash","omit","jinx","lyra","puck","laue","beep","eros","owed","cede","brew","slue","mitt","jest","lynx","wads","gena","dank","volt","gray","pony","veld","bask","fens","argo","work","taxi","afar","boon","lube","pass","lazy","mist","blot","mach","poky","rams","sits","rend","dome","pray","duck","hers","lure","keep","gory","chat","runt","jams","lays","posy","bats","hoff","rock","keri","raul","yves","lama","ramp","vote","jody","pock","gist","sass","iago","coos","rank","lowe","vows","koch","taco","jinn","juno","rape","band","aces","goal","huck","lila","tuft","swan","blab","leda","gems","hide","tack","porn","scum","frat","plum","duds","shad","arms","pare","chin","gain","knee","foot","line","dove","vera","jays","fund","reno","skid","boys","corn","gwyn","sash","weld","ruiz","dior","jess","leaf","pars","cote","zing","scat","nice","dart","only","owls","hike","trey","whys","ding","klan","ross","barb","ants","lean","dopy","hock","tour","grip","aldo","whim","prom","rear","dins","duff","dell","loch","lava","sung","yank","thar","curl","venn","blow","pomp","heat","trap","dali","nets","seen","gash","twig","dads","emmy","rhea","navy","haws","mite","bows","alas","ives","play","soon","doll","chum","ajar","foam","call","puke","kris","wily","came","ales","reef","raid","diet","prod","prut","loot","soar","coed","celt","seam","dray","lump","jags","nods","sole","kink","peso","howl","cost","tsar","uric","sore","woes","sewn","sake","cask","caps","burl","tame","bulk","neva","from","meet","webs","spar","fuck","buoy","wept","west","dual","pica","sold","seed","gads","riff","neck","deed","rudy","drop","vale","flit","romp","peak","jape","jews","fain","dens","hugo","elba","mink","town","clam","feud","fern","dung","newt","mime","deem","inti","gigs","sosa","lope","lard","cara","smug","lego","flex","doth","paar","moon","wren","tale","kant","eels","muck","toga","zens","lops","duet","coil","gall","teal","glib","muir","ails","boer","them","rake","conn","neat","frog","trip","coma","must","mono","lira","craw","sled","wear","toby","reel","hips","nate","pump","mont","died","moss","lair","jibe","oils","pied","hobs","cads","haze","muse","cogs","figs","cues","roes","whet","boru","cozy","amos","tans","news","hake","cots","boas","tutu","wavy","pipe","typo","albs","boom","dyke","wail","woke","ware","rita","fail","slab","owes","jane","rack","hell","lags","mend","mask","hume","wane","acne","team","holy","runs","exes","dole","trim","zola","trek","puma","wacs","veep","yaps","sums","lush","tubs","most","witt","bong","rule","hear","awry","sots","nils","bash","gasp","inch","pens","fies","juts","pate","vine","zulu","this","bare","veal","josh","reek","ours","cowl","club","farm","teat","coat","dish","fore","weft","exam","vlad","floe","beak","lane","ella","warp","goth","ming","pits","rent","tito","wish","amps","says","hawk","ways","punk","nark","cagy","east","paul","bose","solo","teed","text","hews","snip","lips","emit","orgy","icon","tuna","soul","kurd","clod","calk","aunt","bake","copy","acid","duse","kiln","spec","fans","bani","irma","pads","batu","logo","pack","oder","atop","funk","gide","bede","bibs","taut","guns","dana","puff","lyme","flat","lake","june","sets","gull","hops","earn","clip","fell","kama","seal","diaz","cite","chew","cuba","bury","yard","bank","byes","apia","cree","nosh","judo","walk","tape","taro","boot","cods","lade","cong","deft","slim","jeri","rile","park","aeon","fact","slow","goff","cane","earp","tart","does","acts","hope","cant","buts","shin","dude","ergo","mode","gene","lept","chen","beta","eden","pang","saab","fang","whir","cove","perk","fads","rugs","herb","putt","nous","vane","corm","stay","bids","vela","roof","isms","sics","gone","swum","wiry","cram","rink","pert","heap","sikh","dais","cell","peel","nuke","buss","rasp","none","slut","bent","dams","serb","dork","bays","kale","cora","wake","welt","rind","trot","sloe","pity","rout","eves","fats","furs","pogo","beth","hued","edam","iamb","glee","lute","keel","airy","easy","tire","rube","bogy","sine","chop","rood","elbe","mike","garb","jill","gaul","chit","dons","bars","ride","beck","toad","make","head","suds","pike","snot","swat","peed","same","gaza","lent","gait","gael","elks","hang","nerf","rosy","shut","glop","pain","dion","deaf","hero","doer","wost","wage","wash","pats","narc","ions","dice","quay","vied","eons","case","pour","urns","reva","rags","aden","bone","rang","aura","iraq","toot","rome","hals","megs","pond","john","yeps","pawl","warm","bird","tint","jowl","gibe","come","hold","pail","wipe","bike","rips","eery","kent","hims","inks","fink","mott","ices","macy","serf","keys","tarp","cops","sods","feet","tear","benz","buys","colo","boil","sews","enos","watt","pull","brag","cork","save","mint","feat","jamb","rubs","roxy","toys","nosy","yowl","tamp","lobs","foul","doom","sown","pigs","hemp","fame","boor","cube","tops","loco","lads","eyre","alta","aged","flop","pram","lesa","sawn","plow","aral","load","lied","pled","boob","bert","rows","zits","rick","hint","dido","fist","marc","wuss","node","smog","nora","shim","glut","bale","perl","what","tort","meek","brie","bind","cake","psst","dour","jove","tree","chip","stud","thou","mobs","sows","opts","diva","perm","wise","cuds","sols","alan","mild","pure","gail","wins","offs","nile","yelp","minn","tors","tran","homy","sadr","erse","nero","scab","finn","mich","turd","then","poem","noun","oxus","brow","door","saws","eben","wart","wand","rosa","left","lina","cabs","rapt","olin","suet","kalb","mans","dawn","riel","temp","chug","peal","drew","null","hath","many","took","fond","gate","sate","leak","zany","vans","mart","hess","home","long","dirk","bile","lace","moog","axes","zone","fork","duct","rico","rife","deep","tiny","hugh","bilk","waft","swig","pans","with","kern","busy","film","lulu","king","lord","veda","tray","legs","soot","ells","wasp","hunt","earl","ouch","diem","yell","pegs","blvd","polk","soda","zorn","liza","slop","week","kill","rusk","eric","sump","haul","rims","crop","blob","face","bins","read","care","pele","ritz","beau","golf","drip","dike","stab","jibs","hove","junk","hoax","tats","fief","quad","peat","ream","hats","root","flak","grit","clap","pugh","bosh","lock","mute","crow","iced","lisa","bela","fems","oxes","vies","gybe","huff","bull","cuss","sunk","pups","fobs","turf","sect","atom","debt","sane","writ","anon","mayo","aria","seer","thor","brim","gawk","jack","jazz","menu","yolk","surf","libs","lets","bans","toil","open","aced","poor","mess","wham","fran","gina","dote","love","mood","pale","reps","ines","shot","alar","twit","site","dill","yoga","sear","vamp","abel","lieu","cuff","orbs","rose","tank","gape","guam","adar","vole","your","dean","dear","hebe","crab","hump","mole","vase","rode","dash","sera","balk","lela","inca","gaea","bush","loud","pies","aide","blew","mien","side","kerr","ring","tess","prep","rant","lugs","hobo","joke","odds","yule","aida","true","pone","lode","nona","weep","coda","elmo","skim","wink","bras","pier","bung","pets","tabs","ryan","jock","body","sofa","joey","zion","mace","kick","vile","leno","bali","fart","that","redo","ills","jogs","pent","drub","slaw","tide","lena","seep","gyps","wave","amid","fear","ties","flan","wimp","kali","shun","crap","sage","rune","logs","cain","digs","abut","obit","paps","rids","fair","hack","huns","road","caws","curt","jute","fisk","fowl","duty","holt","miss","rude","vito","baal","ural","mann","mind","belt","clem","last","musk","roam","abed","days","bore","fuze","fall","pict","dump","dies","fiat","vent","pork","eyed","docs","rive","spas","rope","ariz","tout","game","jump","blur","anti","lisp","turn","sand","food","moos","hoop","saul","arch","fury","rise","diss","hubs","burs","grid","ilks","suns","flea","soil","lung","want","nola","fins","thud","kidd","juan","heps","nape","rash","burt","bump","tots","brit","mums","bole","shah","tees","skip","limb","umps","ache","arcs","raft","halo","luce","bahs","leta","conk","duos","siva","went","peek","sulk","reap","free","dubs","lang","toto","hasp","ball","rats","nair","myst","wang","snug","nash","laos","ante","opal","tina","pore","bite","haas","myth","yugo","foci","dent","bade","pear","mods","auto","shop","etch","lyly","curs","aron","slew","tyro","sack","wade","clio","gyro","butt","icky","char","itch","halt","gals","yang","tend","pact","bees","suit","puny","hows","nina","brno","oops","lick","sons","kilo","bust","nome","mona","dull","join","hour","papa","stag","bern","wove","lull","slip","laze","roil","alto","bath","buck","alma","anus","evil","dumb","oreo","rare","near","cure","isis","hill","kyle","pace","comb","nits","flip","clop","mort","thea","wall","kiel","judd","coop","dave","very","amie","blah","flub","talc","bold","fogy","idea","prof","horn","shoo","aped","pins","helm","wees","beer","womb","clue","alba","aloe","fine","bard","limo","shaw","pint","swim","dust","indy","hale","cats","troy","wens","luke","vern","deli","both","brig","daub","sara","sued","bier","noel","olga","dupe","look","pisa","knox","murk","dame","matt","gold","jame","toge","luck","peck","tass","calf","pill","wore","wadi","thur","parr","maul","tzar","ones","lees","dark","fake","bast","zoom","here","moro","wine","bums","cows","jean","palm","fume","plop","help","tuba","leap","cans","back","avid","lice","lust","polo","dory","stew","kate","rama","coke","bled","mugs","ajax","arts","drug","pena","cody","hole","sean","deck","guts","kong","bate","pitt","como","lyle","siam","rook","baby","jigs","bret","bark","lori","reba","sups","made","buzz","gnaw","alps","clay","post","viol","dina","card","lana","doff","yups","tons","live","kids","pair","yawl","name","oven","sirs","gyms","prig","down","leos","noon","nibs","cook","safe","cobb","raja","awes","sari","nerd","fold","lots","pete","deal","bias","zeal","girl","rage","cool","gout","whey","soak","thaw","bear","wing","nagy","well","oink","sven","kurt","etna","held","wood","high","feta","twee","ford","cave","knot","tory","ibis","yaks","vets","foxy","sank","cone","pius","tall","seem","wool","flap","gird","lore","coot","mewl","sere","real","puts","sell","nuts","foil","lilt","saga","heft","dyed","goat","spew","daze","frye","adds","glen","tojo","pixy","gobi","stop","tile","hiss","shed","hahn","baku","ahas","sill","swap","also","carr","manx","lime","debs","moat","eked","bola","pods","coon","lacy","tube","minx","buff","pres","clew","gaff","flee","burn","whom","cola","fret","purl","wick","wigs","donn","guys","toni","oxen","wite","vial","spam","huts","vats","lima","core","eula","thad","peon","erie","oats","boyd","cued","olaf","tams","secs","urey","wile","penn","bred","rill","vary","sues","mail","feds","aves","code","beam","reed","neil","hark","pols","gris","gods","mesa","test","coup","heed","dora","hied","tune","doze","pews","oaks","bloc","tips","maid","goof","four","woof","silo","bray","zest","kiss","yong","file","hilt","iris","tuns","lily","ears","pant","jury","taft","data","gild","pick","kook","colt","bohr","anal","asps","babe","bach","mash","biko","bowl","huey","jilt","goes","guff","bend","nike","tami","gosh","tike","gees","urge","path","bony","jude","lynn","lois","teas","dunn","elul","bonn","moms","bugs","slay","yeah","loan","hulk","lows","damn","nell","jung","avis","mane","waco","loin","knob","tyke","anna","hire","luau","tidy","nuns","pots","quid","exec","hans","hera","hush","shag","scot","moan","wald","ursa","lorn","hunk","loft","yore","alum","mows","slog","emma","spud","rice","worn","erma","need","bags","lark","kirk","pooh","dyes","area","dime","luvs","foch","refs","cast","alit","tugs","even","role","toed","caph","nigh","sony","bide","robs","folk","daft","past","blue","flaw","sana","fits","barr","riot","dots","lamp","cock","fibs","harp","tent","hate","mali","togs","gear","tues","bass","pros","numb","emus","hare","fate","wife","mean","pink","dune","ares","dine","oily","tony","czar","spay","push","glum","till","moth","glue","dive","scad","pops","woks","andy","leah","cusp","hair","alex","vibe","bulb","boll","firm","joys","tara","cole","levy","owen","chow","rump","jail","lapp","beet","slap","kith","more","maps","bond","hick","opus","rust","wist","shat","phil","snow","lott","lora","cary","mote","rift","oust","klee","goad","pith","heep","lupe","ivan","mimi","bald","fuse","cuts","lens","leer","eyry","know","razz","tare","pals","geek","greg","teen","clef","wags","weal","each","haft","nova","waif","rate","katy","yale","dale","leas","axum","quiz","pawn","fend","capt","laws","city","chad","coal","nail","zaps","sort","loci","less","spur","note","foes","fags","gulp","snap","bogs","wrap","dane","melt","ease","felt","shea","calm","star","swam","aery","year","plan","odin","curd","mira","mops","shit","davy","apes","inky","hues","lome","bits","vila","show","best","mice","gins","next","roan","ymir","mars","oman","wild","heal","plus","erin","rave","robe","fast","hutu","aver","jodi","alms","yams","zero","revs","wean","chic","self","jeep","jobs","waxy","duel","seek","spot","raps","pimp","adan","slam","tool","morn","futz","ewes","errs","knit","rung","kans","muff","huhs","tows","lest","meal","azov","gnus","agar","sips","sway","otis","tone","tate","epic","trio","tics","fade","lear","owns","robt","weds","five","lyon","terr","arno","mama","grey","disk","sept","sire","bart","saps","whoa","turk","stow","pyle","joni","zinc","negs","task","leif","ribs","malt","nine","bunt","grin","dona","nope","hams","some","molt","smit","sacs","joan","slav","lady","base","heck","list","take","herd","will","nubs","burg","hugs","peru","coif","zoos","nick","idol","levi","grub","roth","adam","elma","tags","tote","yaws","cali","mete","lula","cubs","prim","luna","jolt","span","pita","dodo","puss","deer","term","dolt","goon","gary","yarn","aims","just","rena","tine","cyst","meld","loki","wong","were","hung","maze","arid","cars","wolf","marx","faye","eave","raga","flow","neal","lone","anne","cage","tied","tilt","soto","opel","date","buns","dorm","kane","akin","ewer","drab","thai","jeer","grad","berm","rods","saki","grus","vast","late","lint","mule","risk","labs","snit","gala","find","spin","ired","slot","oafs","lies","mews","wino","milk","bout","onus","tram","jaws","peas","cleo","seat","gums","cold","vang","dewy","hood","rush","mack","yuan","odes","boos","jami","mare","plot","swab","borg","hays","form","mesh","mani","fife","good","gram","lion","myna","moor","skin","posh","burr","rime","done","ruts","pays","stem","ting","arty","slag","iron","ayes","stub","oral","gets","chid","yens","snub","ages","wide","bail","verb","lamb","bomb","army","yoke","gels","tits","bork","mils","nary","barn","hype","odom","avon","hewn","rios","cams","tact","boss","oleo","duke","eris","gwen","elms","deon","sims","quit","nest","font","dues","yeas","zeta","bevy","gent","torn","cups","worm","baum","axon","purr","vise","grew","govs","meat","chef","rest","lame"])))


print('SolutionSpiralMatrix')
print(SolutionSpiralMatrix().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

print(SolutionSpiralMatrix().spiralOrder([]))
print(SolutionSpiralMatrix().spiralOrder([[1]]))
print(SolutionSpiralMatrix().spiralOrder([[1,2]]))
print(SolutionSpiralMatrix().spiralOrder([[1],[2]]))
print('\nEND')

print('SolutionSprialMatrixII')
print(SolutionSprialMatrixII().generateMatrix(3))
print(SolutionSprialMatrixII().generateMatrix(0))
print(SolutionSprialMatrixII().generateMatrix(1))
###########################################

