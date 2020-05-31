import cv2
import numpy as np
from matplotlib import pyplot as plt


class Picture:
    pic_raw = cv2.imread('lena.png')
    pic = np.array(pic_raw, dtype=np.uint8)
    rgb = cv2.COLOR_BGR2RGB
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    def pic_show(self, pic):
        plt.title('Lena Image')
        plt.imshow(cv2.cvtColor(pic, self.rgb))
        plt.tick_params(labelbottom=False,
                        labelleft=False,
                        labelright=False,
                        labeltop=False,
                        bottom=False,
                        left=False,
                        right=False,
                        top=False)
        plt.show()

    def mosaic(self, pic):
        small = cv2.resize(pic, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
        mosic = cv2.resize(small, pic.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
        return mosic

    def mosaic_area(self, pic, x, y, w, h):
        dist = pic.copy()
        dist[y:y + h, x:x + w] = self.mosaic(dist[y:y + h, x:x + w])
        return dist

    def pic_mosaic(self, pic):
        face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cas.detectMultiScale(self.gray)

        for x, y, w, h in faces:
            dist_face = self.mosaic_area(pic, x, y, w, h)
        return dist_face

    def detect_plot(self, pic):
        detect = self.pic_mosaic(pic)
        self.pic_show(detect)


def main():
    picture = Picture()
    picture.pic_show(picture.pic)
    picture.detect_plot(picture.pic)


if __name__ == '__main__':
    main()
