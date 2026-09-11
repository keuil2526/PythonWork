#Data_preprocessing
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Text_Print_With_Line
def printer(text):
    print('='*10, text, '='*10)
    print()

#Import_data
df = pd.read_csv('data/train.csv')
print('Data Read Successfully')

#Check_data_size
print(f'Data Size : {df.shape}')

#Check_missing_values
missing = df.isnull().sum()
print(missing)

#Handle_missing_age_values
age_mean = df['age'].mean()
print(f'\nAverage age : {age_mean:.2f}')
df['age'] = df['age'].fillna(age_mean)
printer('Handled Missing Age Values')
print('Remaining Missing Age Values :', df['age'].isnull().sum())

#Handle_missing_embarked_values
mode = df['embarked'].mode()[0]
print(f'\nEmbarked Mode : {mode}')
df['embarked'] = df['embarked'].fillna(mode)
printer('Handled Missing Embarked Values')
print('Remaining Missing Embarked Values :', df['embarked'].isnull().sum())

#Delete_Cabin_Column
df.drop(columns = ['cabin'], inplace = True)
print('\nDeleted Cabin Column')
print(df.columns)

#Handle_missing_fare_values
fare_median = df['fare'].median()
print(f'\nFare Median : {fare_median}')
df['fare'] = df['fare'].fillna(fare_median)
printer('Handled Missing Fare Values')
print('Remaining Missing Fare Values :', df['fare'].isnull().sum())

drop_columns = [
    "name",
    "ticket",
    "home.dest",
    "boat",
    "body"
]

df.drop(columns = drop_columns, inplace = True)
print()
printer('List Column After Deleting')
print(df.columns)

#Label_Encoding
#Make_Object/Gender[0,1],Embarked[0,1,2]
encoder = LabelEncoder()
df['gender'] = encoder.fit_transform(df['gender'])
printer('Gender Encoding Completed')
print(df['gender'].head(5))

df['embarked'] = encoder.fit_transform(df['embarked'])
printer('Embarked Encoding Completed')
print(df['embarked'].head(5))

#Separate_Feature_and_Label
x = df.drop('survived', axis = 1)
y = df['survived']