# -*- coding: utf-8 -*-

class Model:
    def __init__(self, view): #コンストラクタ
        self.value = '4839'
        self.view = view #viewへの参照
        
    def setFormula(self): #式を入力
        self.view.showFormula(self.value) #viewへ通知
        
    def setButton(self): #式を入力
        self.view.showButton(self.value) #viewへ通知