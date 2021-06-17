from LoadFile import LoadFile
from MyFFT import MyFFT
from Cluster import Cluster
from DataPlot import DataPlot
import json

files = LoadFile([])
files.input_split_file("C:/Users/ymtlab/Documents/20200910_move/spl_pass")
data = files.get_data()
pass_norm_data = [row["norm"] for row in data]

files.input_split_file("C:/Users/ymtlab/Documents/20200910_move/spl_walk")
data = files.get_data()
walk_norm_data = [row["norm"] for row in data]

files.input_split_file("C:/Users/ymtlab/Documents/20200910_move/spl_stand")
data = files.get_data()
stand_norm_data = [row["norm"] for row in data]

norm_data = pass_norm_data + walk_norm_data + stand_norm_data

myfft = MyFFT()
myfft.fft(norm_data)
fft_data = myfft.get_fft_data()

a = [2 for i in range(16)]
b = [1 for i in range(16)]
c = [0 for i in range(16)]
label = a+b+c
output = dict()

output['fft_data'] = fft_data
output['label_data'] = label

with open("C:/Users/ymtlab/Documents/20200910_move/data_set/data.txt",'w') as f:
    f.write(json.dumps(output))