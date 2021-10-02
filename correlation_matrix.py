import matplotlib.pyplot as plt
from readfile import ReadData
import seaborn as sn

class Correlation:
    data = None
    corrMatrix = None

    def __init__(self):
        obj = ReadData()
        self.data = obj.readCSV()
        self.getCorrelation()
        self.visualCorrelation()

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