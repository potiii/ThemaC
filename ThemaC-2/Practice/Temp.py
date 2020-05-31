import cv2
from matplotlib import pyplot as plt

def plot(pic):
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

pic_raw = "cat.jpg"
pict = cv2.imread(pic_raw)


plot(pict)

def cascade(pic):

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    faces = face_cascade.detectMultiScale(pic)

    for x, y, w, h in faces:
        cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), 2)
cascade(pict)
plot(pict)

