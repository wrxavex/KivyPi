from kivy.uix.scatter import Scatter
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivy.clock import Clock

import time
import os

os.environ['TZ'] = 'Asia/Taipei'
time.tzset()

mytext = "My Text"
time_now = "time"





class TestAPP(App):
    def build(self):
        time_now = time.strftime('%X')
        f = FloatLayout()
        s = Scatter()
        l = Label(text=time_now,
                  font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f



if __name__ == "__main__":
    Clock.schedule_interval(TestAPP, 1/60.)
    TestAPP().run()
