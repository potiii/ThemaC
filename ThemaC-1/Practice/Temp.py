# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import psutil
import time
import json

class Pcused:
    filename = 'memory_cpu_used.json'

    def data_write(self):
        data = {}
        keyA = 'memory'
        keyB = 'cpu'
        for i in range(18):
            data.setdefault(i, {})
            data[i].setdefault(keyA, round((psutil.virtual_memory().used / (1024.0 ** 3)), 2))
            data[i].setdefault(keyB, psutil.cpu_percent(interval=1))
            time.sleep(0)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def data_read(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return pd.read_json(self.filename)