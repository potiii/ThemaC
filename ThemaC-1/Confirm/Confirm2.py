import numpy as np
import matplotlib.pyplot as plt


class Confirm:
    def graph(self):
        x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
        y = np.sin(x) - 2 * np.cos(x)
        plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
                   ['-2π', '-π', '0', 'π', '2π'])
        plt.gca().set_aspect('equal')
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y', rotation=0)
        plt.stem(x, y)
        plt.show()


def main():
    confirm = Confirm()
    confirm.graph()


if __name__ == '__main__':
    main()
