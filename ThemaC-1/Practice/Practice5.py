import numpy as np
import matplotlib.pyplot as plt
import csv
import psutil
import time


class Memory:
    filename = 'memory_used.csv'

    def mem_write(self):
        mem_list = []
        for i in range(18):
            mem_list.append(round((psutil.virtual_memory().used / (1024.0 ** 3)), 2))
            time.sleep(1)
        with open(self.filename, 'w', encoding='utf-8') as fi:
            w = csv.writer(fi)
            w.writerow(mem_list)

    def mem_read(self):
        return np.loadtxt(self.filename, delimiter=',')

    def graph_plot(self):
        x = np.arange(0, 180, 10)
        y = self.mem_read()

        plt.plot(x, y, color='red', marker='o')

        plt.xticks(x)
        plt.title('My PC Memory Used.')
        plt.xlabel('seconds')
        plt.ylabel('Used/GB')
        plt.grid(True)
        plt.show()


def main():
    memory = Memory()
    try:
        memory.mem_write()
        memory.graph_plot()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
