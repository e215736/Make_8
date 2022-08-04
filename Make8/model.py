import random
import set
from kivy.uix.popup import Popup

class Model:

    def __init__(self, view):
        self.view = view
        
    def setNum(self):
        random.shuffle(set.q_num)

    def judgeScene(self,scene): # シーン判定
        if scene == 'playing':
            if set.ans == 0:
                set.formula.clear()
                self.setNum()
                self.setFormula()
                self.setButton()
            else:
                set.formula.clear()
                self.view.showInput(set.formula)
                self.setFormula()
                self.setButton()
        if scene == 'correct' and set.ans == len(set.q_num):
            scene = 'allcorrect'
        if scene == 'title':
            self.setNum()
            set.ans == 0
        self.view.changeScene(scene)

    def setFormula(self): # 問題をセット
        self.view.showFormula(set.questions[set.q_num[set.ans]][0]) #viewへ通知
        
    def setButton(self): # 式をボタンに代入
        self.view.showButton(set.questions[set.q_num[set.ans]]) #viewへ通知
    
    def setValue(self,key): #値を入力
        if type(key)==int:
            set.formula.append(set.questions[set.q_num[set.ans]][key])
        else:
            set.formula.append(key)
        self.view.showInput(set.formula)
    
    def delvalue(self): # 入力式の削除
        if len(set.formula)>=1:
            set.formula.pop(-1)
            self.view.showInput(set.formula)
        pass

    def judgement(self): #正誤判定
        if len(set.formula)>=1:
            f = ' '.join(map(str, set.formula))
            f = f.translate(str.maketrans({'－': '-', '×': '*', '÷': '/'}))
            if len(set.formula) == 7 and eval(f) == 8:
                print('OK')
                set.ans += 1
                self.judgeScene('correct')
            else:
                print('NG')
                popup = Failpopup()
                popup.open()
        pass

class Failpopup(Popup):
    pass
