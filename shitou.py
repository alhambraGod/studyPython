# -*- coding: gb2312 -*-
#����ʯͷ��С��Ϸ
import random
#cai = ['ʯͷ','����','��']
cai = ['1','2','3']
#ying = [['ʯͷ','����'],['����','��'],['��','ʯͷ']]
ying = [['1','2'],['2','3'],['3','1']]
ju = int(input('�������ܾ���: '))
pingju = 0
win = 0
lose = 0
i = 1

while i <=ju:
    wocai = input('�������'+str(i)+'��,����ʯͷ��: ')
    computer = random.choice(cai)

    if wocai in cai:
        print('����!����������:{0:s}!'.format(computer))
        if wocai == computer:
            print('����,��͵��������һ���İ�!')
            pingju += 1
        elif [wocai,computer] in ying:
            print('����,��ϲ��,��ֲ�ȭ��Ӯ��!')
            win += 1
        else:
            print('��Ŷ,������,��ֲ�ȭ���俩!')
            lose += 1
        i += 1
    else:
        print('��������ȷ������: ')
print('���β�ȭ��ս����:{0:d}ƽ��,{1:d}Ӯ,{2:d}��'.format(pingju,win,lose))