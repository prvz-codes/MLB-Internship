# Student Score Prediction System

## Files

* DataPreProcessing.py
* LinearRegression.py
* StudentScorePrediction.py
* cleaned_student_data.csv
* actual_vs_predicted.png

## Tools Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

## What I Learned

* Loaded and processed a dataset using Pandas.
* Selected features (X) and target (y).
* Created the `Average_Marks` column.
* Split the dataset into training and testing data.
* Applied feature scaling using `StandardScaler`.
* Built a Linear Regression model.
* Made predictions and evaluated the model.

## Why Train-Test Split is Important

The dataset is divided into:

* 80% Training Data
* 20% Testing Data

The training data is used to train the model, and the testing data is used to check how well the model performs on new data.

## Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

## Model Performance

* MAE: Very close to 0
* MSE: Very close to 0
* R² Score: 1.0

The model performed very well because `Average_Marks` is calculated from the subject marks used as input features.

## How to Run

```bash
python StudentScorePrediction.py
```
