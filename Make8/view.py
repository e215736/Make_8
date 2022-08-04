import set

class View:
    def __init__(self, ui_framework): #コンストラクタ
        self.uiFramework = ui_framework

    def showFormula(self,value): # 問題をセット
        s = set.sm.get_screen('playing')
        s.ids.question.text = value
        r = set.sm.get_screen('retire')
        r.ids.answer.text = set.questions[set.q_num[set.ans]][5]

    def showButton(self,value): # 式をボタンに代入
        s = set.sm.get_screen('playing')
        s.ids.btn1.text = str(value[1])
        s.ids.btn2.text = str(value[2])
        s.ids.btn3.text = str(value[3])
        s.ids.btn4.text = str(value[4])

    def showInput(self,list): # 入力中の式を表示
        formula = ' '.join(map(str, list))
        s = set.sm.get_screen('playing')
        s.ids.formula.text = formula
    
    def changeScene(self,scene): # シーン遷移
        set.sm.current = scene