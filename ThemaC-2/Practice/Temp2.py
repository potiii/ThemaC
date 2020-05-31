import cv2
from matplotlib import pyplot as plt


class Cat:
    pic_raw = 'cat2.jpg'
    pic = cv2.imread(pic_raw)

    def pic_show(self, pic):
        plt.title('Cat Image')
        plt.imshow(cv2.cvtColor(pic, cv2.COLOR_BGR2RGB))
        plt.tick_params(labelbottom=False,
                        labelleft=False,
                        labelright=False,
                        labeltop=False,
                        bottom=False,
                        left=False,
                        right=False,
                        top=False)
        plt.show()

    def detect(self, pic):
        cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
        faces = cascade.detectMultiScale(pic)

        for x, y, w, h in faces:
            cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return faces

    def detect_plot(self, pic):
        detect = self.detect(pic)
        self.pic_show(detect)

def main():
    cat = Cat()
    cat.detect_plot(cat.pic)

if __name__ == '__main__':
    main()
