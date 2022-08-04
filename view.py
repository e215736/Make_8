class View:
    def __init__(self, ui_framework): #コンストラクタ
       self.uiFramework = ui_framework
       
    def showFormula(self,value):
        self.uiFramework.setDisplayFormula(value) #screen.pyのsetDisplayFormulaのtextにvalueを入れる
        
    def showButton(self,value):
        self.uiFramework.setButtonText(value) #screen.pyのsetButtonTextのtextにvalueを入れる
        
    def showValue(self,value):
        self.uiFramework.setDisplayInput(value) #screen.pyのtsetDisplayInputのtextにvalueを入れる
        
    
    