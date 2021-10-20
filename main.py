from correlation_matrix import Correlation
from readfile import ReadData
from classifierfile import Classification
from combination import combination
if __name__ == '__main__':
    #obj = Classification('LogisticRegression', prepocessing='correlation')
    obj = Classification('KNN')
    data = obj.data
    print("dataset \n", data)
    #combinasi = combination()
    

