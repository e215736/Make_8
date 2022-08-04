class Controller:
    def __init__(self,model):
        self.model = model
        self.model.setFormula() #modelへ通知
        self.model.setButton() #modelへ通知
        
    def onPress(self): #ボタンが押された時の処理
        pass