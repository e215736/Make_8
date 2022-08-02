class Controller:
    def __init__(self,model): #コンストラクタ
        self.model = model #modelへの参照
        self.model.setFormula() #modelへ通知
        
    def onPress(self): #ボタンが押された時の処理
        pass
       
