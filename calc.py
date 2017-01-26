# -*- coding: utf-8 -*-
###########################################
# 四则运算


result = [0] * 40
result[0] = 0
result[1] = 1
for i in range(2, 40):
  result[i] = result[i - 1] + result[i - 2]
  print('fib(%2d): ' % i, result[i])


###### recursive algorithm ############
def fib(x):
  if x == 0:
    return 0
  if x == 1:
    return 1
  return fib(x - 1) + fib(x - 2)
  
for i in range(40):
  print('fib(%2d): ' % i, fib(i))
