import pandas as pd

#show_string
def text_show(text):
    print('=' * 80)
    print(text)
    print('=' * 80)

text_show('Titanic data read')

df = pd.read_csv('data/train.csv')
print('Data Read Successfully')

#5_Data_front
print(df.head())

#5_Data_back
print(df.tail())

#5 Data_Random
print(df.sample(5, random_state = 42))

#Data_size_check
rows, cols = df.shape 
print(f'rows : {rows}')
print(f'cols : {cols}')
print(f'shape : {df.shape}')

#See_column
for i, col in enumerate(df.columns, start = 1):
    print(f'{i:2d}. {col}')

#Data_type
df.info()

#Summary_Statics
print(df.describe(include = 'all'))

#Check_Label
print(df['survived'].value_counts())
print('\nratio')
print(df['survived'].value_counts(normalize = True))

#Check_Null
missing = df.isnull().sum()
print(missing)

#Check_duplicates
dup = df.duplicated().sum()
print(dup)