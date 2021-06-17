import json
import glob

class LoadFile:
    def __init__(self,data):
        self.data = data

    def input_split_file(self,input_path):
        self.data = []
        path = input_path 
        data_storage = {"norm":[],"gyro":[]}
        files = glob.glob(path + "/*")
        files = sorted(files,key=lambda x:int(x.split("\\")[-1].split(".")[-2].split("_")[-1]))
        for file in files:
            norm = []
            gyro = []
            with open(file) as f:
                lines = f.readlines()
                norm += [float(row.split(",")[1]) for row in lines]
                data_storage["norm"] = norm
                gyro += [float(row.split(",")[2]) for row in lines]
                data_storage["gyro"] = gyro
                self.data.append(data_storage.copy())

    def output_file(self,output_path):
        path = output_path
        for index,output in enumerate(self.data):
            with open(path + str(index)+".txt","w") as f:
                f.write(json.dumps(output))

    def get_data(self):
        return self.data

    def make_dict_data(self,data,dict,key):
        for index,item in enumerate(data):
                dict[index][key] = item
        self.data = dict

if __name__ == "__main__":
    data = LoadFile([])
    data.input_split_file(".\\clusterling\\input_split_data\\")
    data.output_file(".\\clusterling\\norm_data\\")