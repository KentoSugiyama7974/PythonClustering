from get_data import DataCalculation
from clustring import Cluster
from plot_cluster_data import PlotCluster
from myfft import myfft

import numpy as np

def main():
    path = "c:/Users/ymtlab/Documents/20211214/1/"
    data = np.array([])

    data_calculation = DataCalculation(path)
    norm = data_calculation.get_2dim_norm()

    for name in "ABCDEFGHIJ":
        data = np.append(data, norm[name])

    data = data.reshape(-1,60)
    fft_data = myfft(data)

    clustring = Cluster(fft_data)
    clustring.k_means(cluster=4)
    label = clustring.get_label()

    data = data.reshape(10,-1,60)
    label = label.reshape(10,-1)

    for i in range(len(label)):
        plot_cluster = PlotCluster(data[i], label[i])
        plot_cluster.plot_show()

if __name__ == "__main__":
    main()