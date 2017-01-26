# -*- coding: gb2312 -*-
#剪刀石头布小游戏
import random
#cai = ['石头','剪刀','布']
cai = ['1','2','3']
#ying = [['石头','剪刀'],['剪刀','布'],['布','石头']]
ying = [['1','2'],['2','3'],['3','1']]
ju = int(input('请输入总局数: '))
pingju = 0
win = 0
lose = 0
i = 1

while i <=ju:
    wocai = input('请输入第'+str(i)+'局,剪刀石头布: ')
    computer = random.choice(cai)

    if wocai in cai:
        print('嘿咻!电脑掷出了:{0:s}!'.format(computer))
        if wocai == computer:
            print('真巧,你和电脑想的是一样的哎!')
            pingju += 1
        elif [wocai,computer] in ying:
            print('啊哈,恭喜你,这局猜拳你赢了!')
            win += 1
        else:
            print('啊哦,悲剧啦,这局猜拳你输咯!')
            lose += 1
        i += 1
    else:
        print('请输入正确的手势: ')
print('本次猜拳的战绩是:{0:d}平局,{1:d}赢,{2:d}输'.format(pingju,win,lose))