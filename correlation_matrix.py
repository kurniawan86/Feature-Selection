import matplotlib.pyplot as plt
import pandas as panda
from readfile import ReadData
import seaborn as sn

class Correlation:
    dataset =[]
    data = []
    target = []
    corrMatrix = None
    best = None

    def __init__(self):
        obj = ReadData()
        self.dataset = obj.readDiabetesDataset()
        self.getCorrelation()
        self.getRelevanFeature(0.2)
        self.createData()
        self.visualCorrelation()

    def getCorrelation(self):
        self.corrMatrix = self.dataset.corr()

    def visualCorrelation(self):
        sn.heatmap(self.corrMatrix, annot=True)
        plt.show()

    def viewData(self):
        print("dataset \n", self.data)

    def getRelevanFeature(self,th):
        cor = (self.corrMatrix['Outcome'])
        releFeature = cor[cor > th]
        self.best = releFeature.index
    
    def createData(self):
        new = panda.DataFrame()
        cols = self.dataset.columns
        i = 0
        for item in cols:
            cek = False
            for best in self.best:
                if item==best:
                    cek = True
            if cek==True:
                new.insert(i,self.dataset.columns[i],self.dataset[item])
                i = i+1
        self.data = new
        self.target = self.dataset['Outcome']

    def getXY(self):
        return self.data, self.target