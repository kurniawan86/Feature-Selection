import matplotlib.pyplot as plt
from readfile import ReadData
import seaborn as sn

class Correlation:
    dataset =[]
    data = []
    target = []
    corrMatrix = None


    def __init__(self):
        self.getXY()

    def getXY(self):
        obj = ReadData()
        x, y = obj.readDiabetes()
        self.label = y
        self.data = x

    def getCorrelation(self):
        corr = self.data.corr()
        self.corrMatrix = corr

    def visualCorrelation(self):
        sn.heatmap(self.corrMatrix, annot=True)
        plt.show()

    def viewData(self):
        print("dataset \n", self.data)

    def getCorrelationMatrix(self):
        return self.corrMatrix