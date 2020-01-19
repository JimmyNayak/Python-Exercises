import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('material/music.csv')
X = music_data.drop(columns=['genre'])
Y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X, Y)

tree.export_graphviz(model, out_file='material/music-recommended.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(Y.unique()), label='all', rounded=True, filled=True)
