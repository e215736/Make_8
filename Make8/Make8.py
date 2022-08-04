from kivy.app import App
from kivy.uix.screenmanager import Screen
from model import Model
from view import View
from controller import Controller
import set
# --------------------------------------------------
# Label日本語対応のためfont追加
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')


# --------------------------------------------------
# 各シーン用クラス
class Title(Screen):
    pass
class Playing(Screen):
    pass    
class Correct(Screen):
    pass
class AllCorrect(Screen):
    pass
class Retire(Screen):
    pass


# --------------------------------------------------
# Appクラス
class Make8App(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Make8'
        set.init()
        view = View(self)
        model = Model(view)
        self.controller = Controller(model)

    def build(self):
        # ScreenManagerの設定
        set.sm.add_widget(Title(name='title'))
        set.sm.add_widget(Playing(name='playing'))
        set.sm.add_widget(Correct(name='correct'))
        set.sm.add_widget(AllCorrect(name='allcorrect'))
        set.sm.add_widget(Retire(name='retire'))
        return set.sm
    
    def onClick(self,scene):
        self.controller.onClick(scene)
    
    def onBtn(self,key):
        self.controller.onBtn(key)
    


if __name__ == '__main__':
    Make8App().run()