from time import sleep, asctime, localtime
from kivy.lib import osc
from kivy.clock import Clock


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

serviceport = 9998
activityport = 9999
newest_message = ''


class Info:
    def __init__(self, info, text):
        self.info = info
        self.text = text


class Controller(FloatLayout):
    label_wid = ObjectProperty()
    info = StringProperty()



    def do_action(self):
        self.label_wid.text = my_info.text
        self.info = my_info.info
        print('button press')
        osc.sendMsg('/print/x', [asctime(localtime()), ], ipAddr='192.168.1.141', port=activityport)




class ControllerApp(App):

    def on_start(self):
        Clock.schedule_interval(self.update, 5)

    def build(self):
        return Controller(info='Hello')

    def update(self, nap):
        self.root.ids.my_custom_label.text = asctime(localtime())
        # print('update info')



def some_api_callback(message, *args):
    print("got a message! %s" % message)
    answer_message()
    my_info.info = str(message)
    print('answer message')


def answer_message():
    osc.sendMsg('/print/x', [asctime(localtime()), ], port=activityport)



if __name__ == '__main__':
    osc.init()
    oscid = osc.listen(ipAddr='127.0.0.1', port=serviceport)
    osc.bind(oscid,some_api_callback, '/print/pd')

    my_info = Info('myinfooo', 'mytexxxt')

    Clock.schedule_interval(lambda *x: osc.readQueue(oscid), 0)

    ControllerApp().run()
