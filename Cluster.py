from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

class Cluster:
    def __init__(self):
        self.features = []
        self.y_agg = []
        self.inertia = None
        self.palette = None

    def fix(self,data,index,plus):
        for row in data:
            while len(row) != index:
                if len(row) < index:
                    row += [plus]
                elif len(row) > index:
                    del row[:len(row)-index]
        return data

    def set_data(self,data):
        data = self.fix(data,len(data[0]),0)
        self.features = np.array(data)
    
    def k_means(self,cluster=9):
        model = KMeans(n_clusters=cluster).fit(self.features)
        self.y_agg = model.labels_
        self.inertia = model.inertia_
        self.palette = sns.color_palette(n_colors=cluster)

    def plot(self):
        i = 0
        for index,data in enumerate(self.features):
            ax = plt.plot(range(i,i+len(data)),data,color=self.palette[self.y_agg[index]])
            i += len(data)
        plt.show()
    
    def get_items(self):
        return self.features.tolist(),self.y_agg.tolist()

    def elbow(self,max_chack=20):
        distortions = []
        for cluster in range(1,max_chack):
            self.k_means(cluster)
            distortions.append(self.inertia)
        plt.plot(range(1,max_chack),distortions,marker='o')
        plt.xlabel("Number of clusters")
        plt.ylabel('Distortion')
        plt.show()

    def sort_labels(self):
        sort = {}
        cnt = {}
        for index,label in enumerate(self.y_agg):
            if label not in sort.keys():
                sort[label] = self.features[index]
                cnt[label] = 1
            else:
                sort[label] += self.features[index]
                cnt[label] += 1
        avg = sorted([sum(value)/cnt[key] for key,value in sort.items()])
        for key,value in sort.items():
            sort[key] = avg.index(sum(value)/cnt[key])
        self.y_agg = np.array([sort[row] for row in self.y_agg])


class GAP:
    def __init__(self):
        self.L = Cluster()
        self.Ld = Cluster()
        self.G = []

    def data_set(self,data):
        self.L.set_data(data)
        self.Ld.set_data(np.random.uniform(np.min(self.L.features),np.max(self.L.features),self.L.features.shape))

    def gap(self,max_chack=20):
        for cluster in range(1,max_chack):
            self.L.k_means(cluster)
            self.Ld.k_means(cluster)
            self.G.append(math.log(self.Ld.inertia)-math.log(self.L.inertia))
        plt.plot(range(1,max_chack),self.G,marker='o')
        plt.show()



if __name__ == "__main__":
    data = np.random.uniform(-5,20,(161,128))
    gap = GAP()
    gap.data_set(data)
    gap.gap(10)


        