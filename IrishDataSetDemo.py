import sys
import numpy
import scipy
import metaplot
import sklearn
import pandas

# data set URL
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pandas.read_csv(url, names=names)

# Displays number or records and number of columns
# print(dataset.shape)

# Displays first 30 records
# print(dataset.head(30))

# data set description with all possible aggregation
# print(dataset.describe())

# Display data set by the group
# print(dataset.groupby('class').size())

# Draw plot based on the data
# dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
# metaplot.plt.show()

# Show histogram base on the data
# dataset.hist()
# metaplot.plt.show()

# Show scatter matrix based graph for multivariet plot
# scatter_matrix(dataset)
# metaplot.plt.show()

# Evaluate data set using ML Algorithms
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]

validation_size = 0.20
seed = 6

x_train, x_test, y_train, y_text = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)

seed = 6
scoring = 'accuracy'

# Spot check algorithms
models = [('LR', LogisticRegression(solver='lbfgs', multi_class='auto')),
          ('LDA', LinearDiscriminantAnalysis()),
          ('KNN', KNeighborsClassifier()),
          ('CART', DecisionTreeClassifier()),
          ('NB', GaussianNB()),
          ('SVM', SVC(gamma='auto'))]

# Evaluate each model in turn
results = []
names = []

for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
