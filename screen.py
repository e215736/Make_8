from kivy.app import App

#「ScreenManager()」は実装直後には一つの画面しか所持していません
#そのため、別の画面への遷移したいときには「ScreenManager()」に対して「Screen()」を追加します
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget

from kivy.properties import StringProperty

####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで

class TitleScreen(Screen):
    pass


class MainScreen(Screen):
    pass

class WrongAnsScreen(Screen):
    pass

class RetireScreen(Screen):
    pass

class CorrectScreen(Screen):
    pass

class AllCorrectScreen(Screen):
    pass

class ScreenApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(TitleScreen(name='title'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(WrongAnsScreen(name='wrong'))
        self.sm.add_widget(RetireScreen(name='retire'))
        self.sm.add_widget(CorrectScreen(name='correct'))
        self.sm.add_widget(AllCorrectScreen(name='all'))
        return self.sm


if __name__ == '__main__':
    ScreenApp().run()