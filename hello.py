# coding: gbk
from random import randint
num = randint(1, 100)             # Ϊ�˺�������������㣬�Ȱ�a��Ϊ1
bingo = False
while bingo == False:     # ���a������0��ѭ����1������0��
    print("please input")
    a = int(input())  # ��ѭ���ڲ���ȡ���룬�ı�a��ֵ�����뿴���Ļ���������
    if a<num:
        print("small")
    elif a > num:
        print ("big")
    else:
        print("bingo")
        bingo=True
print("over")