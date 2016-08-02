class M_langren(object):
    """狼人游戏的流程控制"""
    playerNum = 0
    langrenNum = 0
    day = 1
    mumber = []
    langrenList = []
    nvwuNum = 0
    YuyanNum = 0
    Zancun = []
    Nvwu_D = True
    Nvwu_J = True
    JingzhangNum = 0
    def __init__(self):
        
        return

    def setPlayer(self,P):
        
        self.playerNum = P
        return

    def setLangNum(self,K):
        
        self.langrenNum = K
        return

    def setPlayerList(self,P):
        a = 1
        for i in range(P):
            self.mumber.append(a)
            a+=1
        return

    
    def nextDay(self):
        self.day+=1
        return

    def setLangren(self,a):
        self.langrenList.append(a)
        return
    
    def setNvwuNum(self,a):
        self.nvwuNum = a
        return

    def setYuyanNum(self,a):
        self.YuyanNum = a
        return

    def act_Lang(self,a):
        
        self.mumber.remove(int(a))
        return

    def act_Nv(self,a,way):
        if way == 1:
            self.mumber.append(int(a))
        elif way == 2:
            b = self.mumber[:]
            for i in self.mumber:
                if i == a:
                    b.remove(int(i))
            self.mumber = b
        return

    def act_Yu(self,a):
        return (a in self.langrenList)

    def setZancun(self,a):
        self.Zancun.append(int(a))
        return

    def act_N(self):
        for i in self.Zancun:
            self.mumber.remove(i)
            
        return

    def setJingzhang(self,a):
        self.JingzhangNum=a
        return
    def isWin(self):
        Score_L = 0
        for i in self.langrenList:
            if i in self.mumber:
                Score_L+=1
        Score_P=len(self.mumber)-Score_L
        if self.JingzhangNum in self.langrenList:
            Score_L+=1
        else:
            Score_P+=1
        if Score_L>Score_P:
            print('狼人获胜')
            return True
        if len(self.mumber)<=1:
            print('平民胜利')
            return True
        return False