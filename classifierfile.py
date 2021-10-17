from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from correlation_matrix import Correlation
from readfile import ReadData


class classifiers:
    def __init__(self):
        pass

    def logicticRegression(self, X, y):
        model = LogisticRegression(random_state=0).fit(X, y)
        print("Coef each Attribute :", model.coef_)
        return model

    def pickClassifier(self, model, X, y):
        if model == 'LogisticRegression':
            return self.logicticRegression(X, y)
        elif model == 'SVM':
            return self.svm(X, y)
        elif model == 'KNN':
            return self.KNN(X, y)
        elif model == 'MLP':
            return self.MLP(X, y)
        elif model =='MLP One':
            return self.MLP_One(X, y)
        else:
            return 0

    def svm(self, X, y):
        clf = svm.SVC(kernel='linear', C=2, random_state=42)
        clf.fit(X, y)
        return clf

    def MLP(self, X, y):
        clf = MLPClassifier(random_state=1, max_iter=500)
        clf.fit(X, y)
        return clf

    def MLP_One(self, X, y):
        clf = MLPClassifier(hidden_layer_sizes=1, random_state=1, max_iter=1000, activation='identity')
        clf.fit(X, y)
        print(clf.coefs_)
        return clf

    def KNN(self, X, y):
        neigh = KNeighborsClassifier(n_neighbors=3)
        neigh.fit(X, y)
        return neigh

class Classification:
    data = []
    target = []
    model = None
    classy = classifiers()

    def __init__(self,modelname,prepocessing=None):
        if prepocessing==None:
            self.getXYFromReadile()
        elif prepocessing=='correlation':
            print(prepocessing)
            self.getXYfromCorrelation()
        self.getModel(modelname)
        self.scoreTest()

    def getXYFromReadile(self):
        obj = ReadData()
        x, y = obj.readDiabetes()
        self.target = y
        self.data = x

    def getXYfromCorrelation(self):
        obj = Correlation()
        x,y = obj.getXY()
        self.target = y
        self.data = x

    def getModel(self, modelname):
        self.model = self.classy.pickClassifier(
            modelname, self.data, self.target)

    def setLabelClassifier(self):
        return self.model.predict(self.data)

    def scoreTest(self):
        print("Scoring Testing:")
        print("----------------------------")
        ypred = self.setLabelClassifier()
        accuracy = accuracy_score(ypred, self.target)
        print('Accuracy: %f' % accuracy)
        precision = precision_score(ypred, self.target)
        print('Precision: %f' % precision)
        # recall: tp / (tp + fn)
        recall = recall_score(ypred, self.target)
        print('Recall: %f' % recall)
        # f1: 2 tp / (2 tp + fp + fn)
        f1 = f1_score(ypred, self.target)
        print('F1 score: %f' % f1)
        print("----------------------------")
        print("*************************")