import numpy as np
from graphing import * 

lof_file_name = "auux.txt"
log_file = open(lof_file_name, "w+")
log_file.close()


data_src = open("std_dev.txt", "r")
data = data_src.read()

data = data.split('Killing process:')[:-1]
for i in range(len(data)): 
    data[i] = data[i].split('---------------------------------')[:-1]
    for j in range(len(data[i])):
        data[i][j] = data[i][j].split('Number of bytes recieved per second:  ')[1].split('\n')[0]

std_dev = [None for i in range(len(data))]

for i in range(len(data)):
    data[i] = [float(el) for el in data[i]]

    std_dev[i] = np.std(data[i]) / 1024 ** 2


data_src = open("aux.txt", "r")
data = data_src.read()

first = [None for i in range(100)]
second = [None for i in range(100)]

data = data.split('\n')

for i in range(len(data)):
    data[i] = data[i].split(' ')

    first[i] = float(data[i][0])
    second[i] = float(data[i][1])

# plot_graph3([i for i in range(1, len(std_dev) + 1)], std_dev)
for i in range(len(std_dev)):
    log_file = open(lof_file_name, "a")
    log_file.write("%d %.3f %.3f\n" % (first[i], second[i], std_dev[i]))
    log_file.close()
