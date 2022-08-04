class Controller:
    def __init__(self,model):
        self.model = model
        self.model.setFormula() #modelへ通知
        self.model.setButton() #modelへ通知
        
    def onClick(self,scene): #ボタンが押された時の処理
        sm.current = scene