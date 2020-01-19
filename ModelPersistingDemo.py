import pandas as pd
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeClassifier

#  To generate the job lib model file

# music_data = pd.read_csv('material/music.csv')
# X = music_data.drop(columns=['genre'])
# Y = music_data['genre']
# model = DecisionTreeClassifier()
#
# model.fit(X, Y)
#
# joblib.dump(model, 'material/music-recommended.joblib')

# Load jovlib model

model = joblib.load('material/music-recommended.joblib')
predictions = model.predict([[21, 1]])
print(predictions)
