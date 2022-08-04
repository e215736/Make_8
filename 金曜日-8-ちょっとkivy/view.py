import set

class View:
    def __init__(self, ui_framework): #コンストラクタ
        self.uiFramework = ui_framework

    def showFormula(self,value):
        self.uiFramework.setDisplayFormula(value) #screen.pyのsetDisplayFormulaのtextにvalueを入れる
        
    def showButton(self,value):
        self.uiFramework.setButtonText(value) #screen.pyのsetButtonTextのtextにvalueを入れる
        
    def showValue(self,list):
        
        self.uiFramework.setDisplayInput(list) #screen.pyのtsetDisplayInputのtextにvalueを入れる