from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition

def init():
    global sm
    sm = ScreenManager(transition=RiseInTransition())

    global q_num
    q_num = [1,2,3,4,5,6]

    global questions
    questions = [
        ["1238",1,2,3,8,"3+1+8÷2"],["3456",3,4,5,6,"3+4+6-5"],
        ["2348",2,3,4,8,"4×3-8÷2"],["1247",1,2,4,7,"7+4-2-1"],
        ["1999",1,9,9,9,"9×9÷9-1"],["1346",1,3,4,6,"6×4÷3÷1"]
        ]
    global ans
    ans = 0