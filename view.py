class View:
    def __init__(self, ui_framework): #コンストラクタ
       self.uiFramework = ui_framework
       
    def showFormula(self,value):
        self.uiFramework.setDisplayFormula(value) #screen.pyのtextにvalueを入れる
        
    def showButton(self,value):
        self.uiFramework.setButtonText(value) #screen.pyのtextにvalueを入れる