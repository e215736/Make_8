import set

class Controller:
    def __init__(self,model):
        self.model = model # モデルへのアクセス
        
    def onClick(self,scene): # 指定したシーンへ遷移
        self.model.judgeScene(scene)
    
    def onBtn(self,key): # ボタンが押された時の処理
        if len(set.formula)<=6:
            if type(key)==int:
                self.model.setValue(key)
            elif key=='+':
                self.model.setValue(key)
            elif key=='－':
                self.model.setValue(key)
            elif key=='×':
                self.model.setValue(key)
            elif key=='÷':
                self.model.setValue(key)
            else:
                pass
        if key=="ok":
            self.model.judgement()
        elif key=="del":
            self.model.delvalue()
        else:
            pass