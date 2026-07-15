

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("cleaned_student_data.csv")
# print(data.head())

# data.info()

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


print("\nShapes\n")
print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)