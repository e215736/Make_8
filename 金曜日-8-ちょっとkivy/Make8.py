from cgi import print_directory
from curses import keyname
from tty import setcbreak
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
# --------------------------------------------------
# Label日本語対応のためfont追加
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')
# --------------------------------------------------
from model import Model
from view import View
from controller import Controller
import set


class Title(Screen):
    def onClick(self,scene):
        Controller.onClick(scene)


class Playing(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = View(self)
        model = Model(view)
        self.controller = Controller(model)
    
    def setDisplayFormula(self,text): #問題を画面（問題欄）に表示
        self.ids.question.text = text

    def setButtonText(self,value):
        self.ids.btn1.text = str(value[1])
        self.ids.btn2.text = str(value[2])
        self.ids.btn3.text = str(value[3])
        self.ids.btn4.text = str(value[4])

    def setDisplayInput(self,list):
        self.ids.formula.text = str("".join(list))
    
    def onClick(self,scene):
        Controller.onClick(scene)
    
    def onBtn(self,key):
        self.controller.onBtn(key)

class Correct(Screen):
    def goNext(self):
        set.ans += 1
        Model.setFormula()

class Retire(Screen):
    def onClick(self,scene):
        Controller.onClick(scene)


class Make8App(App):
    def __init__(self, **kwargs):
        super(Make8App, self).__init__(**kwargs)
        self.title = 'Make8'
        set.init()

    def build(self):
        # ScreenManagerの設定
        set.sm.add_widget(Title(name='title'))
        set.sm.add_widget(Playing(name='playing'))
        set.sm.add_widget(Correct(name='correct'))
        set.sm.add_widget(Retire(name='retire'))
        return set.sm

if __name__ == '__main__':
    Make8App().run()