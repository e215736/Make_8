from tty import setcbreak
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition

# Label日本語対応のためfont追加
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')

from model import Model
from view import View
from controller import Controller

#スクリーンマネージャ
sm = ScreenManager(transition=RiseInTransition())

class Title(Screen):
    pass

class Playing(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        view = View(self)
        model = Model(view)
        self.controller = Controller(model)
    
    def onClick(self,scene):
        sm.current = 'title'
        #self.controller.onClick(scene)

class Correct(Screen):
    pass

class Retire(Screen):
    pass


class Make8App(App):
    def __init__(self, **kwargs):
        super(Make8App, self).__init__(**kwargs)
        self.title = 'Make8'

    def build(self):
        # ScreenManagerの設定

        sm.add_widget(Title(name='title'))
        sm.add_widget(Playing(name='playing'))
        sm.add_widget(Correct(name='correct'))
        sm.add_widget(Retire(name='retire'))
        return sm

if __name__ == '__main__':
    Make8App().run()