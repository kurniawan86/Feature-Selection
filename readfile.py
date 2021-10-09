import pandas as panda
from sklearn.datasets import load_diabetes

class ReadData:
    def __init__(self):
        pass

    def readCSV(self):
        data = panda.read_csv('train_data.csv')
        return data

    def readDiabetes(self):
        dataset = panda.read_csv('diabetes.csv')
        label = dataset['Outcome']
        data = dataset.drop('Outcome', 1)
        return data,label

    def readDiabetesDataset(self):
        dataset = panda.read_csv('diabetes.csv')
        df = panda.DataFrame(dataset)
        return df