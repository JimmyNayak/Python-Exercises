import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# This demo includes the machine learning study step by step.

# Step 1 : Import the data
# Step 2 : clear or preparing the data (includes remove duplicates,null values and etc)
# Step 3 : Split the data into training / test sets
# Step 4 : Create model
# Step 5 : Train the model
# Step 6 : Make predictions
# Step 7 : Evaluate and improve

# Note :
#    Always test and train model accuracy. To find the model accuracy the thumb rule is
#    to divide 70-80% data for training and divide 20-30% data for testing


# Step 1
music_data = pd.read_csv('material/music.csv')

# print(music_data)

# print(music_data.shape)

# print(music_data.describe())

# print(music_data.values)

# Step 2 : No data which full fill the step 2 requirement

# Step 3
X = music_data.drop(columns=['genre'])
Y = music_data['genre']
# print(X)
# print(Y)

# Step 5
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Step 4
model = DecisionTreeClassifier()
# model.fit(X, Y)
model.fit(X_train, Y_train)

# Step 6
# predictions = model.predict([[21, 1], [22, 0]])
predictions = model.predict(X_test)
print(predictions)

# Step 7
score = accuracy_score(Y_test,predictions)
print(score)

