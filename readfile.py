import pandas as panda

class ReadData:
    def __init__(self):
        pass

    def readCSV(self):
        data = panda.read_csv('train_data.csv')
        return data