import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knn

#Text_Print_With_Line
def printer(text):
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
print(model)

#Train_Model
model.fit(x_train, y_train)
printer('Train Completed')

#Predict
prediction = model.predict(x_test)
printer('Predicted Answer')
print(prediction[:20])