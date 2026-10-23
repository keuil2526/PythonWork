import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.model_selection import cross_val_score as cvs
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.preprocessing import MinMaxScaler as mMs
from sklearn.preprocessing import StandardScaler as ss

#Text_Print_With_Line
def printer(text):
    print()
    print('='*10, text, '='*10)
    print()

#Import_PreprocessedData
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

#Minmax_Scaling
mM_scaler = mMs()
x_train_mM = mM_scaler.fit_transform(x_train)
x_test_mM = mM_scaler.transform(x_test)

#Scaled_Data
knn_model = knn(n_neighbors = 5)

#Train_Model
knn_model.fit(x_train_mM, y_train)

#Accuracy_Test
accuracy_mM = knn_model.score(x_test_mM, y_test)
print(f'Accuracy_mM : {accuracy_mM : .4f}')

#Standard_Scaling
std_scaler = ss()
std_scaler.fit(x_train)
x_train_std = std_scaler.fit_transform(x_train)
x_test_std = std_scaler.transform(x_test)

#Train_Model
knn_model.fit(x_train_std, y_train)

#Accuracy_Test
accuracy_ss = knn_model.score(x_test_std, y_test)
print(f'Accuracy_std : {accuracy_ss : .4f}')

#Cross_Validation
x_std = std_scaler.fit_transform(x)
scores = cvs(knn(n_neighbors = 5), x_std, y, cv = 5)

printer('Each Fold Accuracy')
for i, score in enumerate(scores, start = 1):
    print(f"Fold_{i} : {score:.4f}")
print()
print(f"Average_Accuracy : {scores.mean():.4f}")