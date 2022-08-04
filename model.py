class Model:
    def __init__(self, view): #コンストラクタ
        self.value = '4839'
        self.view = view #viewへの参照
        
    def setFormula(self): #式を入力
        self.view.showFormula(self.value) #viewへ通知
        
    def setButton(self): #式を入力
        self.view.showButton(self.value) #viewへ通知
        
    def setValue(self,value): #値を入力
        self.view.showValue(value)
        
    
    def calculate(): #計算をする
        pass
    
    def coiseFormula(): #問題をランダムに選択
        pass
    
    def judgement(): #正誤判定
        pass