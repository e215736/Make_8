
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import random

# Label日本語対応のためfont追加
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')

from model import Model
from view import View
from controller import Controller


class TitleScreen(Screen):
    pass


class Question:
    # 問題
    questions = [
        [1,2,3,8,"3+1+8÷2"],[3,4,5,6,"3+4+6-5"],
        [2,3,4,8,"4×3-8÷2"],[1,2,4,7,"7+4-2-1"],
        [1,9,9,9,"9×9÷9-1"],[1,3,4,6,"6×4÷3÷1"]
        ]

    q_num = [1,2,3,4,5,6]

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = View(self)
        model = Model(view)
        self.controller = Controller(model)    
        
    def setDisplayFormula(self,text): #問題を画面（問題欄）に表示
        self.ids.label1.text = text
        
    def setButtonText(self,text): #問題の式をボタンに表示
        b1 = text[0]
        b2 = text[1]
        b3 = text[2]
        b4 = text[3]
        self.ids.button1.text = b1
        self.ids.button2.text = b2
        self.ids.button3.text = b3
        self.ids.button4.text = b4
        
    def onPress(self): #ボタンが押された際にそのボタンのtextを画面（回答欄）に表示
        value = self.ids.button1.text
        self.ids.label2.text += value
        
        

class WrongAnsScreen(Screen):
    pass

class RetireScreen(Screen):
    pass

class CorrectScreen(Screen):
    pass



class App(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(TitleScreen(name='title'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(WrongAnsScreen(name='wrong'))
        self.sm.add_widget(RetireScreen(name='retire'))
        self.sm.add_widget(CorrectScreen(name='correct'))
        return self.sm

if __name__ == '__main__':
    App().run()