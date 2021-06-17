import matplotlib.pyplot as plt
import numpy as np

class DataPlot:
    def __init__(self):
        self.color = ["k","b","g","r","purple","gold","teal"]

    def sonogram_plot(self,fft_data,samplerate=256):
        fig = plt.figure()
        fft_data = np.array(fft_data).T
        ax = fig.add_subplot(1,1,1)
        image = ax.imshow(fft_data,vmin=-2,vmax=9,extent=[0,4*len(fft_data),0,samplerate],aspect='auto',cmap='viridis')
        cbar = fig.colorbar(image)

        ax.set_xticks(np.arange(0,1000,50))
        ax.set_yticks(np.arange(0,1000,20))
        ax.set_xlim(0,samplerate*2)
        ax.set_ylim(0,samplerate)

    def nomal_plot(self,data,title="no name"):
        fig = plt.figure(figsize=(15,4))
        plt.title(title)
        ax = fig.add_subplot(1,1,1)
        ax.plot(range(len(data)),data)

    def cluster_plot(self,features,label):
        fig = plt.figure(figsize=(15,4))
        ax = fig.add_subplot(1,1,1)
        for index,data in enumerate(features):
            ax = plt.plot(range((index-1)*len(data),(index)*len(data)),data,color=self.color[label[index]])

    def show(self):
        plt.show()