# -*- coding: utf-8 -*-
###########################################
# Add Two Numbers
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's digit is
# at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.
# Example
# Given 7->1->6 + 5->9->2. That is, 617 + 295.
# Return 2->1->9. That is 912.
# Given 3->1->5 and 5->9->2, return 8->0->8.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
from functools import reduce
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def listGenerator(l):
        if (len(l) == 0):
            return None
        prev = head = ListNode(None)
        for value in l:
            prev.next = ListNode(value)
            if (head.val == None):
                head = prev.next
            prev = prev.next
        return head

    def listPrint(head):
        print('print list nodes')
        while not (head == None):
            print('%d --> ' % head.val)
            head = head.next

    def listPrint(self):
        head = self
        print('print list nodes')
        while not (head == None):
            print('%d --> ' % head.val)
            head = head.next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def treeGenerator(l):
        ret = list()
        i = 0
        while (i < len(l)):
            ret.append(TreeNode(l[i]))
            i += 1
        # map(lambda x : ret.append(TreeNode(x)), l)
        return ret

    def treePrintNodes(self):
        ret = "%d -> " % self.val
        if (self.left != None):
            ret += self.left.treePrintNodes()
        if (self.right != None):
            ret += self.right.treePrintNodes()
        return ret

    def treePrint(self):
        print('print tree nodes: ', self.treePrintNodes())


class SolutionAddTwoNumbers:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        increment = 0
        prev = head = ListNode(None)
        while True:
            if (l1 == None and l2 == None):
                break
            v1 = v2 = 0
            if (l1 != None):
                v1 = l1.val
            if (l2 != None):
                v2 = l2.val
            value = v1 + v2 + increment
            increment = value // 10
            value = value % 10
            # construct new node
            prev.next = ListNode(value)
            if head.val == None:
                head = prev.next
            prev = prev.next
            # next loop
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        # end of loop
        if increment == 1: # add one more node
            prev.next = ListNode(increment)
        return head

# end of SolutionTwoSum

#  Two sum
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
#  Notice
# You may assume that each input would have exactly one solution
# Example
# numbers=[2, 7, 11, 15], target=9
# return [1, 2]
# solution: search from diagonal line
# x x x x x x x x
# x x x x x x x
# x x x x x x
# x x x x x
# x x x x
# x x x
# x x
# x

class SolutionTwoSum:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if (len(numbers) <= 1):
            return None
        i = 0
        j = len(numbers) - 1
        s = sorted(numbers) # s --> sorted_numbers
        while True:
            sum = s[i] + s[j]
            if (sum == target):
                # return result
                index1 = numbers.index(s[i]) + 1
                index2 = numbers.index(s[j]) + 1
                # search from after index1, there may be same number
                while True:
                    if (index2 == index1):
                        index2 = numbers.index(s[j], index2) + 1
                    else:
                        break
                if (index1 < index2):
                    return list([index1, index2])
                else:
                    return list([index2, index1])
            if (target > sum):
                # search in next triangles
                i += 1
            else:
                j -= 1
            if (i >= j):
                # end, not found
                return None
        return None

# class SolutionTwoSum:
#     def __init__(self):
#         self.tempArray = []
#         self.sorted_numbers = []
#         self.startIndex = 0
#
#     def storeTempArray(self, index):
#         print(index)
#         self.tempArray.append(
#             [self.sorted_numbers[self.startIndex] + self.sorted_numbers[index]])
#         return
#     """
#     @param numbers : An array of Integer
#     @param target : target = numbers[index1] + numbers[index2]
#     @return : [index1 + 1, index2 + 1] (index1 < index2)
#     """
#     def twoSum(self, numbers, target):
#         # write your code here
#         i = 0
#         j = 0
#         index = 0
#         self.sorted_numbers = sorted(numbers)
#         while (index < len(numbers)):
#             startIndex = index
#             r = map(self.storeTempArray, range(index, len(numbers)))
#             print(list(r))
#             index += 1
#         print(self.tempArray)
#         return
#
# end of SolutionTwoSum

# Single Number
# Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
class SolutionSingleNumber:
    def singleNumber(self, A):
        if (len(A) == 0):
            return 0
        return reduce(lambda x, y: x ^ y, A)


# Single Number II
# Given 3*n + 1 numbers, every numbers occurs triple times except one, find it.
# Example
# Given [1,1,2,3,3,3,2,2,4,1] return 4
class SolutionSingleNumberII:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        if (len(A) == 0):
            return 0
        if (len(A) == 1):
            return A[0]
        bits = list(0 for x in range(32))  # 32 bits
        i = 0
        while (i < len(A)):
            num = A[i]
            j = 0
            while (num > 0):
                bits[j] += num & 1
                num >>= 1
                j += 1
            i += 1
        # find bits of 1 after mod 3
        i = 0
        while (i < len(bits)):
            bits[i] %= 3
            i += 1
        # find result number
        result = 0
        bitValue = 1
        i = 0
        while (i < len(bits)):
            result += bits[i] * bitValue
            bitValue *= 2
            i += 1
        return result

# bool flags for characters
class CharBoolFlags:
    flags = list(-1 for x in range(256))
    @staticmethod
    def reset():
        CharBoolFlags.flags = list(-1 for x in range(256))
        return

    @staticmethod
    def get(ch):
        return CharBoolFlags.flags[ord(ch)]

    @staticmethod
    def set(ch, v):
        CharBoolFlags.flags[ord(ch)] = v
        return

# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
class SolutionLongestSubstring:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        longest = 0
        currentLen = 0
        CharBoolFlags.reset()
        currentStart = current = 0
        while current < len(s):
            ch = s[current]
            flagPos = CharBoolFlags.get(ch)
            if (flagPos == -1):
                currentLen += 1
            else: # ch already appeared
                if (currentStart <= flagPos and flagPos < current):
                    # found: repeating char
                    if (longest < currentLen):
                        longest = currentLen
                    # move start to next of repeating char
                    # currentLen is not changed
                    currentStart = flagPos + 1
                    currentLen = current - currentStart + 1
                else:
                    # not found: char appeared in previous string
                    currentLen += 1
            # must update flag-pos as current
            CharBoolFlags.set(ch, current)

            # next char
            current += 1

        # last sub-string is longest
        if (longest < currentLen):
            longest = currentLen
        return longest
# end of SolutionLongestSubstring

# Implement a stack with min() function,
# which will return the smallest number in the stack.
# It should support push, pop and min operation all in O(1) cost.
#  Notice
# min operation will never be called if there is no number in the stack.
# sulution: 1 4 2 8 5 6
#           1 --> 2 --> 5 --> 6
class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minValue = []  # store min numbers

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if (len(self.minValue) == 0):
            self.minValue.append(number)
        else:
            if (number <= self.minValue[-1]):
                # NOTE: there may be same min values
                self.minValue.append(number)

    def pop(self):
        # pop and return the top item in stack
        if (len(self.stack) == 0):
            return None
        else:
            number = self.stack.pop()
            if (number == self.minValue[-1]):
                self.minValue.pop()
            return number

    def min(self):
        # return the minimum number in stack
        if (len(self.minValue) == 0):
            return None
        return self.minValue[-1]

# Reverse Integer
# Reverse digits of an integer. Returns 0 when the reversed integer overflows
# (signed 32-bit integer).
class SolutionReverseInteger:
    min32Bit = -1 * (pow(2, 31) - 1)
    max32Bit = pow(2, 31)
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        isNeg = n < 0
        n = abs(n)
        r = 0
        while True:
            lastDigit = n % 10
            n = n // 10
            r = r * 10 + lastDigit
            if (n == 0):
                if (isNeg):
                    r *= -1
                 # check overflow
                if (SolutionReverseInteger.min32Bit > r or
                            r > SolutionReverseInteger.max32Bit):
                    r = 0
                return r
# end of class SolutionReverseInteger:

# Given a list of numbers, return all possible permutations.
#  Notice
# You can assume that there is no duplicate numbers in the list.
# Example
# For
# nums = [1, 2, 3], the
# permutations
# are:
# [
#     [1, 2, 3],
#     [1, 3, 2],
#     [2, 1, 3],
#     [2, 3, 1],
#     [3, 1, 2],
#     [3, 2, 1]
# ]
#
#
class SolutionPermutation:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        if (len(nums) == 0):
            results.append([])
            return results
        nums = sorted(nums)
        results.append(list(nums))
        if (len(nums) == 1):
            return results

        i = len(nums) - 1
        while (True):
            if (i == 0):
                break
            if (nums[i - 1] < nums[i]):
                # find in [index, len), a min number > nums[index - 1]
                j = len(nums) - 1
                while (nums[j] < nums[i - 1]):
                    j -= 1
                temp = nums[i - 1]
                nums[i - 1] = nums[j]
                nums[j] = temp
                # asc sort [index, len), currently must be desc
                # simply swap to do sorting
                start = i
                end = len(nums) - 1
                while (start < end):
                    temp = nums[start]
                    nums[start] = nums[end]
                    nums[end] = temp
                    start += 1
                    end -= 1

                results.append(list(nums))
                # print(list(nums))

                i = len(nums) - 1  # reset index
            else:
                i -= 1
        return results

# Permutation Sequence
# Given n and k, return the k-th permutation sequence.
#  Notice
# n will be between 1 and 9 inclusive.
# Example
# For n = 3, all permutations are listed as follows:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# If k = 4, the fourth permutation is "231"
class SolutionPermutationSequence:
    def getString(self, n):
        ret = ''
        i = 0
        while (i < len(n)):
            ret += ('%d' % n[i])
            i += 1
        return ret

    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        # write your code here
        nums = [i + 1 for i in range(n)]
        if (len(nums) == 0):
            return ""
        nums = sorted(nums)
        if (k == 1):
            return self.getString(nums)

        counter = 1
        i = len(nums) - 1
        while (True):
            if (i == 0):
                break
            if (nums[i - 1] < nums[i]):
                # find in [index, len), a min mumber > nums[index - 1]
                j = len(nums) - 1
                while (nums[j] < nums[i - 1]):
                    j -= 1
                temp = nums[i - 1]
                nums[i - 1] = nums[j]
                nums[j] = temp
                # asc sort [index, len), currently must be desc
                # simply swap to do sorting
                start = i
                end = len(nums) - 1
                while (start < end):
                    temp = nums[start]
                    nums[start] = nums[end]
                    nums[end] = temp
                    start += 1
                    end -= 1

                counter += 1
                if (counter == k):
                    return self.getString(nums)
                i = len(nums) - 1  # reset index
            else:
                i -= 1
        return ""

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#  Notice
# You are not suppose to use the library's sort function for this problem.
# You should do it in-place (sort numbers in the original array).
class SolutionSortColors:
    def sortColors(self, nums):
        # calculate length of each colors
        total = list(0 for x in range(4))  # store length of each color, last is length
        for num in nums:
            total[num] += 1

        index = list(range(3)) # store index for each color
        index[0] = 0
        index[1] = total[0]
        index[2] = total[0] + total[1]
        orig = list(index)
        orig.append(len(nums))

        i = 0
        while (i < len(nums)):
            num = nums[i]
            if (orig[num] <= i and i <= orig[num + 1]):
                index[num] += 1
                i += 1  # num is already sorted
                if (orig[1] <= i):
                    i = index[1]
                if (orig[2] <= i):
                    i = index[2]
            else:
                temp = nums[index[num]]
                nums[index[num]] = nums[i]
                nums[i] = temp
                index[num] += 1
            # end of while
        return nums
# end of SolutionSortColors

# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
# case: ccabbaccefg

# Manacher algorithm: O (N)
# from center to 2-sides: O(N2)
#  optimize: [dabbbbafg], after found abbbba
#     all other 'b' can be ignored
#     next char, should ensure initial N-len string is palindrome
#      next char, if max(substring len) < N, exit
class SolutionLongestPalindrome:
    def findMid(self, s, i):
        left = i - 1
        while (left >= 0):
            if (s[left] == s[i]):
                left -= 1
            else:
                break
        if (left < 0):
            left = 0
        else:
            left += 1

        right = i + 1
        while (right < len(s)):
            if (s[right] == s[i]):
                right += 1
            else:
                break
        if (right >= len(s)):
            right = len(s) - 1
        else:
            right -= 1

        return left, right

    longestLeft = longestRight = 0
    def find(self, s, i):
        if not (0 <= i and i < len(s)):
            return
        mid = self.findMid(s, i)
        left = mid[0]
        right = mid[1]
        while (0 <= left and right < len(s)):
            if (s[left] != s[right]):
                break
            left -= 1
            right += 1
        if (left < 0):
            left = 0
        else:
            left += 1
        if (right >= len(s)):
            right = len(s) - 1
        else:
            right -= 1

        if ((right - left) > (self.longestRight - self.longestLeft)):
            self.longestLeft = left
            self.longestRight = right
        pass

    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # write your code here
        i = len(s) // 2
        j = len(s) // 2 + 1
        while (i >= 0 or j < len(s)):
            self.find(s, i)
            self.find(s, j)
            i -= 1
            j += 1
        return s[self.longestLeft : (self.longestRight + 1)]

    # def longestPalindrome(self, s):
    #     # write your code here
    #     CharBoolFlags.reset()
    #     currrentStart = i = 0
    #     midStart = midLen = 0
    #     result = []
    #     while True:
    #         # next char
    #         ch = s[i]
    #         if (currrentStart == i):
    #             result.append(ch)
    #             prev = ch
    #         else:
    #             # compare with prev
    #             if (prev == ch):
    #                 if (midStart + midLen > 0):
    #                     if (i < midStart + midLen):
    #                         midLen += 1
    #                     else:
    #                         # check mirrored char
    #                         if (ch != s[midStart - (i - (midStart + midLen) + 1)]):
    #                             # mirror is wrong
    #                             el
    #                 else:
    #                     midStart = i - 1
    #                     midLen = 2
    #                 result.append(ch)
    #             else:
    #                 if (midLen == 0):
    #                     result.append(ch)
    #                 else:
    #                     # check mirrored char
    #                     if ()
    #         i += 1
    #
    #     # last sub-string is longest
    #     if (longest < currentLen):
    #         longest = currentLen
    #         longest_substring = s[currentStart: currentStart + currentLen]
    #     return longest_substring

# Given a roman numeral, convert it to an integer.
# The answer is guaranteed to be within the range from 1 to 3999.
# 罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。
# 按照下面的规则可以表示任意正整数。
# 重复数次：一个罗马数字重复几次，就表示这个数的几倍。
# 右加左减：在一个较大的罗马数字的右边记上一个较小的罗马数字，表示大数字加小数字。
# 在一个较大的数字的左边记上一个较小的罗马数字，表示大数字减小数字。
# 但是，左减不能跨越等级。比如，99不可以用IC表示，用XCIX表示
class SolutionRemanToInteger:
    def romanToInt(self, s):
        # decide sign according to priority of operator
        if (len(s) == 0):
            return 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = roman[s[-1]]
        sign = 1
        i = -2 # loop from left, start from -2
        while (-i <= len(s)):
            if (roman[s[i]] < roman[s[i + 1]]):
                sign = -1
            else:
                if (roman[s[i]] > roman[s[i + 1]]):
                    sign = 1
                ## if (roman[s[i]] = roman[s[i + 1]]):, sign not changed
            result += sign * roman[s[i]]
            i -= 1
        return result

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#  Notice
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
# note: [1,0,-1,-1,-1,-1,0,1,1,1]
class Solution3Sum:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = list()
        numbers = sorted(numbers)
        prev = numbers[0] - 1
        last = numbers[-1] + 1
        i0 = 0
        while (i0 < len(numbers)):
            if (prev == numbers[i0]):
                # avoid dup triple
                i0 += 1
                continue
            prev = numbers[i0]
            last = numbers[-1] + 1
            i1 = i0 + 1
            i2 = len(numbers) - 1
            while (i1 < i2):
                sum = numbers[i0] + numbers[i1] + numbers[i2]
                if (sum == 0):
                    # found: add to result
                    # avoid dup triple
                    if (last != numbers[i2]):
                        last = numbers[i2]
                        result.append([numbers[i0], numbers[i1], numbers[i2]])
                    i1 += 1
                    i2 -= 1
                else:
                    if (sum < 0):
                        i1 += 1
                    else:
                        i2 -= 1
            i0 += 1
        return result

# Longest Common Prefix
# Given k strings, find the longest common prefix (LCP).
class SolutionLarestCommonPrevix:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if (len(strs) == 0):
            return ''
        src = strs[0] # find shortest string
        for i in range(1, len(strs)):
            if (len(strs[i]) <len(src)):
                src = strs[i]
        if (len(src) == 0):
            return ''
        i = 0
        while (i < len(src)):
            for str in strs:
                if (src[i] != str[i]):
                    if (i == 0):
                        return ''
                    else:
                        return src[:i]
            i += 1
        return src
# end of SolutionLarestCommonPrevix

# Given n points on a 2D plane, find the maximum number of points
# that lie on the same straight line.
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class SolutionMaxPointsOnALine:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        pass


# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm
# to find the maximum profit.
class SolutionBestSellStock1:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if (len(prices) == 0):
            return 0
        lowest = prices[0]
        i = 0
        result = 0
        while (i < len(prices)):
            if (lowest > prices[i]):
                lowest = prices[i]
            currentProfit = prices[i] - lowest
            if (result < currentProfit):
                result =  currentProfit
            i+= 1
        return result

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# solution: buy and sell until price goes down
class SolutionBestSellStock2:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if (len(prices) <= 1):
            return 0
        profit = 0
        i = 0
        while (i < len(prices) - 1):
            delta = prices[i + 1] - prices[i]
            if (delta >= 0):
                profit += delta
            i += 1
        return profit

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#  Notice
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
class SolutionBestSellStock3:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if (len(prices) <= 1):
            return 0

        # create pre-profit
        preProfit = list()
        maxProfit = 0 # reset max profit
        i = 0
        lowPrice = prices[0]
        while (i < len(prices)):
            if (lowPrice > prices[i]):
                lowPrice = prices[i]
            if (maxProfit < prices[i] - lowPrice):
                maxProfit = prices[i] - lowPrice
            preProfit.append(maxProfit)
            i += 1
        # print(preProfit)

        postProfit = list()
        maxProfit = 0 # reset max profit
        i = len(prices) - 1
        highPrice = prices[i]
        while (i >= 0):
            if (highPrice < prices[i]):
                highPrice = prices[i]
            if (maxProfit < highPrice - prices[i]):
                maxProfit = highPrice - prices[i]
            postProfit.insert(0, maxProfit)
            i -= 1
        # print(postProfit)

        maxProfit = 0
        i = 0
        while (i < len(prices)):
            currentMax = preProfit[i] + postProfit[i]
            if (maxProfit < currentMax):
                maxProfit = currentMax
            i += 1

        return maxProfit

class SolutionBestSellStock3_2:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if (len(prices) <= 1):
            return 0

        # create pre-profit
        preProfit = list([0])
        i = 1
        lowPrice = prices[0]
        while (i < len(prices)):
            if (lowPrice > prices[i]):
                lowPrice = prices[i]
            preProfit.append(max(preProfit[i - 1], prices[i] - lowPrice))
            i += 1
        # print(preProfit)

        postProfit = list([0])
        i = len(prices) - 2
        highPrice = prices[len(prices) - 1]
        while (i >= 0):
            if (highPrice < prices[i]):
                highPrice = prices[i]
            postProfit.insert(0, max(postProfit[0], highPrice - prices[i]))
            i -= 1
        # print(postProfit)

        maxProfit = 0
        i = 0
        while (i < len(prices)):
            maxProfit = max(maxProfit, preProfit[i] + postProfit[i])
            i += 1

        return maxProfit

# Implement pow(x, n).
#  Notice
# You don't need to care about the precision of your answer,
# it's acceptable if the expected answer and your answer 's
# difference is smaller than 1e-3.
class SolutionPowXN:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        l = list() # store 2, 4, 8..
        if (x == 0):
            return 0
        if (n == 0):
            return 1
        if (n == 1):
            return x
        last = x * x
        lastPow = 2
        sum = 0
        ret = 1
        isNegative = n < 0
        n = abs(n)
        loop = 0
        while True:
            loop += 1
            if (sum + lastPow <= n):
                sum += lastPow
                ret *= last
                last = last * last
                lastPow = lastPow * 2
            else:
                last = x * x
                lastPow = 2
            if (sum == n):
                break
            if (sum + 1 == n):
                ret *= x
                break
        print('n: %d, loop: %d' % (n, loop))
        if (isNegative):
            return 1.0 / ret
        else:
            return ret


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class SolutionSortList:
    def merge2Lists(self, l1, l2):
        if (l1 == None and l2 == None):
            return None
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        h1 = l1
        h2 = l2
        if (l1.val < l2.val):
            ret = l1
            h1 = h1.next
        else:
            ret = l2
            h2 = h2.next
        cur = ret
        while True:
            if (h1 == None):
                cur.next = h2
                break
            if (h2 == None):
                cur.next = h1
                break
            if (h1.val < h2.val):
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        return ret

    def sortListWithLen(self, head, listLen):
        if (head == None):
            return None
        if (listLen == 1):
            head.next = None
            return head
        if (listLen == 2):
            l2 = head.next
            l2.next = None
            head.next = None
            return self.merge2Lists(head, l2)

        midLen = listLen // 2  # floor
        index = 0
        mid = head
        while (index < midLen):
            mid = mid.next
            index += 1
        # left: [head, mid)   right: [mid, None)
        left  = self.sortListWithLen(head, midLen)
        right = self.sortListWithLen(mid, listLen - midLen)
        return self.merge2Lists(left, right)

    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        listLen = 0
        cur = head
        while (cur != None):
            listLen += 1
            cur = cur.next
        return self.sortListWithLen(head, listLen)

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class SolutionMergeSortedList:
    def merge2Lists(self, l1, l2):
        if (l1 == None and l2 == None):
            return None
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        h1 = l1
        h2 = l2
        if (l1.val < l2.val):
            ret = l1
            h1 = h1.next
        else:
            ret = l2
            h2 = h2.next
        cur = ret
        while True:
            if (h1 == None):
                cur.next = h2
                break
            if (h2 == None):
                cur.next = h1
                break
            if (h1.val < h2.val):
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        return ret

    # merging sort
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    # Time Limit Exceeded
    # def mergeKLists(self, lists):
    #     # write your code here
    #     if (len(lists) == 0):
    #         return None
    #     ret = lists[0]
    #     index = 1
    #     while (index < len(lists)):
    #         l = lists[index]
    #         ret = self.merge2Lists(ret, l)
    #         index += 1
    #     return ret


    def mergeKLists(self, lists):
        # write your code here
        if (len(lists) == 0):
            return None
        if (len(lists) == 1):
            return lists[0]
        midLen = len(lists) // 2
        left = self.mergeKLists(lists[:midLen])
        right = self.mergeKLists(lists[midLen:])
        return self.merge2Lists(left, right)

# Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class SolutionClimbingStairs:
    # f(1) = 1
    # f(x) = f(x - 1) + x
    def calcX(self, x):
        if (x <= 1):
            return x
        return self.calcX(x - 1) + x

    # C(n, n2)
    def calc(self, n, n2):
        x = 1
        i = 0
        while (i < n2):
            x *= n
            n -= 1
            i += 1

        i = 0
        y = 1
        k = 1
        while (i < n2):
            y *= k
            k += 1
            i += 1
        return x // y

    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if (n <= 1):
            return n
        n2 = n // 2
        total = 0
        while (n2 >= 0):
            total += self.calc(n - n2, n2)
            n2 -= 1
        return total

# Merge Sorted Array
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#  Notice
# You may assume that A has enough space (size that is greater or equal to m + n)
# to hold additional elements from B. The number of elements
# initialized in A and B are m and n respectively.
class SolutionMergeSortedArray:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = len(A) - 1
        ia = m - 1
        ib = n - 1
        while (ia >=0 or ib >= 0):
            putA = True
            if (ia < 0):
                putA = False
            elif (ib < 0):
                putA = True
            else:
                putA = A[ia] > B[ib]
            if (putA):
                A[i] = A[ia]
                ia -= 1
            else:
                A[i] = B[ib]
                ib -= 1
            i -= 1
        return

# Maximum Subarray
# Given an array of integers, find a contiguous subarray which has the largest sum.
#  Notice
# The subarray should contain at least one number.
class SolutionMaxSubarray_1:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        start = 0
        end = 1
        i = 1
        curSum = nums[0]
        maxSum = curSum
        maxStart = start
        maxEnd = end
        while (i < len(nums)):
            if (curSum > 0 and curSum + nums[i] > 0):
                curSum += nums[i]
                end += 1
                if (maxSum < curSum):
                    maxSum = curSum
                    maxStart = start
                    maxEnd = end
            else:
                # reset
                if (maxSum < curSum):
                    maxSum = curSum
                    maxStart = start
                    maxEnd = end
                start = i
                end = i + 1
                curSum = nums[i]
            i += 1
        if (maxSum < curSum):
            maxSum = curSum
            maxStart = start
            maxEnd = end
        # return nums[maxStart:maxEnd]
        return maxSum

class SolutionMaxSubarray:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if (len(nums) == 0):
            return 0
        prevMax = maxSum = nums[0]
        i = 1
        while (i < len(nums)):
            if (prevMax + nums[i] > 0):
                prevMax = max(prevMax + nums[i], nums[i])
                maxSum = max(maxSum, prevMax)
            else:
                prevMax = 0
                maxSum = max(maxSum, nums[i])
            i += 1
        return maxSum


# Maximum Subarray II
# Given an array of integers, find two non-overlapping subarrays
# which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.
#  Notice
# The subarray should contain at least one number
# Example
# For given [1, 3, -1, 2, -1, 2], the two subarrays are
# [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.
class SolutionMaxSubarrayII:
    beforeMax = list()
    afterMax = list()

    def getBeforeMax(self, nums):
        prevMax = maxSum = nums[0]
        self.beforeMax.append(maxSum)
        i = 1
        while (i < len(nums)):
            if (prevMax + nums[i] > 0):
                prevMax = max(prevMax + nums[i], nums[i])
                maxSum = max(maxSum, prevMax)
            else:
                prevMax = 0
                maxSum = max(maxSum, nums[i])
            self.beforeMax.append(maxSum)
            i += 1
        return

    def getAfterMax(self, nums):
        prevMax = maxSum = nums[-1]
        self.afterMax.append(maxSum)
        i = 1
        while (i < len(nums)):
            temp = nums[len(nums) - i -1]
            if (prevMax + temp > 0):
                prevMax = max(prevMax + temp, temp)
                maxSum = max(maxSum, prevMax)
            else:
                prevMax = 0
                maxSum = max(maxSum, temp)
            self.afterMax.insert(0, maxSum)
            i += 1
        return
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if (len(nums) == 0):
            return 0
        self.getBeforeMax(nums)
        self.getAfterMax(nums)
        maxSum = self.beforeMax[0] + self.afterMax[1]
        i = 1
        while (i < len(nums)):
            # if (i == len(nums) - 1):
            maxSum = max(maxSum, self.beforeMax[i - 1] + self.afterMax[i])
            # else:
            #     maxSum = max(maxSum, self.beforeMax[i] + self.afterMax[i + 1],
            #                          self.beforeMax[i - 1] + self.afterMax[i])
            i += 1
        return maxSum

class SolutionMaxSubarrayII_wrong:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        if (len(nums) == 0):
            return 0
        maxSum1 = prevMax = nums[0]
        maxSum2 = None
        i = 1
        while (i < len(nums)):
            if (prevMax + nums[i] > 0):
                prevMax = max(prevMax + nums[i], nums[i])
                temp = maxSum1
                maxSum1 = max(maxSum1, prevMax)
                if (maxSum1 != temp):
                    maxSum2 = maxSum1
            else:
                prevMax = 0
                if (maxSum2 == None):
                    maxSum2 = nums[i]
            i += 1

        if (maxSum2 == None):
            return maxSum1
        return maxSum1 + maxSum2;



# Valid Parentheses
# Given a string containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Example
# The brackets must close in the correct order,
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class SolutionValidParentheses:
    def getLeftOrd(self, ch):
        if (ch == '('): return 0
        if (ch == '['): return 1
        if (ch == '{'): return 2
        return -1

    def getRightOrd(self, ch):
        if (ch == ')'): return 0
        if (ch == ']'): return 1
        if (ch == '}'): return 2
        return -1

    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        i = 0
        saveLeft = list() # a stack
        while (i < len(s)):
            leftOrd = self.getLeftOrd(s[i])
            if (leftOrd != -1):
                saveLeft.append(leftOrd) # put into the stack
            else:
                rightOrd = self.getRightOrd(s[i])
                if (len(saveLeft) == 0):
                    return False
                leftOrd = saveLeft.pop()
                if (rightOrd != leftOrd):
                    return False
            i += 1
        return len(saveLeft) == 0

# word break
# Given a string s and a dictionary of words dict,
# determine if s can be break into a space-separated sequence of
# one or more dictionary words.
class SolutionWordBreak:
    # find word from s[i] and from dict[j]
    def findWord(self, s, i, dict, j):
        if(i >= len(s)):
            return -1
        iString = i
        id = j
        while (id < len(dict)):
            word = dict[id]
            iWord = 0
            while (iString < len(s) and iWord < len(word)):
                if (s[iString] != word[iWord]):
                    break
                iWord += 1
                iString += 1
            if (iWord == len(word)):
                # print('find word: ', dict[id])
                if (len(word) == 0):
                    return -1
                return id  # found
            # next dict's word
            iString = i
            id += 1
        return -1

    def dp(self, s, i, dict, j):
        if (i >= len(s)):
            return True
        while (j < len(dict)):
            dictIndex = self.findWord(s, i, dict, j)
            if (dictIndex == -1):
                return False
            ret = self.dp(s, i + len(dict[dictIndex]), dict, 0)
            if (ret == True):
                return True
            j += 1
        return False

    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        dict = sorted(dict)
        return self.dp(s, 0, dict, 0)

# Count and Say
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#  Notice
# The sequence of integers will be represented as a string.

# Example
# Given n = 5, return "111221".
class SolutionCountAndSay:
    def genNext(self, str):
        if (len(str) <= 0):
            return ""
        i = 1
        curLen = 1
        prev = str[0]
        ret = ""
        while (i < len(str)):
            if (prev == str[i]):
                curLen += 1
            else:
                ret =  ret + ('%d%s' % (curLen, prev))
                prev = str[i]
                curLen = 1
            i += 1
        if (curLen > 0):
            ret = ret + ('%d%s' % (curLen, prev))
        return ret

    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        if (n <= 0):
            return ""
        i = 1
        ret = "1"
        while (i < n):
            ret = self.genNext(ret)
            # print(ret)
            i += 1
        return ret

# Invert a binary tree.
# Definition of TreeNode:

class SolutionInvertBinaryTree:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        if (root == None):
            return
        left = root.left
        root.left = root.right
        root.right = left
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        return

# Majority Number
# # Given an array of integers, the majority number is the number
# that occurs more than half of the size of the array. Find it.
# Notice
# You may assume that the array is non-empty and the majority number always exist in the array.
#
# Example
# Given [1, 1, 1, 1, 2, 2, 2], return 1
class SolutionMajorityNumber:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if (len(nums) == 0):
            return None
        count = 1
        cur = nums[0]
        i = 1
        while (i < len(nums)):
            if (cur == nums[i]):
                count += 1
            else:
                count -= 1
            if (count == 0):
                count = 1
                cur = nums[i]
            i += 1
        return cur

# Remove Element
# Given an array and a value, remove all occurrences of that value in place and return the new length.
# The order of elements can be changed, and the elements after the new length don't matter.
# Example
# Given an array [0,4,4,0,0,2,4,4], value=4
# return 4 and front four elements of the array is [0,0,0,2]
class SolutionRemoveElement:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        if (len(A) <= 0):
            return 0
        tail = 0
        i = 0
        while (i < len(A)):
            if (A[i] != elem):
                if (i > tail):
                    A[tail] = A[i]
                    A[i] = elem
                tail += 1
            i += 1
        return tail

#  Container With Most Water
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#  Notice
# You may not slant the container.
# Example
# Given [1,3,2], the max area of the container is 2.

class PointHeight:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height

# this is the algorithm for histogram
class SolutionHistogram:
    # return max area
    def popHeight(self, s, point, maxArea, isLast):
        i = len(s) - 1
        while (i >= 0):
            p = s[-1]
            if (p.height < point.height and (not isLast)):
                return maxArea
            s.pop()  # remove last point
            area = (point.pos - p.pos) * min(p.height, point.height)
            maxArea = max(maxArea, area)
            # print('maxarea: ', maxArea)
            i -= 1
        return maxArea

    # @param heights: a list of integers
    # @return: an integer
    # return: max area of the container
    def maxArea(self, heights):
        # write your code here
        if (len(heights) <= 1):
            return 0
        maxArea = 0
        s = list([PointHeight(0, heights[0])])  # a stack
        i = 1
        while (i < len(heights) - 1):
            h = heights[i]
            if (h < s[-1].height):
                maxArea = self.popHeight(s, PointHeight(i, h), maxArea, False)
            s.append(PointHeight(i, h))
            i += 1
        maxArea = self.popHeight(s, PointHeight(len(heights) - 1, heights[-1]), maxArea, True)
        return maxArea


#  Container With Most Water
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#  Notice
# You may not slant the container.
# Example
# Given [1,3,2], the max area of the container is 2.
# solution: start from 2 edrges, move 1 shorter height evey time
class SolutionContainerWithMostWater:
    def maxArea(self, heights):
        if (len(heights) <= 1):
            return 0
        l = 0
        r = len(heights) - 1
        maxArea = min(heights[l] , heights[r]) * (r - l)
        while (l < r):
            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))
            # print(maxArea)
        return maxArea

# House Robber
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount
# of money of each house, determine the maximum amount of money
# you can rob tonight without alerting the police.
class SolutionHouseRobber:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if (len(A) == 0):
            return 0
        if (len(A) == 1):
            return A[-1]
        if (len(A) == 2):
            return max(A[0], A[1])

        maxValue = 0
        value = list([A[0], max(A[0], A[1])])
        i = 2
        while (i < len(A)):
            current = max(value[0] + A[i], value[1])
            maxValue = max(maxValue, current)
            value[0] = value[1]
            value[1] = maxValue
            i += 1
        return maxValue

def printMatrix(matrix):
    r = 0
    while (r < len(matrix)):
        line = ""
        c = 0
        while (c < len(matrix[r])):
            line += '%d, ' % matrix[r][c]
            c += 1
        print(line)
        r += 1
    return

# Set Matrix Zeroes
# Given a m x n matrix, if an element is 0,
# set its entire row and column to 0. Do it in place.
class SolutionSetMatrixZeroes:
    def setRowZero(self, matrix, r, endColumn):
        c = 0  # column
        while (c <= endColumn):
            matrix[r][c] = 0
            c += 1

    def setColumnZero(self, matrix, c):
        r = 0  # row
        while (r < len(matrix)):
            matrix[r][c] = 0
            r += 1

    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        # store column info in the first row that has 0
        r = 0  # row
        zeroRow = -1
        # set rows as zero
        while (r < len(matrix)):
            c = 0  # column
            shouldSet = False
            while (c < len(matrix[r])):
                if (matrix[r][c] == 0):
                    if (not shouldSet):
                        shouldSet = True
                        self.setRowZero(matrix, r, c)
                    if (zeroRow == -1):
                        zeroRow = r
                    matrix[zeroRow][c] = 1 # indicate column should set zero
                elif (shouldSet):
                    matrix[r][c] = 0
                c += 1
            r += 1
        if (zeroRow == -1):
            return  # no zero found
        # set column as zero
        c = 0
        while (c < len(matrix[zeroRow])):
            if (matrix[zeroRow][c] == 1):
                self.setColumnZero(matrix, c)
            c += 1
        return


class SolutionMaxProductSubarray:
    def maxProduct(self, nums):
        if (len(nums) == 0):
            return 0
        maxRet = prevMax = prevMin = nums[0]
        i = 1
        while (i < len(nums)):
            maxRet = max(maxRet, nums[i], prevMax * nums[i], prevMin * nums[i])
            temp = prevMax
            prevMax = max(nums[i], prevMax * nums[i], prevMin * nums[i])
            prevMin = min(nums[i], temp * nums[i], prevMin * nums[i])
            i += 1
        return maxRet


# Maximum Product Subarray
# Find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# solution: when meet 0, finsih current product
#           when met neg, check even neg: true then continue current;
class SolutionMaxProductSubarray_Wrong:
    def getMax(self, ret, cur, cur2):
        if (cur == None):
            return ret
        if (cur2 == None):
            ret = max(ret, cur)
        else:
            ret = max(ret, cur, cur2)
        return ret

    # @param nums: an integer[]
    # @return: an integer
    # def maxProduct1(self, nums):
    #     # write your code here
    #     ret = nums[0]
    #     cur = None
    #     cur2 = None
    #     i = 0
    #     while (i < len(nums)):
    #         if (nums[i] == 0):
    #             ret = self.getMax(ret, cur, cur2)
    #             cur = None
    #             cur2 = None
    #         else:
    #             if (cur == None):
    #                 cur = nums[i]
    #             else:
    #                 # [pos, pos*, neg], [neg, neg], [neg, pos]
    #                 useCur2 = not (cur > 0 and nums[i] > 0)
    #                 if (useCur2 and cur2 == None):
    #                     if (cur < 0):
    #                         cur2 = nums[i]
    #                         if (nums[i] > 0):
    #                             ret = self.getMax(ret, cur, cur2)
    #                             cur *= nums[i]
    #                         else:
    #                             cur *= nums[i]
    #                             ret = self.getMax(ret, cur, cur2)
    #                     else:
    #                         ret = self.getMax(ret, cur, cur2)
    #                         cur *= nums[i]
    #                         if (i + 1 < len(nums) and nums[i + 1] > 0):
    #                             cur2 = nums[i]
    #                 else:
    #                     cur *= nums[i]
    #                     if (cur2 != None):
    #                         cur2 *= nums[i]
    #                     if (nums[i] < 0):
    #                         ret = self.getMax(ret, cur, cur2)
    #         i += 1
    #     return self.getMax(ret, cur, cur2)

    def maxProduct(self, nums):
        # write your code here
        ret = nums[0]
        cur = None
        cur2 = None
        i = 0
        while (i < len(nums)):
            if (nums[i] == 0):
                ret = self.getMax(ret, cur, cur2)
                cur = None
                cur2 = None
            else:
                if (cur == None):
                    cur = nums[i]
                else:
                    if (cur2 == None):
                        useCur2 = not (cur > 0 and nums[i] > 0)
                        if (useCur2):
                            cur2 = nums[i]
                            ret = self.getMax(ret, cur, cur2)
                    else:
                        if (nums[i] < 0):
                            ret = self.getMax(ret, cur, cur2)
                        cur2 *= nums[i]
                    cur *= nums[i]
                    ret = self.getMax(ret, cur, cur2)
            i += 1
        return self.getMax(ret, cur, cur2)

# Find Minimum in Rotated Sorted Array
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
#  Notice
# You may assume no duplicate exists in the array.
class SolutionFindMinInRotatedSortedArray:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if (len(nums) == 1):
            return nums[0]
        if (nums[0] < nums[-1]):
            return nums[0]  # no rotation
        start = 0
        end = len(nums) - 1
        while True:
            if (end - start <= 1):
                return min(nums[start], nums[end])
            i = start + (end - start) // 2
            if (nums[i] > nums[0]):
                start = i
            else:
                end = i

#  Identical Binary Tree
# Check if two binary trees are identical. Identical
# means the two binary trees have the same structure
# and every identical position has the same value.
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class SolutionIsIdenticalTree:
    def dfs(self, a, b):
        if (a == None):
            return b == None
        if (b == None):
            return False
        return (a.val == b.val and self.dfs(a.left, b.left) and self.dfs(a.right, b.right))

    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # Write your code here
        return self.dfs(a, b)

# Add Binary
# Given two binary strings, return their sum (also a binary string).
class SolutionAddBinary:
    doAddTable = {0:('0', 0), 1:('1', 0), 2:('0', 1), 3:('1', 1)}
    def doAdd(self, t1, t2, add):
        oneNum = 0
        if (t1 == '1'):
            oneNum += 1
        if (t2 == '1'):
            oneNum += 1
        if (add == 1):
            oneNum += 1
        return self.doAddTable[oneNum]

    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        shortString = a
        longString = b
        if (len(a) > len(b)):
            shortString = b
            longString = a
        ret = ''
        add = 0
        i = 0
        lenLong = len(longString)
        lenShort = len(shortString)
        while (i < lenLong):
            t1 = longString[lenLong - i - 1]
            if (i < len(shortString)):
                t2 = shortString[lenShort - i - 1]
            else:
                t2 = '0'
            addResult = self.doAdd(t1, t2, add)
            ret = addResult[0] + ret
            add = addResult[1]
            i += 1
        if (add == 1):
            ret = '1' + ret
        return ret

# Anagrams
# Given an array of strings, return all groups of strings that are anagrams.
#  Notice
# All inputs will be in lower-case
# Example
# Given["lint", "intl", "inlt", "code"],
# return ["lint", "inlt", "intl"].
# Given["ab", "ba", "cd", "dc", "e"],
# return ["ab", "ba", "cd", "dc"].
##################### NOT DONE #######################
class SolutionAnagram:
    def calcFlag(self, word):
        flag = 0
        j = 0
        while (j < len(word)):
            flag += ord(word[j])
            j += 1
        return flag

    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        retIndex = list(False for x in range(len(strs)))
        i = 0
        while (i < len(strs)):
            if (retIndex[i]):  # found
                i += 1
                continue

            lenCurWord = len(strs[i])
            curFlag = self.calcFlag(strs[i])

            k = i + 1
            while (k < len(strs)):
                if (len(strs[k]) == lenCurWord):
                    retIndex[k] = (curFlag == self.calcFlag(strs[k]))
                    retIndex[i] = True
                k += 1
            i += 1
        # copy result strings
        ret = list()
        i = 0
        while (i < len(strs)):
            if (retIndex[i]):
                ret.append(strs[i])
            i += 1
        return  ret

# Unique Binary Search Trees
# Given n, how many structurally unique BSTs
# (binary search trees) that store values 1...n?
# Example
# Given n = 3, there are a total of 5 unique BST's.
# 1           3    3       2      1
#  \         /    /       / \      \
#   3      2     1       1   3      2
#  /      /       \                  \
# 2     1          2                  3

# sub-tree with N right nodes, changed to sub-trees with right nodes: 1 1-right, 1 2-rights, 1 3-rights, .... 1 N+1-rights
#          1 2 3 4 5
# n = 1    1
# n = 2    1 1
# n = 3    1 1
#          1 1 1
#   total: 2 2 1
# n = 4    5 5 3 1
# n = 4    14  14  9  4  1


class SolutionUniqueBST:
    def calcN(self, result, n):
        result.append(1)
        i = n - 2
        while (i >= 1):
            result[i] = result[i + 1] + result[i - 1]
            i -= 1
        result[0] = result[1]

    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        result = list([1])
        i = 2
        while (i <= n):
            self.calcN(result, i)
            i += 1

        # print(result)
        sum = 0
        i = 0
        while (i < len(result)):
            sum += result[i]
            i += 1
        return sum

# Evaluate Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Example
# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# solution: use a stack
class SolutionEvaluateReversePolishNotation:
    __OPERATORS = set(['+', '-', '*', '/'])
    def isOperator(self, ch):
        return ch in self.__OPERATORS

    def calc(self, operator, op2, op1):
        op2 = int(op2)
        op1 = int(op1)
        if (operator == '+'):
            return op1 + op2
        if (operator == '-'):
            return op1 - op2
        if (operator == '*'):
            return op1 * op2
        if (operator == '/'):
            # NOTE: can not use op1 // op2
            # if ((op1 * op2 < 0 ) and (abs(op1) < abs(op2))):
            #     return 0
            # see http://www.tuicool.com/articles/ry6fme
            if (op1 * op2 < 0):
                return -((-op1) / op2)
            return op1 // op2

    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        stack = []
        i = 0
        while (i < len(tokens)):
            element = tokens[i]
            if (self.isOperator(element)):
                element = self.calc(tokens[i], stack.pop(-1), stack.pop(-1))
                # print(element)
            stack.append(element)
            i += 1
        return int(stack.pop(-1))

# Search in Rotated Sorted Array
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Example
# For [4, 5, 1, 2, 3] and target=1, return 2.
# For [4, 5, 1, 2, 3] and target=0, return -1.
class SolutionSearchTargetInRotatedSortedArray:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        sl = 0
        sr = (len(A) - 1) // 2
        nsl = sr + 1
        nsr = len(A) - 1
        while (sl <= sr):
            # [start, mid], [mid + 1, end]
            if (A[sl] > A[sr]):
                tempsl = sl
                tempsr = sr
                sl = nsl
                sr = nsr
                nsl = tempsl
                nsr = tempsr
            if (A[sl] <= target and target <= A[sr]):
                if (A[sl] == target):
                    return sl
                if (A[sr] == target):
                    return sr
                start = sl + 1
                end = sr - 1
            else:
                start = nsl
                end = nsr
            sl = start
            sr = start + (end - start) // 2
            nsl = sr + 1
            nsr = end
        return -1

# Copy List with Random Pointer
# A linked list is given such that each node contains an additional
# random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def listGenerator(l):
        prev = head = None
        for value in l:
            newNode = RandomListNode(value)
            if (prev == None):
                head = prev = newNode
            else:
                prev.next = newNode
            prev = newNode
        return head

    def listPrint(self):
        head = self
        print('print random list nodes')
        while not (head == None):
            randomStr = 'None'
            if (head.random != None):
                randomStr = head.random.label
            print('%d (%s)--> ' % (head.label, randomStr))
            head = head.next


# solution:
# 1) copy all list, each new node after old node
# 2) navigate: set .random info
# 3) remove old nodes, leave new nodes
class SolutionCopyRandomListNode:
    # def findInCopied(self, copied, node):
    #     i = 0
    #     while (i < len(copied)):
    #         if (copied[i] == node):
    #             return True
    #         i += 1
    #     return False
    #
    #     p = copied
    #     while (p != None):
    #         if (p == copied):
    #             return True
    #         p = p.next
    #     return False

    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if (head == None):
            return None
        # 1) copy all list, each new node after old node
        p = head
        while (p != None):
            newNode = RandomListNode(p.label)
            newNode.next = p.next
            p.next = newNode
            p = newNode.next
        # print('step 1')
        # head.listPrint()

        # 2) navigate: set .random info
        p = head
        while (p != None):
            newNode = p.next
            if (p.random == None):
                newNode.random = None
            else:
                newNode.random = p.random.next
            p = newNode.next  # next old node
        # print('step 2')
        # head.listPrint()

        # 3) remove old nodes, leave new nodes
        newHead = head.next
        newNode = newHead
        p = head
        while (p != None):
            p.next = newNode.next
            p = p.next
            if (p != None):
                newNode.next = p.next
                newNode = newNode.next
        # print('step 3:')
        # newHead.listPrint()
        return newHead

# Trapping Rain Water
# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water
# it is able to trap after raining.
# Example
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# Solution:for Hi, find maxBefore and maxAfter, water is max(0, min(maxBefore, maxAfter) - Hi)
class SolutionTrappingRainWater:
    def findMaxBefore(self, heights):
        i = 1
        prevMax = heights[0]
        maxBefore = list([prevMax])
        while (i < len(heights)):
            prevMax = max(prevMax, heights[i])
            maxBefore.append(prevMax)
            i += 1
        return maxBefore

    def findMaxAfter(self, heights):
        i = len(heights) - 2
        prevMax = heights[-1]
        maxAfter = list([prevMax])
        while (i >= 0):
            prevMax = max(prevMax, heights[i])
            maxAfter.insert(0, prevMax)
            i -= 1
        return maxAfter

    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if (len(heights) <= 2):
            return 0
        sum = 0
        maxBefore = self.findMaxBefore(heights)
        maxAfter = self.findMaxAfter(heights)
        i = 1
        while (i < len(heights) - 1):
            sum += max(0, min(maxBefore[i - 1], maxAfter[i + 1]) - heights[i])
            i += 1
        return  sum
#
# Largest Number
# Given a list of non negative integers, arrange them such that they form the largest number.
#  Notice
# The result may be very large, so you need to return a string instead of an integer.
# Example
# Given [1, 20, 23, 4, 8], the largest formed number is 8423201.
# solution: sort in dest dict order



class SolutionLargetstNumber:
    #@param num: A list of non negative integers
    #@return: A string
    # notice: string sorting for [101, 1] returns ['101', '1'] is wrong: result is 1011; while correct result is 1101
    def largestNumber(self, num):
        # write your code here
        if (len(num) == 0):
            return 0
        strArray = list()
        i = 0
        while (i < len(num)):
            strArray.append(str(num[i]))
            i += 1
        strArray = sorted(strArray, reverse = True)
        # print(strArray)

        # handle: 1 and 10
        i = len(strArray) - 1
        while (i >= 1):
            if (int(strArray[i - 1] + strArray[i]) < int(strArray[i] + strArray[i - 1])):
                temp = strArray[i - 1]
                strArray[i - 1] = strArray[i]
                strArray[i] = temp
                # [90, 9, 9]
                i = min(len(strArray) - 1, i + 1)
            else:
                i -= 1

        # print(strArray)

        result = ''
        i = 0
        while (i < len(strArray)):
            result += strArray[i]
            i += 1

        # use str(int()) for '00'
        # return str(int(result))
        # remove leading '0'
        if (strArray[0] == '0'):
            return '0'
        return str(int(result))

# Happy Number
# Write an algorithm to determine if a number is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of
# the squares of its digits, and repeat the process until the number equals 1
# (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
# Example
# 19 is a happy number
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
class SolutionHappyNumber:

    def __init__(self):
        self.midValues = set()

    def calcSquare(self, newNum):
        sum = 0
        while (True):
            oneDigit = newNum  % 10
            sum += (oneDigit * oneDigit)
            if (newNum < 10):
                return sum
            newNum = newNum // 10
        return None

    # return None means continue
    def check(self, newNum):
        if (newNum == 1):
            return True
        if (newNum in self.midValues):
            return False
        self.midValues.add(newNum)
        return None

    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        result = None
        newNum = n
        while (result == None):
            newNum = self.calcSquare(newNum)
            # print(newNum)
            result = self.check(newNum)
        return result

# Letter Combinations of a Phone Number
# Given a digit string excluded 01, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#  Notice
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# Given "23"
# Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
class SolutionLetterCombinationOfPhoneNumber:
    letterMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def getMap(self, ch):
        return self.letterMap[ch]

    def getWord(self, digits, digitList):
        word = ''
        i = 0
        while (i < len(digitList)):
            word += self.getMap(digits[i])[digitList[i]]
            i += 1
        return word

    def getNext(self, lenList, digitList):
        i = 0
        while (i < len(digitList)):
            currentIndex = digitList[i]
            if (currentIndex + 1 < lenList[i]):
                digitList[i] = currentIndex + 1
                return True
            else:
                digitList[i] = 0
            i += 1
        return False

    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        if (len(digits) == 0):
            return []
        lenList = list()
        i = 0
        while (i < len(digits)):
            lenList.append(len(self.getMap(digits[i])))
            i += 1
        # print(lenList)
        result = list()
        digitList = list(0 for x in range(len(lenList)))
        while (True):
            result.append(self.getWord(digits, digitList))
            if (not self.getNext(lenList, digitList)):
                return result
        return result

# Word Search
#
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
# Example
# Given board =
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
class SolutionWordSearchIn2DBoard:

    def recursiveSearch(self, board, word, path, i, j, wordIndex):
        # if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0])):
        #     return False
        if (path[i][j] == True):
            return False    # use only once
        if (board[i][j] == word[wordIndex]):
            if (wordIndex == len(word) - 1):
                return True
            path[i][j] = True # searched
            # print(path)
            if (j - 1 >= 0 and self.recursiveSearch(board, word, path, i, j - 1, wordIndex + 1)):
                return True
            if (i - 1 >= 0 and self.recursiveSearch(board, word, path, i - 1, j, wordIndex + 1)):
                return True
            if (j + 1 < len(board[0]) and self.recursiveSearch(board, word, path, i, j + 1, wordIndex + 1)):
                return True
            if (i + 1 < len(board) and self.recursiveSearch(board, word, path, i + 1, j, wordIndex + 1)):
                return True
        path[i][j] = False  # reset searched flag
        return False

    # not needed
    def clearPath(self, path):
        i = 0
        while (i < len(path)):
            j = 0
            while (j < len(path[0])):
                path[i][j] = False
                j += 1
            i += 1

    def search(self, board, word, path):
        i = 0
        while (i < len(board)):
            j = 0
            while (j < len(board[0])):
                # self.clearPath(path)
                if (self.recursiveSearch(board, word, path, i, j, 0)):
                    return True
                j += 1
            i += 1
        return False

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if (len(board) == 0):
            return False
        path = list()
        i = 0
        while (i < len(board)):
            path.append(list(False for x in range(len(board[0]))))
            i += 1
        return self.search(board, word, path)

# Divide Two Integers
# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return 2147483647
# Example
# Given dividend = 100 and divisor = 9, return 11.
class SolutionDivideTwoIntegers:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        if ((dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0)):
            negSign = False
        else:
            negSign = True
        if (dividend < 0):
            dividend = 0 - dividend
        if (divisor < 0):
            divisor = 0 - divisor

        if (divisor == 0 or dividend < divisor):
            return 0
        mid = list([divisor])

        while (dividend >= divisor and (dividend - divisor) >= (mid[-1] + mid[-1])):
            mid.append(mid[-1] + mid[-1])
            dividend -= mid[-1]
        # print(mid, dividend, divisor)
        MAX_RESULT = 2147483647
        result = 0
        i = 0
        power2 = 1
        while (True):
            result += power2
            if (result > MAX_RESULT and (not negSign)):
                return MAX_RESULT
            i += 1
            if (i >= len(mid)):
                break
            power2 <<= 1
        # print(mid, dividend, divisor, result)
        i = len(mid) - 1
        while (i >= 0):
            if (dividend - mid[i] >= divisor):
                result += power2
                if (result > MAX_RESULT and (not negSign)):
                    return MAX_RESULT
                dividend -= mid[i]
                if (dividend < divisor):
                    break
            power2 >>= 1
            i -= 1
        if (negSign):
            result = 0 - result
        return result

# Integer to Roman
# Given an integer, convert it to a roman numeral.
# The number is guaranteed to be within the range from 1 to 3999.
# Clarification
# 罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。
# 按照下面的规则可以表示任意正整数。
# 重复数次：一个罗马数字重复几次，就表示这个数的几倍。
# 右加左减：在一个较大的罗马数字的右边记上一个较小的罗马数字，表示大数字加小数字。
# 在一个较大的数字的左边记上一个较小的罗马数字，表示大数字减小数字。
# 但是，左减不能跨越等级。比如，99不可以用IC表示，用XCIX表示
# What is Roman Numeral?
# https://en.wikipedia.org/wiki/Roman_numerals
# https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
# http://baike.baidu.com/view/42061.htm
# Example
# 4 -> IV
# 12 -> XII
# 21 -> XXI
# 99 -> XCIX
# more examples at: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
class SolutionIntegerToRoman:
    # @param {int} n The integer
    # @return {string} Roman representation
    def intToRoman(self, n):
        if (n <=0 or n > 3999):
            return ''
        # Write your code here
        # oneDict = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', }
        oneDict = {1:'0', 2:'00', 3:'000', 4:'01', 5:'1', 6:'10', 7:'100', 8:'1000', 9:'02', }
        romanList = (['IVX', 'XLC', 'CDM'])
        romanList = (['IVX', 'XLC', 'CDM', 'M'])
        result = ''
        i = -1
        while (n > 0):
            i += 1
            if (i >= len(romanList)):
                return "overflow"
            digit = n % 10
            if (digit > 0):
                dict = oneDict[digit]
                roman = romanList[i]
                digitString = ''
                j = 0
                while (j < len(dict)):
                    digitString += roman[int(dict[j])]
                    j += 1
                result = digitString + result
            n //= 10
        return result

# Word Ladder
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
#  Notice
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# Example
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# solution: build a graph, O(N2) time, O(N)space
class SolutionWordLadder:
    def findWordInCurDict_TLE(self, curDict, word):
        i = 0
        while (i < len(curDict)):
            oneWord = curDict[i]
            diff = 0
            j = 0
            while (j < len(oneWord)):
                if (oneWord[j] != word[j]):
                    diff += 1
                    if (diff > 1):
                        break
                j += 1
            if (diff == 1):
                return True
            i += 1
        return False

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength_TLE(self, start, end, dict):
        # write your code here
        curDict = list([start])
        dictList = list(dict)
        dictList.append(end)
        step = 1
        while (len(dictList) > 0):
            nextDict = list()
            i = 0
            while (i < len(dictList)):
                word = dictList[i]
                if (self.findWordInCurDict(curDict, word)):
                    if (word == end):
                        return step + 1
                    del dictList[i]
                    nextDict.append(word)
                else:
                    i += 1
            curDict = nextDict
            print('curDict: ', curDict)
            if (len(curDict) == 0):
                return 0
            step += 1
        return 0

    def findWordInCurDict(self, curDict, word):
        for oneWord in curDict:
            diff = 0
            j = 0
            while (j < len(oneWord)):
                if (oneWord[j] != word[j]):
                    diff += 1
                    if (diff > 1):
                        break
                j += 1
            if (diff == 1):
                return True
        return False

    def ladderLength(self, start, end, dict):
        # write your code here
        curDict = set([start])
        # dict = set()
        dict.add(end)
        step = 1
        while (len(dict) > 0):
            nextDict = set()

            for word in dict:
                if (self.findWordInCurDict(curDict, word)):
                    if (word == end):
                        return step + 1
                    # dict.remove(word)
                    nextDict.add(word)
            dict -= nextDict
            curDict = nextDict
            print('curDict: ', curDict)
            if (len(curDict) == 0):
                return 0
            step += 1
        return 0

# Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# Example
# Given the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
class SolutionSpiralMatrix:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        if (len(matrix) == 0):
            return list()
        # right, bottom, left, top
        retSize = len(matrix[0]) * len(matrix)
        border = list([len(matrix[0]) - 1, len(matrix) - 1, 0, 1])
        nextValue = [[0, 1], [1,0], [0,-1], [-1,0]]
        borderIndex = 0
        row = 0
        col = 0
        ret = list()
        while (True):
            # print(ret, row, col, borderIndex)
            ret.append(matrix[row][col])
            if (len(ret) == retSize):
                break # traverse all elements

            changeBorder = True
            while (changeBorder):
                changeBorder = False

                rowDelta = nextValue[borderIndex][0]
                newRow = row + rowDelta
                if (rowDelta > 0):
                    changeBorder = newRow > border[borderIndex]
                elif  (rowDelta < 0):
                    changeBorder = newRow < border[borderIndex]

                colDelta = nextValue[borderIndex][1]
                newCol = col + colDelta
                if (colDelta > 0):
                    changeBorder = newCol > border[borderIndex]
                elif (colDelta < 0):
                    changeBorder = newCol < border[borderIndex]

                if (changeBorder):
                    border[borderIndex] -= (rowDelta + colDelta)
                    borderIndex = (borderIndex + 1) % len(border)
            row = newRow
            col = newCol
        return ret

# Spiral Matrix II
# Given an integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# Example
# Given n = 3,
# You should return the following matrix:
# [
#   [ 1, 2, 3 ],
#   [ 8, 9, 4 ],
#   [ 7, 6, 5 ]
# ]
class SolutionSprialMatrixII:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        if (n == 0):
            return []
        # Write your code here
        ret = [ [0 for x in range(n)] for x in range(n)]
        border = [n - 1, n - 1, 0, 1]
        nextValue = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        borderIndex = 0
        row = 0
        col = 0
        i = 1
        while (True):
            # print(ret, row, col, borderIndex)
            ret[row][col] = i
            if (i == n * n):
                break;
            i += 1
            changeBorder = True
            while (changeBorder):
                changeBorder = False

                rowDelta = nextValue[borderIndex][0]
                newRow = row + rowDelta
                if (rowDelta > 0):
                    changeBorder = newRow > border[borderIndex]
                elif (rowDelta < 0):
                    changeBorder = newRow < border[borderIndex]

                colDelta = nextValue[borderIndex][1]
                newCol = col + colDelta
                if (colDelta > 0):
                    changeBorder = newCol > border[borderIndex]
                elif (colDelta < 0):
                    changeBorder = newCol < border[borderIndex]

                if (changeBorder):
                    border[borderIndex] -= (rowDelta + colDelta)
                    borderIndex = (borderIndex + 1) % len(border)
            row = newRow
            col = newCol
        return ret

# Generate Parentheses
# Given n pairs of parentheses, write a function to
# generate all combinations of well-formed parentheses.
# Example
# Given n = 3, a solution set is:
# "((()))", "(()())", "(())()", "()(())", "()()()"
class SolutionGenerateParentthese_wrong:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        if (n <= 0):
            return [""]
        i = 1
        ret = set(["()"])
        while (i < n):
            newRet = set([])
            for str in ret:
                newRet.add(str + "()")
                newRet.add("()" + str)
                newRet.add("(" + str + ")")
            ret = newRet
            i += 1
        return list(ret)

# solution: "((("
#  r(i-1) <= r(i)
#  i <= r(i) <= len
# 0123: each time try to add last digit; when increase high position, all latter r(i) should be reset as max(r(i-1), i)
class SolutionGenerateParentthese:
    def generateOne(self, rightPos):
        ret = '('
        pos = 0 # 0 means after leftBracket#0
        i = 0
        while (i < len(rightPos)):
            if (rightPos[i] == pos):
                ret += ')'
                i += 1
            else:
                pos += 1
                ret += '('
        return ret

    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        if (n <= 0):
            return [""]
        if (n == 1):
            return ["()"]
        rightPos = [x for x in range(n)]  # init as [0123]
        ret = []
        while (rightPos[0] < n):
            print(rightPos)
            ret.append(self.generateOne(rightPos))
            # generate next right positions
            i = n - 2 # last pos is always n - 1
            while (i >= 0):
                rightPos[i] += 1
                if (rightPos[i] < n):
                    j = i + 1     # last pos is always n - 1
                    while (j < n - 1):
                        rightPos[j] = max(rightPos[j - 1], j)
                        j += 1
                    break
                i -= 1
        return ret

# Linked List Cycle II
# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
# Example
# Given -21->10->4->5, tail connects to node index 1，return 10
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class SolutionLinkedListCycleII:
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        fast = head
        slow = head
        while (True):
            if (slow == None):
                return None
            slow = slow.next

            if (fast == None):
                return None
            fast = fast.next
            if (fast == None):
                return None
            fast = fast.next
            if (slow == fast):
                break  # find cycle
        # a + b = L1, a is head
        # c + b = L2, b&c is slow
        L1 = 0
        p = head
        while (p != slow):
            L1 += 1
            p = p.next

        L2 = 1
        p = slow.next
        while (p != slow):
            L2 += 1
            p = p.next

        if (L1 > L2):
            p1 = head
            p2 = slow
        else:
            p1 = slow
            p2 = head
        # p1 move abs(L1 - L2) steps first
        i = 0
        while (i < abs(L1 - L2)):
            p1 = p1.next
            i += 1
        # move at the same time
        while (p1 != p2):
            p1 = p1.next
            p2 = p2.next
        # print('find begin node: ', p1.val)
        return p1

# Edit Distance
# Given two words word1 and word2, find the minimum number of steps
# required to convert word1 to word2. (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# Example
# Given
# word1 = "mart" and word2 = "karma",
# return 3.
# solution: for each char of word1, find same sub-string
#               L1<same>R1
#               R2<same>R2
# optimize: for "ma", when search "m", we can note down "a"'s position to avoid re-calc
# TODO:WRONG SOLUTION
class SolutionEditDistance:
    def calcDistance(self, word1, word2, i1, i2, currentMin):
        diff = 0
        # [start, end)
        start = -1 * max(i1, i2)
        end = max(len(word1) - i1, len(word2) - i2)
        if (abs(i1 - i2) + abs((len(word1) - i1) - (len(word2) - i2)) >= currentMin):
            return currentMin
        i = start
        while (i < end):
            if (i + i1 < 0 or i + i1 >= len(word1)):
                diff += 1
                i += 1
                continue
            if (i + i2 < 0 or i + i2 >= len(word2)):
                diff += 1
                i += 1
                continue
            if (word1[i + i1] != word2[i + i2]):
                diff += 1
            i += 1
        return diff

    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        ret = max(len(word1), len(word2))  # when no char is the same
        i1 = 0
        while (i1 < len(word1)):
            i2 = 0
            while (i2 < len(word2)):
                if (word1[i1] == word2[i2]):
                    distance = self.calcDistance(word1, word2, i1, i2, ret)
                    # print(ret, distance, i1, i2)
                    ret = min(ret, distance)

                i2 += 1
            i1 += 1
        return ret

# c++ solution
# class Solution {
# public:
#     int minDistance(string word1, string word2) {
#         // Start typing your C/C++ solution below
#         // DO NOT write int main() function
#         int row = word1.length() + 1;
#         int col = word2.length() + 1;
#
#         vector<vector<int> > f(row, vector<int>(col));
#
#         for (int i = 0; i < row; i++)
#             f[i][0] = i;
#
#         for (int i = 0; i < col; i++)
#             f[0][i] = i;
#
#         for (int i = 1; i < row; i++)
#             for (int j = 1; j < col; j++){
#                 if (word1[i-1] == word2[j-1])
#                     f[i][j] = f[i-1][j-1];
#                 else
#                     f[i][j] = f[i-1][j-1] + 1;
#                 f[i][j] = min(f[i][j], min(f[i-1][j]+1, f[i][j-1]+1));
#             }
#
#         return f[row-1][col-1];
#     };
# };

# Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of
# the longest consecutive elements sequence.
# Clarification
# Your algorithm should run in O(n) complexity.
# Example
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# solution: use a hash
class SolutionLongestConsecutiveSequence:
    def searchFlag(self, flag, n, incre):
        ret = 0
        while (True):
            if (n in flag):
                ret += 1
                flag.remove(n)
                n += incre
            else:
                break
        return ret

    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        flag = set(num)
        i = 0
        ret = 0
        while (i < len(num)):
            asc = self.searchFlag(flag, num[i], 1)
            desc = self.searchFlag(flag, num[i] - 1, -1)
            if (asc + desc > ret):
                ret = asc + desc
            i += 1
        return ret
#
# First Missing Positive
# Given an unsorted integer array, find the first missing positive integer.
# Example
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Challenge
# Your algorithm should run in O(n) time and uses constant space.
# solution: radix-sorting, [min, max] put in the array; n can be changed as remaining length
#           init: min is 1 & max is len(A)
#           when i <= min or i > n, skip and reduce length
#           note: there may be dup numbers
class SolutionFirstMissingPositive:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if (len(A) == 0):
            return 1
        left = 0
        right = len(A) - 1
        lastInt = len(A)
        while (left <= right):
            num = A[left]
            if ((num < (left + 1)) or (num > lastInt)):
                A[left] = A[right] # skip A[left], swap and try A[right]
                lastInt -= 1
                right -= 1
                continue
            if (num == left + 1):
                # good sorting
                left += 1
            else:
                if (A[num - 1] == num):
                    A[left] = A[right] # skip A[left], swap and try A[right]
                    lastInt -= 1
                    right -= 1
                    continue
                A[left] = A[num - 1] # next number to try
                A[num - 1] = num     # radix sort: put in correct position
        # print(A, left, right)
        if (right < 0):  # 1 does not exist
            return 1
        return A[right] + 1

# Palindrome Linked List
# Implement a function to check if a linked list is a palindrome.
# Example
# Given 1->2->1, return true
# solution: find mid point of the list, break and revert first half
class SolutionPalindromeLinkedList:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        ret = False
        length = 0
        p = head
        while (p != None):
            length += 1
            p = p.next
        if (length == 0):
            return True
        if (length == 1):
            return True

        # revert first half
        i = 0
        p = None
        c = head
        n = c.next
        while (i < length // 2):
            c.next = p
            p = c
            c = n
            n = n.next
            i += 1
        second = c
        if (length % 2 == 1):
            second = c.next

        # compare first(p) and second
        while (p != None):
            if (p.val != second.val):
                return False
            p = p.next
            second = second.next
        return True

# Number of Islands
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
# Find the number of islands.
# Example
# Given graph:
# [
#   [1, 1, 0, 0, 0],
#   [0, 1, 0, 0, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1]
# ]
# return 3.
class SolutionNumberOfIslands_wrong:
    def fillSameRow(self, grid, row, col, island):
        j = col + 1
        while (j < len(grid[row])):
            if (grid[row][j] == 1):
                grid[row][j] = island
                j += 1
            else:
                break
        j = col - 1
        while (j >= 0):
            if (grid[row][j] == 1):
                grid[row][j] = island
                j -= 1
            else:
                break

    # return: True if filled; False if no fill
    def fill(self, grid, row, island):
        col = 0
        ret = False
        while (col < len(grid[row])):
            if (grid[row][col] != 1):
                col += 1
                continue
            # left
            if (col - 1 >= 0 and grid[row][col - 1] == island):
                grid[row][col] = island
                col += 1
                ret = True
                continue
            # top. row - 1 must > 0
            if (grid[row - 1][col] == island):
                grid[row][col] = island
                col += 1
                ret = True
                continue
            # right and right-top
            ############### WRONG OCCURS HERE ######################
            ############### SHOULD CHECK WHOLE LINE ################
            if (col + 1 < len(grid[row]) and
                grid[row - 1][col + 1] == island and
                grid [row][col + 1] == 1):
                grid[row][col] = island
                grid[row][col + 1] = island
                col += 2
                ret = True
                continue;
            col += 1
        return ret

    def search(self, grid, row, col, island):
        if (grid[row][col] != 1):
            return False
        grid[row][col] = island
        self.fillSameRow(grid, row, col, island)
        row += 1
        while (row < len(grid)):
            if (not self.fill(grid, row, island)):
                break
            row += 1
        return True

    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        island = 2
        row = 0
        col = 0
        while (row < len(grid)):
            while (col < len(grid[row])):
                if (self.search(grid, row, col, island)):
                    island += 1
                col += 1
            col = 0
            row += 1

        i = 0
        j = 0
        while (i < len(grid)):
            rowString = ""
            while (j < len(grid[i])):
                rowString += ', %-3d' % grid[i][j]
                if (not self.check(grid, i, j)):
                    print("error:", i, j)
                j += 1
            print(rowString)
            j = 0
            i += 1
        print(grid)
        return island - 2

    def check(self, grid, row, col):
        if (grid[row][col] == 0):
            return True
        if (row - 1 >= 0):
            if (not (grid[row - 1][col] == 0 or grid[row - 1][col] == grid[row][col])):
                return False
        if (row + 1 < len(grid)):
            if (not (grid[row + 1][col] == 0 or grid[row + 1][col] == grid[row][col])):
                return False
        if (col + 1 < len(grid[row])):
            if (not (grid[row][col + 1] == 0 or grid[row][col + 1] == grid[row][col])):
                return False
        if (col - 1 >= 0):
            if (not (grid[row][col - 1] == 0 or grid[row][col - 1] == grid[row][col])):
                return False
        return True

class SolutionNumberOfIslands:
    def fillRow(self, grid, row, col, island):
        if (row + 1 < len(grid) and grid[row + 1][col] == 1):
            grid[row + 1][col] = island
            self.fillRow(grid, row + 1, col, island)
        if (row - 1 >= 0 and grid[row - 1][col] == 1):
            grid[row - 1][col] = island
            self.fillRow(grid, row - 1, col, island)

        j = col + 1
        while (j < len(grid[row])):
            if (grid[row][j] == 1):
                grid[row][j] = island
                if (row + 1 < len(grid) and grid[row + 1][j] == 1):
                    grid[row + 1][j] = island
                    self.fillRow(grid, row + 1, j, island)
                if (row - 1 >= 0 and grid[row - 1][j] == 1):
                    grid[row - 1][j] = island
                    self.fillRow(grid, row - 1, j, island)
                j += 1
            else:
                break
        j = col - 1
        while (j >= 0):
            if (grid[row][j] == 1):
                grid[row][j] = island
                if (row + 1 < len(grid) and grid[row + 1][j] == 1):
                    grid[row + 1][j] = island
                    self.fillRow(grid, row + 1, j, island)
                if (row - 1 >= 0 and grid[row - 1][j] == 1):
                    grid[row - 1][j] = island
                    self.fillRow(grid, row - 1, j, island)
                j -= 1
            else:
                break

    def search(self, grid, row, col, island):
        if (grid[row][col] != 1):
            return False
        grid[row][col] = island
        self.fillRow(grid, row, col, island)
        return True

    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        island = 2
        row = 0
        col = 0
        while (row < len(grid)):
            while (col < len(grid[row])):
                if (self.search(grid, row, col, island)):
                    island += 1
                col += 1
            col = 0
            row += 1

        ############# code to verify result ###########################
        i = 0
        j = 0
        while (i < len(grid)):
            rowString = ""
            while (j < len(grid[i])):
                rowString += ', %-3d' % grid[i][j]
                if (not self.check(grid, i, j)):
                    print("error:", i, j)
                j += 1
            print(rowString)
            j = 0
            i += 1
        print(grid)
        return island - 2

    def check(self, grid, row, col):
        if (grid[row][col] == 0):
            return True
        if (row - 1 >= 0):
            if (not (grid[row - 1][col] == 0 or grid[row - 1][col] == grid[row][col])):
                return False
        if (row + 1 < len(grid)):
            if (not (grid[row + 1][col] == 0 or grid[row + 1][col] == grid[row][col])):
                return False
        if (col + 1 < len(grid[row])):
            if (not (grid[row][col + 1] == 0 or grid[row][col + 1] == grid[row][col])):
                return False
        if (col - 1 >= 0):
            if (not (grid[row][col - 1] == 0 or grid[row][col - 1] == grid[row][col])):
                return False
        return True

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class SolutionHasCycle:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if (head == None):
            return False
        fast = head
        slow = head
        while (True):
            fast = fast.next
            if (fast == None):
                return False
            fast = fast.next
            if (fast == None):
                return False
            slow = slow.next
            if (slow == fast):
                return True


# Example
# Given a binary tree as follow:
#   1
#  / \
# 2   3
#    / \
#   4   5
# The maximum depth is 3.
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class SolutionMaxDepth:
    def __init__(self):
        self.maxRet = 0

    def traverse(self, root, depth):
        depth += 1
        if (depth > self.maxRet):
            self.maxRet = depth
        if (root.left != None):
            self.traverse(root.left, depth)
        if (root.right != None):
            self.traverse(root.right, depth)
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth1(self, root):
        # write your code here
        if (root == None):
            return 0
        self.traverse(root, 0)
        return self.maxRet

    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Reverse Words in a String
# Given an input string, reverse the string word by word.
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# Clarification
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
class SolutionReverseWordsInAString:
    def firstPos(self, s, start, isFindSpace):
        i = start
        while (i < len(s)):
            if (isFindSpace and (s[i] == ' ')):
                return i
            if ((not isFindSpace) and (s[i] != ' ')):
                return i
            i += 1
        return -1  # not found

    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        ret = ''
        i = 0
        l = len(s)
        while (i < l):
            start = self.firstPos(s, i, False)
            # print('start: ', start)
            if (start == -1):
                break
            end = self.firstPos(s, start + 1, True)
            # print('end: ', end)
            if (end == -1):
                end = len(s)  # final word
            # append the word to the head
            # print('sub: ', s[start : (end - start)])
            if (len(ret) == 0):
                ret = s[start : end] + ret
            else:
                ret = s[start : end] + ' ' + ret
            i = end + 1
        return ret


# Valid Sudoku
# Determine whether a Sudoku is valid.
# The Sudoku board could be partially filled,
# where empty cells are filled with the character ..
#  Notice
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.
class SolutionValidSudoku:
    def checkRow(self, board, x, y, rows):
        # check rows
        i = x
        flag = [0 for v in range(9)]  # reset flag
        while (i < x + rows):
            row = board[i]
            j = y
            while (j < y + rows):
                # print('%d, %d' % (i, j))
                if (row[j] != '.'):
                    # check flag
                    # print(str(row[j]), ' - ', int(row[j]))
                    if (flag[int(row[j]) - 1] != 0):
                        return False
                    # set flag
                    flag[int(row[j]) - 1] = 1
                j += 1
            i += 1
            if (rows > 3):
                flag = [0 for v in range(9)]  # reset flag
            # else:
            #     print(flag)
        # print(flag)
        return True

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        flag = [0 for x in range(9)]

        # print(len(board), ', ', len(board[0]))
        # check rows
        if (not self.checkRow(board, 0, 0, 9)):
            return False
        x = 0
        y = 0
        while (x <= 2):
            if (not self.checkRow(board, x, y, 3)):
                return False
            y = (y + 3)
            if (y > 6):
                y = 0
                x += 1

        # i = 0
        # while (i < len(board)):
        #     flag = [0 for x in range(9)] # reset flag
        #     row = board[i]
        #     j = 0
        #     while (j < len(row)):
        #         # print('%d, %d' % (i, j))
        #         if (row[j] != '.'):
        #             # check flag
        #             # print(str(row[j]), ' - ', int(row[j]))
        #             if (flag[int(row[j]) - 1] != 0):
        #                 return False
        #             # set flag
        #             flag[int(row[j]) - 1] = 1
        #         j += 1
        #     i += 1

        # check columns
        i = 0
        while (i < len(board[0])):
            flag = [0 for x in range(9)] # reset flag
            j = 0
            while (j < len(board[0])):
                if (board[j][i] != '.'):
                    # check flag
                    if (flag[int(board[j][i]) - 1] != 0):
                        return False
                    # set flag
                    flag[int(board[j][i]) - 1] = 1
                j += 1
            i += 1

        # check grid
        return True

# Decode Ways
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# Example
# Given encoded message 12, it could be decoded as AB (1 2) or L (12).
# The number of ways decoding 12 is 2.
# solution:
# DP: ret(n) = ret(n-1) + x
#     x: 0,        if [n-2][n-1] can not be decoded
#     x: ret(n-2), if [n-2][n-1] can be decoded
class SolutionDecodeWays:
    def canDecode(self, s, i):
        if (s[i - 1] == '0'):
            return False
        temp = int(s[i - 1]) * 10 + int(s[i])
        return (1 <= temp and temp <= 26)

    def getNum(self, s, i, n2, n1):
        if (self.canDecode(s, i)):
            if (s[i] != '0'):
                return n2 + n1
            else:
                return n2
        else:
            if (s[i] != '0'):
                return n1
            else:
                return 0

    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        # Write your code here
        if (len(s) == 0):
            return 0
        if (s[0] != '0'):
            n2 = 1
        else:
            n2 = 0
        if (len(s) == 1 or n2 == 0):
            return n2

        if (self.canDecode(s, 1)):
            if (s[1] != '0'):
                n1 = 2
            else:
                n1 = 1
        else:
            if (s[1] != '0'):
                n1 = 1
            else:
                return 0
        if (len(s) == 2):
            return n1

        i = 2
        while (i < len(s)):
            ret = self.getNum(s, i, n2, n1)
            if (ret == 0):
                return 0
            n2 = n1
            n1 = ret
            i += 1
        return ret

class SolutionDecodeWays_2:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def canDecode(self, s, i):
        if (s[i - 1] == '0'):
            return False
        temp = int(s[i - 1]) * 10 + int(s[i])
        return (1 <= temp and temp <= 26)

    def getNum(self, s, i, n2, n1):
        if (i < 0):
            return 0
        if (i == 0):
            if (s[i] == '0'):
                return 0
            else:
                return 1

        ret = 0
        if (s[i] != '0'):
            ret += n1
        if (self.canDecode(s, i)):
            if (n2 == 0):
                ret += 1
            else:
                ret += max(n2, 1)
        return ret

    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        # Write your code here
        ret = 0
        n2 = 0
        n1 = 0
        i = 0
        while (i < len(s)):
            ret = self.getNum(s, i, n2, n1)
            if (ret == 0):
                return 0
            n2 = n1
            n1 = ret
            i += 1
        return ret

# Binary Tree Maximum Path Sum
# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.
# Example
# Given the below binary tree:
#   1
#  / \
# 2   3
# return 6.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class SolutionBinaryTreeMaximumPathSum:
    def __init__(self):
        self.maxKnownPathSum = -2147483648

    def recursiveCalc(self, root):
        if (root == None):
            return 0
        pathLeft = self.recursiveCalc(root.left)
        pathRight = self.recursiveCalc(root.right)
        maxKnownPathSum = pathLeft + root.val + pathRight
        self.maxKnownPathSum = max(
            self.maxKnownPathSum,
            maxKnownPathSum,
            root.val)
        return max(pathLeft, pathRight) + root.val

    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        ret = self.recursiveCalc(root)
        return max(ret, self.maxKnownPathSum)


# Minimum Path Sum
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#  Notice
# You can only move either down or right at any point in time.
# TLE solution, O(2^(M*N))
class SolutionMinimumPathSum_TLE:
    def recursiveGetMinPath(self, grid, row, col):
        # if ((row == len(grid) - 1) and (col == len(grid[0]) - 1)):
        #     return grid[row][col]
        # go down
        down = 2147483647
        if ((row + 1 <= len(grid) - 1)):
            down = self.recursiveGetMinPath(grid, row + 1, col)
        right = 2147483647
        if ((col + 1 < len(grid[0]))):
            right = self.recursiveGetMinPath(grid, row, col + 1)
        if (down == 2147483647 and right == 2147483647):
            ret = grid[row][col]
        else:
            ret = min(right, down) + grid[row][col]
        # print("[%d,%d] - %d, [%d, %d]" % (row, col, ret, right, down))
        return ret

    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if (grid == None or len(grid) == 0):
            return 0
        return self.recursiveGetMinPath(grid, 0, 0)

# DP
# path_matrix[i,j] =
# min(path_matrix[i, j - 1], path_matrix[i - 1, j]) + grid[i,j]
class SolutionMinimumPathSum:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if (grid == None or len(grid) == 0):
            return 0
        matrix = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        matrix[0][0] = grid[0][0]
        row = 1
        while (row < len(grid)):
            matrix[row][0] = matrix[row - 1][0] + grid[row][0]
            row += 1
        col = 1
        while (col < len(grid[0])):
            matrix[0][col] = matrix[0][col - 1] + grid[0][col]
            col += 1

        row = 1
        while (row < len(grid)):
            col = 1
            while (col < len(grid[0])):
                matrix[row][col] = min(matrix[row][col - 1], matrix[row - 1][col]) + grid[row][col]
                col += 1
            row += 1

        return matrix[row - 1][col - 1]

# Reorder List
# Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln
# reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# Example
# Given 1->2->3->4->null, reorder it to 1->4->2->3->null.
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# solution
# break the list in the middle. and reverse left list
# l, m, r
# each step: r -> m, l -> r. Then: m = l, l = l.next, r = r.next
# 1,2,3,4,5
#   l m r
# 1,2,3,4,5,6
#     l r (m=None)
class SolutionReorderList:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        # find length
        lenList = 0
        p = head
        while (p != None):
            lenList += 1
            p = p.next
        if (lenList <= 1):
            return head

        # find middle
        l = head
        i = 1
        while (i < lenList // 2):
            l = l.next
            i += 1
        # m is the REAL middle
        r = l.next
        m = None  # for even-length
        if (lenList % 2 == 1):
            m = l.next # for odd-length
            r = m.next
            m.next = None

        # reverse left list
        p = head
        pPrev = None
        pNext = p.next
        while (True):
            p.next = pPrev  # reverse
            pPrev = p
            p = pNext
            pNext = pNext.next
            if (pPrev == l):
                break

        # l, m, r
        # each step: r -> m, l -> r. Then: m = l, l = l.next, r = r.next
        while (l != None and r != None):
            rNext = r.next
            r.next = m
            lNext = l.next
            l.next = r

            m = l
            l = lNext
            r = rNext
        return head

# Triangle
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below Notice
# Bonus point if you are able to do this using only O(n)
# extra space, where n is the total number of rows in the triangle.
# Example
# Given the following triangle:
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# solution
# store length in each row, then find the min value in last row
# [
#      [2],
#     [5,6],
#    [11,10,13],
#   [15,11,18,13]
# ]

class SolutionTriangle:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if (triangle == None or len(triangle) == 0):
            return 0
        row = 1
        while (row < len(triangle)):
            col = 0
            while (col < len(triangle[row])):
                # calc min path values of last 2 numbers of upper row
                if (col == 0):
                    # for first and last number
                    triangle[row][0] += triangle[row - 1][0]
                elif (col == len(triangle[row]) - 1):
                    triangle[row][col] += triangle[row - 1][col - 1]
                else:
                    triangle[row][col] += min(triangle[row - 1][col - 1], triangle[row - 1][col])
                col += 1
            row += 1
        # search in last row for min value
        ret = 2147483647
        row = len(triangle) - 1
        col = 0
        while (col < len(triangle[row])):
            ret = min(triangle[row][col], ret)
            col += 1
        return ret