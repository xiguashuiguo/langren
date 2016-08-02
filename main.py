#! /usr/bin/env python
# -*- coding: utf-8 -*- 

from M_langren  import *

def setLangrenList(M_):
    if M_.day == 1:
        for i in range(M_.langrenNum):
            print("请输入狼人编码：")
            a = input()
            M_.setLangren(a)
    
    return

def setNvwu(M_):
    if M_.day == 1:
        print("请输入女巫编码 ")
        a = input()
        M_.setNvwuNum(a)
    return

def setYuyan(M_):
    if M_.day == 1:
        print("请输入预言家编码： ")
        a = input()
        M_.setYuyanNum(a)
    return

def action_Langren(M_):
    
    print("狼人今晚目标是： ")
    print(M_.mumber)
    a=input()
    M_.setZancun(a)
    return

def action_Nvwu(M):
    r = (int(M.nvwuNum) in M.mumber)
    print("今晚死的是"+str(M.Zancun[0])+"是否使用解药？（1：是 ； 0：否）")
    a = input()
    a = int(a)
    if a  == 0 or (not r) or not(M.Nvwu_J):
        aa = False
    else:
        aa = True
    if(aa):
        M.Zancun.clear()
        M.Nvwu_J=False

    print("今晚是否使用毒药？（1：是 ； 0：否）")
    b = input()
    b = int (b)
    print("对谁使用")
    print(M.mumber)
    c = input()
    c = int(c)
    if b == 0 or (not r) or not(M.Nvwu_D):
        bb = False
    else:
        bb = True
    if bb :
        M.setZancun(c)
        M.Nvwu_D = False
    
    

def action_Yuyan(M):
    print("你要查验几号？")
    print(M.mumber)
    s = input()
    r = (int(M.YuyanNum) in M.mumber)
    if r and (M.act_Yu(s)):
        print(str(s)+"是狼人")
    elif r and not(M.act_Yu(s)):
        print(str(s)+"不是狼人")
    else:
        print("我不告诉你")
    
    return
    
        
def night(M):
    print("这是第"+str(M.day)+"夜")
    setLangrenList(M)
    action_Langren(M)
    print(M.Zancun)
    setNvwu(M)
    action_Nvwu(M)
    print(M.Zancun)
    setYuyan(M)
    action_Yuyan(M)
    print("夜晚结束，请大家睁眼！")
    M.act_N()
    return

def AboutJingzhang(M):
    if not(M.JingzhangNum in M.mumber):
        print('请输入警长玩家编号： ')
        print(M.mumber)
        a = input()
        a=int(a)
        M.setJingzhang(a)
    return

def Piaojue(M):
    print('请输入票死玩家编号： ')
    print(M.mumber)
    a = input()
    a = int(a)
    M.mumber.remove(a)

def day(M):

    M.nextDay()
    print("这是第"+str(M.day)+"天，昨夜阵亡：")
    print(M.Zancun)
    M.Zancun=[]
    AboutJingzhang(M)
    Piaojue(M)
    
    return

isRestart = True
while(True):
    if(isRestart):
        print('玩家个数：')
        P = input()
        P = int(P)
        print('狼人个数：')
        L = input()
        L = int(L)
    main = M_langren()
    main.setPlayer(P)
    main.setLangNum(L)
    main.setPlayerList(P)
    
    while(True):
        night(main)
        
        if main.isWin():
            print('是否重新开始(1：是；0：否)')
            a=input()
            a=int(a)
            if a == 0:
                isRestart = False
            else:
                isRestart = True
            break
        day(main)
        if main.isWin():
            print('是否重新开始(1：是；0：否)')
            a=input()
            a=int(a)
            if a == 0:
                isRestart = False
            else:
                isRestart = True
            break

    break
