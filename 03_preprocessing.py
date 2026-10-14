#Data_preprocessing
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Text_Print_With_Line
def printer(text):
    print()
    print('='*10, text, '='*10)
    print()

#Import_Data
df = pd.read_csv('data/lux_data.csv')
print('Data Read Successfully')

#Check_data_size
print(f'Data Size : {df.shape}')

#Check_missing_values
printer('Missing Values Before Processing')
missing = df.isnull().sum()
print(missing[missing > 0])

#Select_Image_Feature_Columns
#Use luma and gradient features from center + 4 corners + square region
FEATURE_COLS = [
    'C_mean_luma', 'C_std_luma', 'C_grad_mean', 'C_grad_std',
    'UL_mean_luma', 'UL_std_luma', 'UL_grad_mean', 'UL_grad_std',
    'UR_mean_luma', 'UR_std_luma', 'UR_grad_mean', 'UR_grad_std',
    'LR_mean_luma', 'LR_std_luma', 'LR_grad_mean', 'LR_grad_std',
    'LL_mean_luma', 'LL_std_luma', 'LL_grad_mean', 'LL_grad_std',
    'corner_mean_luma', 'corner_std_luma', 'corner_range_luma',
    'C_minus_corner_mean_luma', 'C_over_corner_mean_luma',
    'square_mean_luma', 'square_std_luma',
    'square_grad_mean', 'square_grad_std',
    'square_mean_sat_proxy',
    'square_bottom_minus_top_luma', 'square_right_minus_left_luma',
    'square_center_minus_corners_luma',
    'square_grid_range_mean_luma', 'square_grid_std_mean_luma',
]

TARGET_COL = 'target_lux'

#Select_Columns
df_model = df[FEATURE_COLS + [TARGET_COL]].copy()
print(f'\nSelected {len(FEATURE_COLS)} feature columns')

#Handle_missing_values (corner features NaN for 1point images - fill with C value)
for col in FEATURE_COLS:
    if df_model[col].isnull().sum() > 0:
        col_mean = df_model[col].mean()
        df_model[col] = df_model[col].fillna(col_mean)
        print(f'Filled NaN in {col} with mean={col_mean:.4f}')

printer('Missing Values After Processing')
print(df_model.isnull().sum().sum(), 'total missing values remain')

#Separate_Feature_and_Label
x = df_model[FEATURE_COLS]
y = df_model[TARGET_COL]
print(f'\nFeature shape : {x.shape}')
print(f'Label  shape : {y.shape}')
print(f'Label  range : {y.min()} ~ {y.max()}')

#Save_Preprocessed_Data
df_model.to_csv('data/lux_preprocessed.csv', index=False)
printer('Preprocessed Data Saved to lux_preprocessed.csv')
