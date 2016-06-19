from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lib import osc
import subprocess
import set_id
from kivy.clock import Clock
from time import sleep
import random
import thread

my_id = set_id.id_setter()
print(my_id.my_movie)

serviceport = 8999
activityport = 9999


def osc_all_play_yourself(dt):
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.189', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.190', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.191', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.192', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.198', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.199', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.200', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.188', port=serviceport)
    osc.sendMsg('/derrick/osc', dataArray=[0], ipAddr='192.168.1.159', port=serviceport)


class DerrickWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            if my_id.locked == 0:
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.189', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.190', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.191', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.192', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.198', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.199', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.200', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.188', port=serviceport)
                osc.sendMsg('/derrick/osc', dataArray=[my_id.id_to_set], ipAddr='192.168.1.159', port=serviceport)


def stopFS():
    if v1fs.is_available == 1:
        stopVideo(v1fs)
        playAll()
    if v2fs.is_available == 1:
        stopVideo(v2fs)
        playAll()
    if v3fs.is_available == 1:
        stopVideo(v3fs)
        playAll()
    if v4fs.is_available == 1:
        stopVideo(v4fs)
        playAll()


def stopall():

    print ('stop all: \n')

    if f1.is_available == 1:
        f1.proc.stdin.write('q')
        f1.is_available = 0
        print ('f1 stop')
    if f2.is_available == 1:
        f2.proc.stdin.write('q')
        f2.is_available = 0
        print ('f2 stop')
    if f3.is_available == 1:
        f3.proc.stdin.write('q')
        f3.is_available = 0
        print ('f3 stop')
    if f4.is_available == 1:
        f4.proc.stdin.write('q')
        f4.is_available = 0
        print ('f4 stop')
    if f5.is_available == 1:
        f5.proc.stdin.write('q')
        f5.is_available = 0
        print ('f5 stop')
    if f6.is_available == 1:
        f6.proc.stdin.write('q')
        f6.is_available = 0
        print ('f6 stop')
    if f7.is_available == 1:
        f7.proc.stdin.write('q')
        f7.is_available = 0
        print ('f7 stop')
    if f8.is_available == 1:
        f8.proc.stdin.write('q')
        f8.is_available = 0
        print ('f8 stop')
    if f9.is_available == 1:
        f9.proc.stdin.write('q')
        f9.is_available = 0
        print ('f9 stop')

    if v1.is_available == 1:
        v1.is_available = 0
        v1.proc.stdin.write('q')
    if v2.is_available == 1:
        v2.is_available = 0
        v2.proc.stdin.write('q')
    if v3.is_available == 1:
        v3.is_available = 0
        v3.proc.stdin.write('q')
    if v4.is_available == 1:
        v4.is_available = 0
        v4.proc.stdin.write('q')

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

    if my_video.is_available == 1:
        my_video.is_available = 0
        my_video.proc.stdin.write('q')
        print ('my video stop')

    print ('f1 status is %d \n' % f1.is_available)
    print ('f2 status is %d \n' % f2.is_available)
    print ('f3 status is %d \n' % f3.is_available)
    print ('f4 status is %d \n' % f4.is_available)
    print ('f5 status is %d \n' % f5.is_available)
    print ('f6 status is %d \n' % f6.is_available)
    print ('f7 status is %d \n' % f7.is_available)
    print ('f8 status is %d \n' % f8.is_available)
    print ('f9 status is %d \n' % f9.is_available)

    print ('a1 status is %d \n' % a1.is_available)
    print ('a2 status is %d \n' % a2.is_available)
    print ('a3 status is %d \n' % a3.is_available)

    print ('MY video status is %d \n' % my_video.is_available)


def playAll():
    if v1.is_available == 0:
        v1.is_available = 1
        v1.videoPlay()
    if v2.is_available == 0:
        v2.is_available = 1
        v2.videoPlay()
    if v3.is_available == 0:
        v3.is_available = 1
        v3.videoPlay()
    if v4.is_available == 0:
        v4.is_available = 1
        v4.videoPlay()


def playone(omxvideo):
    if omxvideo.is_available == 0:
        omxvideo.is_available = 1
        omxvideo.videoPlay()


def play_one_v2(omxvideo, dt):
    if omxvideo.is_available == 0:
        omxvideo.is_available = 1
        omxvideo.videoPlay()


def play_random_audio(seed, dt):
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
        

def stopVideo(videoins):
    if videoins.is_available == 1:
        videoins.is_available = 0
        videoins.proc.stdin.write('q')


def croparea_setter(id):
    id = int(id)
    if id == 1:
        crop_area = "0,0,240,160"
        return crop_area
    if id == 2:
        crop_area = "240,0,480,160"
        return crop_area
    if id == 3:
        crop_area = "480,0,720,160"
        return crop_area
    if id == 4:
        crop_area = "0,160,240,320"
        return crop_area
    if id == 5:
        crop_area = "240,160,480,320"
        return crop_area
    if id == 6:
        crop_area = "480,160,720,320"
        return crop_area
    if id == 7:
        crop_area = "0,320,240,480"
        return crop_area
    if id == 8:
        crop_area = "240,320,480,480"
        return crop_area
    if id == 9:
        crop_area = "480,320,720,480"
        return crop_area


class DerrickApp(App):
    def build(self):
        return DerrickWidget()


class OmxVideoPlayer:
    VideoCount = 0

    def __init__(self, pos, crop, name):
        self.pos = pos
        self.name = name
        self.is_playing = 0
        self.is_available = 0
        self.proc = 0
        self.crop = crop
        OmxVideoPlayer.VideoCount += 1

    def videoPlay(self):
        self.proc = subprocess.Popen(['omxplayer','--no-osd', '--loop', '--win', self.pos, self.name, '--crop', self.crop], stdin=subprocess.PIPE)

    def videoCount(self):
        print (OmxVideoPlayer.VideoCount)

    def killvideo(self):
        if self.is_playing == 1:
            self.is_playing = 0
            self.proc.stdin.write('q')


class OmxAudioPlayer:
    AudioCount = 0

    def __init__(self, name):
        self.name = name
        self.is_playing = 0
        self.is_available = 0
        self.proc = 0
        OmxAudioPlayer.AudioCount += 1

    def audio_play(self):
        self.proc = subprocess.Popen(['omxplayer','-o', 'local', '--loop', '--no-osd', self.name], stdin=subprocess.PIPE)

    @staticmethod
    def audio_count():
        print (OmxVideoPlayer.AudioCount)

    def kill_audio(self):
        if self.is_playing == 1:
            self.is_playing = 0
            self.proc.stdin.write('q')

v1 = OmxVideoPlayer("0,0,400,240", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/1.mp4")
v2 = OmxVideoPlayer("400,0,800,240", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/2.mp4")
v3 = OmxVideoPlayer("0,240,400,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/3.mp4")
v4 = OmxVideoPlayer("400,240,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/4.mp4")


f1 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/1.mp4")
f2 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/2.mp4")
f3 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/3.mp4")
f4 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/4.mp4")
f5 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/5.mp4")
f6 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/6.mp4")
f7 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/7.mp4")
f8 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/8.mp4")
f9 = OmxVideoPlayer("0,0,800,480", croparea_setter(my_id.id_to_set), "/home/pi/newTaipei/9.mp4")

a1 = OmxAudioPlayer("/home/pi/newTaipei/no1.wav")
a2 = OmxAudioPlayer("/home/pi/newTaipei/no2.wav")
a3 = OmxAudioPlayer("/home/pi/newTaipei/no3.wav")


v1fs = OmxVideoPlayer("0,0,800,480", "0,0,720,480", "/home/pi/newTaipei/1.mp4")
v2fs = OmxVideoPlayer("0,0,800,480", "0,0,720,480", "/home/pi/newTaipei/2.mp4")
v3fs = OmxVideoPlayer("0,0,800,480", "0,0,720,480", "/home/pi/newTaipei/3.mp4")
v4fs = OmxVideoPlayer("0,0,800,480", "0,0,720,480", "/home/pi/newTaipei/4.mp4")

my_video = OmxVideoPlayer("0,0,800,480", "0,0,720,480", my_id.my_movie)


def derrick_osc(message, *args):
    print(my_id.locked, 'my id locked status 1 is locked')
    print ('f1 status is %d \n' % f1.is_available)
    print ('f1 proc is %s \n' % f1.proc)
    print ('f2 status is %d \n' % f2.is_available)
    print ('f3 status is %d \n' % f3.is_available)
    print ('f4 status is %d \n' % f4.is_available)
    print ('f5 status is %d \n' % f5.is_available)
    print ('f6 status is %d \n' % f6.is_available)
    print ('f7 status is %d \n' % f7.is_available)
    print ('f8 status is %d \n' % f8.is_available)
    print ('f9 status is %d \n' % f9.is_available)

    print ('a1 status is %d \n' % a1.is_available)
    print ('a2 status is %d \n' % a2.is_available)
    print ('a3 status is %d \n' % a3.is_available)

    print ('MY video status is %d \n' % my_video.is_available)
    print ('my video proc is %s \n' % my_video.proc)


    if int(message[2]) != int(my_id.id_to_set):
        print('random delay')

    else:
        if my_id.locked == 0:
            Clock.schedule_once(osc_all_play_yourself, 12)
            my_id.locked = 1
    print('got message', message[2])

    if int(message[2]) == 1:
        print ('id 1 touched')
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f1, ))
        print ('play f1')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f1 with audio')
    if int(message[2]) == 2:
        print ('id 2 touched')
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f2, ))
        print('play f2')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print('f2 with audio')

    if int(message[2]) == 3:
        print ('id 3 touched')
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f3, ))
        print ('play f3')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f3 with audio')

    if int(message[2]) == 4:
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        print ('id 4 video play before')
        thread.start_new_thread(playone, (f4, ))
        print ('id 4 after video')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('id 4 audio play')

    if int(message[2]) == 5:
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f5, ))
        print ('play f5')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f5 with audio')

    if int(message[2]) == 6:
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f6, ))
        print ('play f6')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f6 with auido')
    if int(message[2]) == 7:
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f7, ))
        print ('play f7')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f7 with audio')

    if int(message[2]) == 8:
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (f8, ))
        print ('play f8')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f8 with audio')

    if int(message[2]) == 9:
        my_id.locked = 1
        stopall()
        sleep(random.uniform(0,1))

        thread.start_new_thread(playone, (f9, ))
        print ('play f9')
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('f9 with audio')

    if int(message[2]) == 0:
        stopall()
        sleep(random.uniform(0,1))
        thread.start_new_thread(playone, (my_video, ))
        print ('play 0 my_video')
        print ('my_video status is %d \n' % my_video.is_available)
        thread.start_new_thread(play_random_audio, ("none", "null"))
        print ('Play random audio')
        my_id.locked = 0
        print ('unlock')



if __name__ == '__main__':
    
    osc.init()
    oscid = osc.listen(ipAddr='0.0.0.0', port=serviceport)
    osc.bind(oscid, derrick_osc, '/derrick/osc')

    Clock.schedule_interval(lambda *x: osc.readQueue(oscid), 0)
    print (my_id.id_to_set, 'id_to_set')
    print (croparea_setter(my_id.id_to_set))

    playone(my_video)

    DerrickApp().run()
