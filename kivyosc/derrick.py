from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lib import osc
import subprocess
import set_id

my_id = set_id.id_setter()
print(my_id.my_movie)

serviceport = 8999
activityport = 9999

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:

            print (my_id.my_movie+"touched")
            # if v1fs.is_available == 1:
            #     stopVideo(v1fs)
            #     playAll()
            #     return
            # if v2fs.is_available == 1:
            #     stopVideo(v2fs)
            #     playAll()
            #     return
            # if v3fs.is_available == 1:
            #     stopVideo(v3fs)
            #     playAll()
            #     return
            # if v4fs.is_available == 1:
            #     stopVideo(v4fs)
            #     playAll()
            #     return
            # 
            # if 0 < touch.x < 200 and 240 < touch.y < 480:
            #     if v1.is_available == 0:
            #         v1.is_available = 1
            #         v1.videoPlay()
            #         return
            #     stopVideo(v1)
            # 
            # if 200 < touch.x < 400 and 240 < touch.y < 480:
            #     if v1fs.is_available == 0:
            #         v1fs.is_available = 1
            #         stopAll()
            #         v1fs.videoPlay()
            #         return
            # 
            # if 400 < touch.x < 600 and 240 < touch.y < 480:
            #     if v2fs.is_available == 0:
            #         v2fs.is_available = 1
            #         stopAll()
            #         v2fs.videoPlay()
            #         return
            # 
            # if 600 < touch.x < 800 and 240 < touch.y < 480:
            #     if v2.is_available == 1:
            #         v2.is_available = 0
            #         v2.proc.stdin.write('q')
            #     else:
            #         v2.is_available = 1
            #         v2.videoPlay()
            # 
            # if 0 < touch.x < 200 and 0 < touch.y < 240:
            #     if v3.is_available == 1:
            #         v3.is_available = 0
            #         v3.proc.stdin.write('q')
            #     else:
            #         v3.is_available = 1
            #         v3.videoPlay()
            # 
            # if 200 < touch.x < 400 and 0 < touch.y < 240:
            #     if v3fs.is_available == 0:
            #         v3fs.is_available = 1
            #         stopAll()
            #         v3fs.videoPlay()
            #         return
            # 
            # if 400 < touch.x < 600 and 0 < touch.y < 240:
            #     if v4fs.is_available == 0:
            #         v4fs.is_available = 1
            #         stopAll()
            #         v4fs.videoPlay()
            #         return
            # 
            # if 600 < touch.x < 800 and 0 < touch.y < 240:
            #     if v4.is_available == 1:
            #         v4.is_available = 0
            #         v4.proc.stdin.write('q')
            #     else:
            #         v4.is_available = 1
            #         v4.videoPlay()


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


def stopAll():
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


def stopVideo(videoins):
    if videoins.is_available == 1:
        videoins.is_available = 0
        videoins.proc.stdin.write('q')


class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


class OmxVideoPlayer:
    VideoCount = 0

    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
        self.is_playing = 0
        self.is_available = 0
        self.proc = 0
        OmxVideoPlayer.VideoCount += 1

    def videoPlay(self):
        self.proc = subprocess.Popen(['omxplayer','--no-osd', '--loop', '--win', self.pos, self.name], stdin=subprocess.PIPE)

    def videoCount(self):
        print (OmxVideoPlayer.VideoCount)

    def killvideo(self):
        if self.is_playing == 1:
            self.is_playing = 0
            self.proc.stdin.write('q')


v1 = OmxVideoPlayer("0,0,400,240", "/home/pi/newTaipei/1.mp4")
v2 = OmxVideoPlayer("400,0,800,240", "/home/pi/newTaipei/2.mp4")
v3 = OmxVideoPlayer("0,240,400,480", "/home/pi/newTaipei/3.mp4")
v4 = OmxVideoPlayer("400,240,800,480", "/home/pi/newTaipei/4.mp4")
v1fs = OmxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/1.mp4")
v2fs = OmxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/2.mp4")
v3fs = OmxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/3.mp4")
v4fs = OmxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/4.mp4")

my_video = OmxVideoPlayer("0,0,800,480", my_id.my_movie)


def derrick_osc(message, *args):
    print("got a message! %s" % message)

    # answer_message()
    print(str(message))
    # print('answer message')

if __name__ == '__main__':
    
    osc.init()
    oscid = osc.listen(ipAddr='0.0.0.0', port=serviceport)
    osc.bind(oscid, derrick_osc, '/derrick/osc')

    playone(my_video)

    MyPaintApp().run()
