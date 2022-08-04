

class Controller:
    def __init__(self,model): #コンストラクタ
        self.model = model #modelへの参照
        self.inputValue = ''
        self.model.setFormula() #modelへ通知
        self.model.setButton() #modelへ通知
        
    def onPress(self,key): #ボタンが押された時の処理、計算機参考
        if key.isdigit():
            self.model.setValue(key)
        elif key in "+-/*": #演算子キーか？ 
            #self.model.calculate
            self.model.setvValue(key)
        else:
            pass