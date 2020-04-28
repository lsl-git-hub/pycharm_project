# coding: gbk
from random import randint
num = randint(1, 100)             # 为了后面的条件能满足，先把a设为1
bingo = False
while bingo == False:     # 如果a不等于0就循环（1不等于0）
    print("please input")
    a = int(input())  # 在循环内部获取输入，改变a的值（想想看不改会怎样？）
    if a<num:
        print("small")
    elif a > num:
        print ("big")
    else:
        print("bingo")
        bingo=True
print("over")