from readfile import ReadData
import pandas as pd
import numpy as np

class combination:
    datasetOri = []
    objData = ReadData()
    dataset = []
    y = []

    def __init__(self):
        self.datasetOri = self.objData.readDiabetesDataset()
        self.getTarget()
        self.viewData()
        self.createData()

    def viewData(self):
        print("target Data ", self.y)

    def createData(self):
        df = self.datasetOri.iloc[:, 0]
        df1 = self.datasetOri.iloc[:, 1]
        df.append(df1)
        asu = df.values.tolist()
        print(df)

    def getCombination(self):
        pass

    def getTarget(self):
        self.y = self.datasetOri.iloc[:,0]
        self.y = np.array(self.y)