import matplotlib.pyplot as plt
import numpy as np


class Heart:
    def graph(self):
        t = np.arange(0, 2 * np.pi, 0.01)
        x = 16 * np.sin(t) ** 3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlim(-17, 17)
        ax.set_ylim(-20, 13)
        ax.plot(x, y, color='red')
        ax.set_aspect(1)

        plt.grid(True)

        plt.show()


def main():
    heart = Heart()
    heart.graph()


if __name__ == '__main__':
    main()
