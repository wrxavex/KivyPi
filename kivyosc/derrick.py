from kivy.app import App
from kivy.uix.widget import Widget
import subprocess
import set_id


myid = set_id.id_setter()
print(myid.id_to_set)

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:

            if v1fs.is_available == 1:
                stopVideo(v1fs)
                playAll()
                return
            if v2fs.is_available == 1:
                stopVideo(v2fs)
                playAll()
                return
            if v3fs.is_available == 1:
                stopVideo(v3fs)
                playAll()
                return
            if v4fs.is_available == 1:
                stopVideo(v4fs)
                playAll()
                return

            if 0 < touch.x < 200 and 240 < touch.y < 480:
                if v1.is_available == 0:
                    v1.is_available = 1
                    v1.videoPlay()
                    return
                stopVideo(v1)

            if 200 < touch.x < 400 and 240 < touch.y < 480:
                if v1fs.is_available == 0:
                    v1fs.is_available = 1
                    stopAll()
                    v1fs.videoPlay()
                    return

            if 400 < touch.x < 600 and 240 < touch.y < 480:
                if v2fs.is_available == 0:
                    v2fs.is_available = 1
                    stopAll()
                    v2fs.videoPlay()
                    return

            if 600 < touch.x < 800 and 240 < touch.y < 480:
                if v2.is_available == 1:
                    v2.is_available = 0
                    v2.proc.stdin.write('q')
                else:
                    v2.is_available = 1
                    v2.videoPlay()

            if 0 < touch.x < 200 and 0 < touch.y < 240:
                if v3.is_available == 1:
                    v3.is_available = 0
                    v3.proc.stdin.write('q')
                else:
                    v3.is_available = 1
                    v3.videoPlay()

            if 200 < touch.x < 400 and 0 < touch.y < 240:
                if v3fs.is_available == 0:
                    v3fs.is_available = 1
                    stopAll()
                    v3fs.videoPlay()
                    return

            if 400 < touch.x < 600 and 0 < touch.y < 240:
                if v4fs.is_available == 0:
                    v4fs.is_available = 1
                    stopAll()
                    v4fs.videoPlay()
                    return

            if 600 < touch.x < 800 and 0 < touch.y < 240:
                if v4.is_available == 1:
                    v4.is_available = 0
                    v4.proc.stdin.write('q')
                else:
                    v4.is_available = 1
                    v4.videoPlay()


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


def stopVideo(videoins):
    if videoins.is_available == 1:
        videoins.is_available = 0
        videoins.proc.stdin.write('q')


class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


class omxVideoPlayer:
    VideoCount = 0

    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
        self.is_playing = 0
        self.is_available = 0
        self.proc = 0
        omxVideoPlayer.VideoCount += 1

    def videoPlay(self):
        self.proc = subprocess.Popen(['omxplayer', '--loop', '--win', self.pos, self.name], stdin=subprocess.PIPE)

    def videoCount(self):
        print (omxVideoPlayer.VideoCount)

    def killvideo(self):
        if self.is_playing == 1:
            self.is_playing = 0
            self.proc.stdin.write('q')


v1 = omxVideoPlayer("0,0,400,240", "/home/pi/newTaipei/1.mp4")
v2 = omxVideoPlayer("400,0,800,240", "/home/pi/newTaipei/2.mp4")
v3 = omxVideoPlayer("0,240,400,480", "/home/pi/newTaipei/3.mp4")
v4 = omxVideoPlayer("400,240,800,480", "/home/pi/newTaipei/4.mp4")
v1fs = omxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/1.mp4")
v2fs = omxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/2.mp4")
v3fs = omxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/3.mp4")
v4fs = omxVideoPlayer("0,0,800,480", "/home/pi/newTaipei/4.mp4")

if __name__ == '__main__':

    playAll()

    MyPaintApp().run()
