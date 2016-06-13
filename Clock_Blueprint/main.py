import sys
try:
    import paho.mqtt.client as mqtt
except ImportError:
    import os
    import inspect
    cmd_subflolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe()))[0], "../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

import subprocess
import thread
mqtt_content = "Loading"






def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))


def on_message(mqttc, obj, msg):
    global mqtt_content
    mqtt_content= str(msg.payload)
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


def on_publish(mqttc, obj, msg):
    print("mid: "+str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect("www.znh.tw", 1883, 60)
mqttc.subscribe("/inTopic", 0)


def get_mqtt():
    mqttc.loop_forever()


from time import strftime


class ClockApp(App):
    global mqtt_content
    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0.0016)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(minutes), int(seconds), int(seconds * 100 % 100)))
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        self.root.ids.mqtt_text.text = mqtt_content
        if mqtt_content == "RED":
            self.root.ids.mqtt_text.color = (1, 0, 0, 1)
        elif mqtt_content == "GREEN":
            self.root.ids.mqtt_text.color = (0, 1, 0, 1)
        elif mqtt_content == "BLUE":
            self.root.ids.mqtt_text.color = (0, 0, 1, 1)
        else:
            self.root.ids.mqtt_text.color = (1, 1, 1, 1)


    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0



class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    thread.start_new_thread(get_mqtt,())
    ClockApp().run()