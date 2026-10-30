import pandas as pd
import matplotlib.pyplot as plt
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

#CV
scores = cvs(model, x, y, cv = 5)
printer('Each Fold Accuracy')

for i, score in enumerate(scores, start = 1):
    print(f"Fold {i}: {score : .4f}")
print()
print(f'Average Accuracy: {scores.mean() : .4f}')

#Feature_Importance
printer("Feature Importance")

importance = pd.DataFrame({
    "Feature": x.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(by = "Importance", ascending = False)

print(importance)

#Feature_Importance_Graph
plt.figure(figsize = (8,5))

plt.bar(importance["Feature"], importance["Importance"])

plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")

plt.xticks(rotation = 45)

plt.tight_layout()

plt.show()

#Decision_Tree_Visualize
plt.figure(figsize = (18, 10))

plot_tree(
    model,
    feature_names = x.columns,
    class_names = ["Dead", "Survived"],
    filled = True,
    rounded = True,
    fontsize = 9
)

plt.title("Decision Tree")

plt.show()

#New_Passenger_Predict
new_passenger = pd.DataFrame([{
    "pclass": 1,
    "gender": 0,
    "age": 25,
    "sibsp": 0,
    "parch": 0,
    "fare": 80,
    "embarked": 2
}])

result = model.predict(new_passenger)

print("\n")
print("=" * 60)

if result[0] == 1:
    print("Predict Result : Survived")
else:
    print("Predict Result : Dead")