# %%
import numpy as np
import matplotlib.pyplot as plt
import psutil
import time
import json


class Pcstats:
    filename = 'memory_cpu_used.json'
    keyA = 'memory'
    keyB = 'cpu'

    def stats_write(self):
        data = {}
        for i in range(18):
            data.setdefault(i, {})
            data[i].setdefault(self.keyA, round((psutil.virtual_memory().used / (1024.0 ** 3)), 2))
            data[i].setdefault(self.keyB, psutil.cpu_percent(interval=1))
            time.sleep(1)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def stats_read(self):
        with open(self.filename) as f:
            return json.load(f)

    def dict_to_mem_list(self):
        return [self.stats_read()[str(i)][self.keyA] for i in range(len(self.stats_read()))]

    def dict_to_cpu_list(self):
        return [self.stats_read()[str(i)][self.keyB] for i in range(len(self.stats_read()))]

    def graph_plot(self):
        mem_list = self.dict_to_mem_list()
        cpu_list = self.dict_to_cpu_list()

        x = np.arange(0, 180, 10)

        fig = plt.figure()
        ax1 = fig.add_subplot()
        ax1.plot(x, mem_list, color='red', marker='o')
        ax2 = ax1.twinx()
        ax2.plot(x, cpu_list, color='blue', marker='o')
        plt.xticks(np.arange(0, 180, 10))
        plt.title('My PC Used.')
        plt.xlabel('seconds')
        ax1.set_ylabel('Memory/GB')
        ax2.set_ylabel('CPU/Percent')
        plt.grid(True)
        plt.show()


def main():
    pcstats = Pcstats()
    #pcstats.stats_write()
    pcstats.graph_plot()


if __name__ == '__main__':
    main()
