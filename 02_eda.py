import pandas as pd

#Text_Print_With_Line
def printer(text):
    print()
    print('='*10, text, '='*10)
    print()

printer('Lux Data EDA')

#Import_Data
df = pd.read_csv('data/lux_data.csv')
print('Data Read Successfully')

#5_Data_front
print(df.head())

#5_Data_back
print(df.tail())

#5_Data_Random
print(df.sample(5, random_state=42))

#Data_size_check
rows, cols = df.shape
print(f'rows : {rows}')
print(f'cols : {cols}')
print(f'shape : {df.shape}')

#See_column
printer('Column List')
for i, col in enumerate(df.columns, start=1):
    print(f'{i:3d}. {col}')

#Data_type
printer('Data Info')
df.info()

#Summary_Statics (numeric only)
printer('Summary Statistics')
print(df.describe())

#Check_Label (target : target_lux = lux_C)
printer('Target Label Distribution (target_lux)')
print(f'Min  : {df["target_lux"].min()}')
print(f'Max  : {df["target_lux"].max()}')
print(f'Mean : {df["target_lux"].mean():.2f}')
print(f'Std  : {df["target_lux"].std():.2f}')

#Label_Kind_Distribution (1point vs 5point)
printer('Label Kind Distribution')
print(df['label_kind'].value_counts())
print('\nratio')
print(df['label_kind'].value_counts(normalize=True))

#Surface_Group_Distribution
printer('Surface Group Distribution')
print(df['surface_group_norm'].value_counts())

#Check_Null
printer('Missing Values per Column')
missing = df.isnull().sum()
print(missing[missing > 0])

#Check_duplicates
dup = df.duplicated().sum()
print(f'\nDuplicate Rows : {dup}')

#Lux_Range_by_Surface_Group
printer('Mean Lux by Surface Group')
print(df.groupby('surface_group_norm')['target_lux'].describe())
