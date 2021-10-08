from correlation_matrix import Correlation
from readfile import ReadData

if __name__ == '__main__':
    obj = Correlation()
    print("label :", obj.label)
    print("data :\n", obj.data)