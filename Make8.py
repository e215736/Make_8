from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.properties import StringProperty

# Label日本語対応のためfont追加
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')

class Title(Screen):
    pass

class Playing(Screen):
    text = StringProperty('')

    def __init__(self, **kwargs):
        super(Playing, self).__init__(**kwargs)
        self.text = 'No Text'
    
    def onButtonClick(self):
        self.text = self.ids.textInput.text

class Make8App(App):
    def __init__(self, **kwargs):
        super(Make8App, self).__init__(**kwargs)
        self.title = 'kivytest'

    def build(self):
        # ScreenManagerの設定
        self.sm = ScreenManager(transition=RiseInTransition())
        self.sm.add_widget(Title(name='title'))
        self.sm.add_widget(Playing(name='playing'))
        return self.sm

if __name__ == '__main__':
    Make8App().run()