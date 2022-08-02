# -*- coding: utf-8 -*-

class Model:
    def __init__(self, view): #コンストラクタ
        self.view = view #viewへの参照
        
    def setFormula(self):
        self.view.showFormula('1241') #viewへ通知
    
    

         