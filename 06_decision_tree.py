import pandas as pd
import matplotlib as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.model_selection import cross_val_score as cvs
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score

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

#Decision_Tree
model = dtc(max_depth = 3, random_state = 42)

#Learn
model.fit(x_train, y_train)

#Predict
prediction = model.predict(x_test)

#Calculate_Accuracy
accuracy = accuracy_score(y_test, prediction)
print(f'Accuracy : {accuracy : .4f}')