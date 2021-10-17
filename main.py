from correlation_matrix import Correlation
from readfile import ReadData
from classifierfile import Classification
if __name__ == '__main__':
    # obj = Classification('LogisticRegression', prepocessing='correlation')
    obj = Classification('MLP One', prepocessing='correlation')
    data = obj.data
    # print("dataset \n", data)
