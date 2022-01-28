from sklearn.cluster import KMeans

import numpy as np

class Cluster():
    def __init__(self, data):
        self.data = data

    def k_means(self,cluster=4):
        model = KMeans(n_clusters=cluster).fit(self.data)
        self.labels = model.labels_
        self.label_sort(cluster)

    def label_sort(self,cluster):
        label_dict = dict()
        for i in range(cluster):
            label_dict[i] = np.ndarray([])

        for i in range(len(self.labels)):
            label_dict[self.labels[i]] = np.append(label_dict[self.labels[i]], self.data[i])
        
        for i in label_dict.keys():
            label_dict[i] = label_dict[i].mean()

        for i,(key,value) in enumerate(sorted(label_dict.items(), key= lambda x:x[1])):
            label_dict[key] = i

        self.labels = np.array([label_dict[i] for i in self.labels])


    def get_label(self):
        return self.labels