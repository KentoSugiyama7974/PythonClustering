import pandas as pd
import numpy as np

class DataCalculation():
    def __init__(self,path):
        self.data = None
        self.norm = None
        self.names = "ABCDEFGHIJ"
        self.read_data(path)
        self.calculation_norm()
        
    def read_data(self,path):
        self.data = dict()
        for name in self.names:
            self.data[name] = pd.read_csv(path+name+"_sensor.csv",usecols=[x for x in range(1,10)])

    def calculation_norm(self):
        self.norm = dict()
        for name in self.names:
            df = self.data[name]
            self.norm[name] = ((df["x_acc"]**2 + df["y_acc"]**2 + df["z_acc"]**2)**(1/2)).values

    def get_data(self):
        return self.data

    def get_norm(self):
        return self.norm

    def get_2dim_norm(self,shape=60):
        for name in self.names:
            much = len(self.norm[name])%shape
            mean = self.norm[name].mean()
            plus = [mean for x in range(shape-much)]
            self.norm[name] = np.append(self.norm[name],plus)
            self.norm[name] = self.norm[name].reshape(-1,shape)
        return self.norm
        

if __name__ == "__main__":
    path = "c:/Users/ymtlab/Documents/20211214/1/"
    a = DataCalculation(path)
    norm = a.get_2dim_norm()
    print(norm["J"])