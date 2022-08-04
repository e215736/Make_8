import set

class Controller:
    def __init__(self,model):
        self.model = model
        self.model.setFormula() #modelへ通知
        self.model.setButton() #modelへ通知
        
    def onClick(scene): # 指定したシーンへ遷移
        set.sm.current = scene
    
    def onBtn(self,key): # ボタンが押された時の処理、計算機参考
        if key.isdigit():
            self.model.setValue(key)
        elif key=="ok":
            self.model.judgement()
        elif key=="del":
            self.model.delvalue()
        elif key in "+-/*": #演算子キーか？
            self.model.setValue(key)
        else:
            pass