
from unicodedata import name
from kivy.app import App


#「ScreenManager()」は実装直後には一つの画面しか所持していません
#そのため、別の画面への遷移したいときには「ScreenManager()」に対して「Screen()」を追加します
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from model import Model
from view import View
from controller import Controller

class TitleScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = View(self)
        model = Model(view)
        self.controller = Controller(model)    
        
    def setDisplayFormula(self,text): #問題を画面（問題欄）に表示
        self.ids.label1.text = text
          
    def onPress(self): #ボタンが押された際にそのボタンのtextを画面（回答欄）に表示
        value = self.ids.button1.text
        self.ids.label2.text += value
        
        

class WrongAnsScreen(Screen):
    pass

class RetireScreen(Screen):
    pass

class CorrectScreen(Screen):
    pass



class ScreenApp(App):
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
    ScreenApp().run()