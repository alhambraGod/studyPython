
junyi=135
while True:
  i= input('请输入一个数字：')
  print('你输入的是',i)
  mama=int(i)
  if(mama==junyi) :
    print('猜中了！')
    break
  else:
    if(mama<junyi):
      print('你的数字小')
    else:
      print('你的数字大')
  print('加油，再来一次吧\n')

print('成功，欢迎再来')

#
# exit()

junyi = 123
while True:
  i = input('妈妈，输入一个数字: ')
  print('妈妈，你输入的是: ', i)
  mama = int(i)
  if (mama == junyi):
    print('猜中了！')
    break
  else:
    if (mama < junyi):
      print('妈妈的数字小')
    else:
      print('妈妈的数字大')
    print('再来一次吧\n')

print('成功，byebye')


############ end ###############
############################
# p=print
# p(98989)