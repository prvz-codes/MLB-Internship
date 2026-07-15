import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


data = pd.read_csv("cleaned_student_data.csv")


x = data[[
        "Math",
        "English",
        "Science",
        "Computer",
        "Physics",
        "Chemistry"
    ]]


y = data["Average_Marks"]


X_train , X_test , y_train , y_test = train_test_split(x ,y ,test_size = 0.20 , random_state = 42)

# print("Training Features:")
# print(X_train.head())



# print("\nTesting Features:")
# print(X_test.head())


# print("\nTraining Target:")
# print(X_test[:5])



scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

linearModel = LinearRegression()

linearModel.fit(X_train , y_train)

modelPred = linearModel.predict(X_test)

comp = pd.DataFrame({"Actual " : y_test.values , "Predicted : " :  modelPred})

print(comp.head())


mae = mean_absolute_error(y_test , modelPred)

mse = mean_squared_error(y_test , modelPred)
r2 = r2_score(y_test , modelPred)

print("Mean Absolute Error :", mae)
print("Mean Squared Error :", mse)
print("R² Score :", r2)