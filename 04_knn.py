import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsRegressor as knn
from sklearn.metrics import mean_absolute_error, mean_squared_error

#Text_Print_With_Line
def printer(text):
    print()
    print('='*10, text, '='*10)
    print()

TARGET_COL = 'target_lux'

#Import_Preprocessed_Data
df = pd.read_csv('data/lux_preprocessed.csv')
print(df.head(5))
printer('Data Load Completed')

#Separate_Feature_and_Label
x = df.drop(TARGET_COL, axis=1)
y = df[TARGET_COL]
print(f'Feature columns : {list(x.columns)}')
print(f'Feature shape   : {x.shape}')
print(f'Label  shape    : {y.shape}')

#Separate_Train_and_Test_Data
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=42)
print(f'Train Data : {x_train.shape}')
print(f'Test  Data : {x_test.shape}')

#Generate_KNN_Regressor_Model
model = knn(n_neighbors=5)
print(f'Model : {model}')

#Train_Model
model.fit(x_train, y_train)
printer('Train Completed')

#Predict
prediction = model.predict(x_test)
print(f'Predicted (first 20) : {prediction[:20].round(1)}')

#Accuracy_Test (Regression Metrics)
mae  = mean_absolute_error(y_test, prediction)
rmse = np.sqrt(mean_squared_error(y_test, prediction))
r2   = model.score(x_test, y_test)

printer('Model Performance (K=5)')
print(f'MAE  (Mean Absolute Error)       : {mae:.2f} lux')
print(f'RMSE (Root Mean Squared Error)   : {rmse:.2f} lux')
print(f'R2   Score                       : {r2:.4f}')

#Compare_Predicted_Answer
result = pd.DataFrame({
    'Actual'    : y_test.values,
    'Predicted' : prediction.round(1),
    'Error'     : (y_test.values - prediction).round(1)
})
print(result.head(20))

#New_Sample_Predict
"""
Feature Order (35 features)
C_mean_luma, C_std_luma, C_grad_mean, C_grad_std,
UL_mean_luma, UL_std_luma, UL_grad_mean, UL_grad_std,
UR_mean_luma, UR_std_luma, UR_grad_mean, UR_grad_std,
LR_mean_luma, LR_std_luma, LR_grad_mean, LR_grad_std,
LL_mean_luma, LL_std_luma, LL_grad_mean, LL_grad_std,
corner_mean_luma, corner_std_luma, corner_range_luma,
C_minus_corner_mean_luma, C_over_corner_mean_luma,
square_mean_luma, square_std_luma, square_grad_mean, square_grad_std,
square_mean_sat_proxy,
square_bottom_minus_top_luma, square_right_minus_left_luma,
square_center_minus_corners_luma,
square_grid_range_mean_luma, square_grid_std_mean_luma
"""
new_sample = x_test.iloc[[0]]
new_pred = model.predict(new_sample)
printer('New Sample Prediction')
print(f'Actual  : {y_test.iloc[0]} lux')
print(f'Predicted : {new_pred[0]:.1f} lux')

#K_Value_Change_Test
printer('K Value Search (odd 1~99)')
score_log = []
even = []
for i in range(100):
    if i % 2 == 0:
        continue
    else:
        even.append(i)

for k in even:
    model_k = knn(n_neighbors=k)
    model_k.fit(x_train, y_train)
    r2_k = model_k.score(x_test, y_test)
    mae_k = mean_absolute_error(y_test, model_k.predict(x_test))
    print(f'K : {k:2d}  R2 : {r2_k:.4f}  MAE : {mae_k:.2f} lux')
    score_log.append(r2_k)

best_k = even[score_log.index(max(score_log))]
printer('Best K')
print(f'Best K : {best_k},  Best R2 : {max(score_log):.4f}')
