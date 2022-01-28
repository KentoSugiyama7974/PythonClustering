import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class PlotCluster():
    def __init__(self,data,label):
        self.data = data
        self.label = label
        self.color = sns.color_palette(n_colors=len(np.unique(label)))

    def plot_show(self):
        _, l = self.data.shape
        for i in range(len(self.label)):
            plt.plot(range(i*l,(i+1)*l),self.data[i],color=self.color[self.label[i]])
        plt.show()