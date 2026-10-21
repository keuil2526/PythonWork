import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.preprocessing import MinMaxScaler as mms
from sklearn.preprocessing import StandardScaler as ss

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

#No_Scaling_Data
model = knn(n_neighbors = 5)

#Train_Model
model.fit(x_train, y_train)

#Accuracy_Test
accuracy = model.score(x_test, y_test)
print(f'Accuracy_None : {accuracy : .4f}')

#mms
scaler = mms()
x_train_mm = scaler.fit_transform(x_train)
x_test_mm = scaler.transform(x_test)

#Scaled_Data
knn_model = knn(n_neighbors = 5)

#Train_Model
knn_model.fit(x_train_mm, y_train)

#Accuracy_Test
accuracy = knn_model.score(x_test_mm, y_test)
print(f'Accuracy_mm : {accuracy : .4f}')