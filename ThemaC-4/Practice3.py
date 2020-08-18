import time

from datetime import datetime
from picamera import PiCamera


class Picture:
    def __init__(self):
        self.camera = PiCamera()

    def pic(self):
        now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.camera.preview()
        for i in range(18):
            self.camera.resolution = (320, 240)
            self.camera.image_effect = 'emboss'
            self.camera.annotate_text = now_time
            self.camera.capture('pic2/image{0}.jpg'.format(i))
            time.sleep(10)
        self.camera.stop_preview()


def main():
    picture = Picture()
    picture.pic()


if __name__ == '__main__':
    main()
