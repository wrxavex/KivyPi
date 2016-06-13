from time import sleep, asctime, localtime
from kivy.lib import osc
from kivy.clock import Clock


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

serviceport = 8999
activityport = 9999


class Info:
    def __init__(self, info, text, count):
        self.info = info
        self.text = text
        self.count = count


class Controller(FloatLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.info = 'press'+str(my_info.count)

        my_info.count += 1
        print('button press')
        osc.sendMsg('/print/x', dataArray=['/print/pd''sen2d'], ipAddr='192.168.1.139', port=activityport)
        osc.sendMsg('/print/pd', dataArray=['sen2d', my_info.count], ipAddr='192.168.1.141', port=serviceport)
        osc.sendMsg('/print/pd', dataArray=['sen2d', my_info.count], ipAddr='192.168.1.139', port=serviceport)
        print('osc send')


class ControllerApp(App):

    def on_start(self):
        pass
        Clock.schedule_interval(self.update, 0)

    def build(self):
        return Controller(info='Hello')

    def update(self, nap):
        self.root.ids.my_custom_label.text = my_info.info
        # print('update info')


def some_api_callback(message, *args):
    print("got a message! %s" % message)

    # answer_message()
    my_info.info = str(message)
    # print('answer message')


# def answer_message():
   # osc.sendMsg('/print/x', [asctime(localtime()), ],ipAddr='127.0.0.1', port=serviceport)


if __name__ == '__main__':
    osc.init()
    oscid = osc.listen(ipAddr='0.0.0.0', port=serviceport)
    osc.bind(oscid, some_api_callback, '/print/pd')

    my_info = Info('myinfooo', 'mytexxxt', 0)

    Clock.schedule_interval(lambda *x: osc.readQueue(oscid), 0)

    ControllerApp().run()
