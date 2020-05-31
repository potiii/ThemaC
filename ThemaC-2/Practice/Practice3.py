import cv2
from matplotlib import pyplot as plt


class Cat:
    pic_raw = "cat.jpg"
    pic = cv2.imread(pic_raw)

    def plot(self, pic):
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

    def cascade(self, pic):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
        faces = face_cascade.detectMultiScale(pic)

        for x, y, w, h in faces:
            cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), 2)


def main():
    cat = Cat()
    cat.plot(cat.pic)
    cat.cascade(cat.pic)
    cat.plot(cat.pic)


if __name__ == '__main__':
    main()
