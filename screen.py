from kivy.app import App

#「ScreenManager()」は実装直後には一つの画面しか所持していません
#そのため、別の画面への遷移したいときには「ScreenManager()」に対して「Screen()」を追加します
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget

from kivy.properties import StringProperty

input_formula = []


class TitleScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self,num):
        self.text = "a"
        input_formula.append(num)
        self.ids.formula.text = "input_formula"

class WrongAnsScreen(Screen):
    pass

class RetireScreen(Screen):
    pass

class CorrectScreen(Screen):
    pass



class ScreenApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(TitleScreen(name='title'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(WrongAnsScreen(name='wrong'))
        self.sm.add_widget(RetireScreen(name='retire'))
        self.sm.add_widget(CorrectScreen(name='correct'))
        return self.sm


class Fromula():
    pass


if __name__ == '__main__':
    ScreenApp().run()