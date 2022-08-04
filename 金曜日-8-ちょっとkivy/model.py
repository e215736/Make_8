import random
import set


class Model:
    formula = []

    def __init__(self, view):
        self.value = '4839'
        self.view = view
        self.setNum()
        
    def setNum(self):
        random.shuffle(set.q_num)

    def setFormula(self): #式をセット
        self.view.showFormula(set.questions[set.q_num[set.ans]][0]) #viewへ通知
        
    def setButton(self): #式を入力
        self.view.showButton(set.questions[set.q_num[set.ans]]) #viewへ通知
    
    def setValue(self,key): #値を入力
        #self.formula.append(set.questions[set.q_num[set.ans]][key])
        print(self.formula)
        #self.view.showValue(self.fomula)
    
    def delvalue():
        pass
    
    def calculate(): #計算をする
        pass
    
    def coiseFormula(): #問題をランダムに選択
        pass
    
    def judgement(): #正誤判定
        pass
