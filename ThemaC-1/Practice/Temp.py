
import psutil
import time
list = []
for i in range(20):
    list.append(round((psutil.virtual_memory().used / (1024.0 ** 3)), 2))
    time.sleep(0)

list2 = [round((psutil.virtual_memory().used / (1024.0 ** 3)), 2) or time.sleep(1) for i in range(20)]

print(list)
print(list2)
