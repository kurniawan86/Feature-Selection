import pandas as panda
from sklearn.datasets import load_diabetes

class ReadData:
    def __init__(self):
        pass

    def readCSV(self):
        data = panda.read_csv('train_data.csv')
        return data

    def readDiabetes(self):
        diabetes = load_diabetes()
        data = diabetes.data
        features = diabetes.feature_names
        df = panda.DataFrame(data, columns = features)
        return df