import pandas as pd
from pandas import DataFrame
from LabWorks.algoritms.knnLib.KNN import KNN


data = pd.read_csv(r"/Users/ruslantagirov/Desktop/transfusion.data.csv")
test = pd.read_csv(r"/Users/ruslantagirov/Desktop/transfusion.test.data.csv")
Y_test = test['whether he/she donated blood in March 2007']
test = test.drop(['whether he/she donated blood in March 2007'], axis=1)
my_result = DataFrame()
my_result['1'] = Y_test
knn_classifier = KNN(data, test, 6, 'whether he/she donated blood in March 2007')
my_result.insert(1, 'after', knn_classifier.predictClassification())
print('Classification: ', knn_classifier.score(my_result, '1', 'after'))

keep_col = ['ID', 'OUTCOME', 'TIME', 'RADIUS', 'TEXTURE', 'PERIMETR', 'AREA', 'SMOOTHNESS', 'COMPACTNESS', 'CONCAVITY']
data_w = pd.read_csv(r"/Users/ruslantagirov/Desktop/breast-cancer-wisconsin.data.csv")
test_w = pd.read_csv(r"/Users/ruslantagirov/Desktop/breast-canser-wisconsin.test.data.csv")
data2 = data_w[keep_col]
test2 = test_w[keep_col]
Y_test2 = test2['OUTCOME']
test2 = test2.drop(['OUTCOME'], axis=1)
my_result2 = DataFrame()
my_result2['1'] = Y_test2
knn_regression = KNN(data2, test2, 5, 'OUTCOME')
my_result2.insert(1, 'after', knn_regression.predictRegression())
print('Regression: ', knn_regression.score(my_result2, '1', 'after'))
