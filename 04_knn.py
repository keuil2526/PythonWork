import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knn

#Text_Print_With_Line
def printer(text):
    print()
    print('='*10, text, '='*10)
    print()

#Import_Preprocessing_Data
df = pd.read_csv('data/titanic_preprocessed.csv')
print(df.head(5))
printer('Data Load Completed')

#Separate_Feature_and_Label
x = df.drop('survived', axis = 1)
y = df['survived']
print(x.columns, x.shape)
print(y, y.shape)

#Separate_Train_and_Test_Data
x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.2, random_state = 42)
print('Train Data : ', x_train.shape)
print('Test Data : ', x_test.shape)

#Generate_KNN_Model
model = knn(n_neighbors = 5)
print(f'Model : {model}')

#Train_Model
model.fit(x_train, y_train)
printer('Train Completed')

#Predict
prediction = model.predict(x_test)
print(f'Predicted Answer : {prediction[:20]}')

#Accuracy_Test
accuracy = model.score(x_test, y_test)
print(f'Accuracy : {accuracy : .4f}')
print(f'Accuracy(%) : {accuracy*100 : .2f}')

#Compare_Predicted_Answer
result = pd.DataFrame({
    'Actual' : y_test.values,
    'Predicted' : prediction
})
print(result.head(20))

#New_Passenger_Predict
"""
Feature Sorting

pclass
gender
age
sibsp
parch
fare
embarked
"""

new_passenger = [[1, 0, 28, 0, 0, 100, 2]]

prediction = model.predict(new_passenger)
print('Alive') if prediction[0] == 1 else print('Dead')

#K_Value_Change_Test
score_log = []
even = []
for i in range(100):
    if i % 2 == 0:
        continue
    else:
        even.append(i)
for k in even: 
    model = knn(n_neighbors=k)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print(f'K : {k : 2d}\nAccuracy : {score : .4f}\n')
    score_log.append(score)
print(f'when K : {int(score_log.index(max(score_log)))*2+1}, score : {max(score_log) : .2f}')