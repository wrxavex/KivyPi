from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lib import osc
import subprocess
import set_id
from kivy.clock import Clock
import random

my_id = set_id.IDSetter()
print(my_id.my_movie)

serviceport = 8999
activityport = 9999


class DerrickWidget(Widget):
    pass


def stop_all():

    if a1.is_available == 1:
        a1.is_available = 0
        a1.proc.stdin.write('q')
        print ('a1 stop')
    if a2.is_available == 1:
        a2.is_available = 0
        a2.proc.stdin.write('q')
        print ('a2 stop')
    if a3.is_available == 1:
        a3.is_available = 0
        a3.proc.stdin.write('q')
        print ('a3 stop')


def play_random_audio():
    random_number = random.randint(1, 3)
    print ('random number is %d' % random_number)
    if random_number == 1:
        if a1.is_available == 0:
            a1.is_available = 1
            print ('playing audio 1')
            a1.audio_play()
    elif random_number == 2:
        if a2.is_available == 0:
            a2.is_available = 1
            print ('playing audio 2')
            a2.audio_play()
    elif random_number == 3:
        if a3.is_available == 0:
            a3.is_available = 1
            print ('playing audio 3')
            a3.audio_play()
    else:
        print ('what is wrong')


class DerrickApp(App):
    def build(self):
        return DerrickWidget()


class OmxAudioPlayer:
    AudioCount = 0

    def __init__(self, name):
        self.name = name
        self.is_playing = 0
        self.is_available = 0
        self.proc = 0
        OmxAudioPlayer.AudioCount += 1

    def audio_play(self):
        self.proc = subprocess.Popen(['omxplayer', '-o', 'local', '--loop', '--no-osd', self.name],
                                     stdin=subprocess.PIPE)

    @staticmethod
    def audio_count():
        print (OmxAudioPlayer.AudioCount)

    def kill_audio(self):
        if self.is_playing == 1:
            self.is_playing = 0
            self.proc.stdin.write('q')

a1 = OmxAudioPlayer("/home/pi/newTaipei/no1.wav")
a2 = OmxAudioPlayer("/home/pi/newTaipei/no2.wav")
a3 = OmxAudioPlayer("/home/pi/newTaipei/no3.wav")


def derrick_osc(message, *args):

    print('got message', message[2])
    stop_all()
    play_random_audio()


if __name__ == '__main__':
    osc.init()
    oscid = osc.listen(ipAddr='0.0.0.0', port=activityport)
    osc.bind(oscid, derrick_osc, '/derrick/osc')

    Clock.schedule_interval(lambda *x: osc.readQueue(oscid), 0)
    print (my_id.id_to_set, 'id_to_set')
    play_random_audio()
    DerrickApp().run()