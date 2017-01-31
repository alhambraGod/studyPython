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


print('\nEND')
###########################################

