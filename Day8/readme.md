# Breast Cancer Prediction System

## Overview
This project uses the Breast Cancer Wisconsin Diagnostic Dataset from Scikit-learn to predict whether a tumor is **Benign** or **Malignant** using Logistic Regression. The model is evaluated and improved using Hyperparameter Tuning with GridSearchCV.

## Project Files

- `Dataset_Exploration.py` - Explore the dataset using Pandas.
- `Baseline_Model.py` - Train and evaluate the baseline Logistic Regression model.
- `Hyperparameter_Tuning.py` - Tune the model using GridSearchCV and compare the results.
- `breast_cancer.py` - Complete prediction pipeline with final evaluation.
- `confusion_matrix.png` - Confusion matrix of the final model.
- `baseline_vs_tuned.png` - Comparison graph of baseline and tuned models.

## Dataset
- Breast Cancer Wisconsin Diagnostic Dataset
- Source: Scikit-learn

## What I Learned
- Model Evaluation
- Accuracy, Precision, Recall and F1-Score
- Confusion Matrix
- Underfitting and Overfitting
- Cross Validation
- Hyperparameter Tuning
- GridSearchCV

## Best Parameters
- C = 0.1
- Solver = liblinear

## Baseline vs Tuned Model

| Metric | Baseline | Tuned |
|---------|----------|--------|
| Accuracy | 97.37% | 99.12% |
| Precision | 97.22% | 98.61% |
| Recall | 98.59% | 100.00% |
| F1-Score | 97.90% | 99.30% |

## Key Observations
- Data scaling improved model performance.
- GridSearchCV found the best hyperparameters automatically.
- The tuned model performed better than the baseline model.
- The final model achieved higher Accuracy, Precision, Recall, and F1-Score.

## Requirements

- Python 3
- Pandas
- Matplotlib
- Scikit-learn

## How to Run

```bash
python Dataset_Exploration.py
python Baseline_Model.py
python Hyperparameter_Tuning.py
python breast_cancer.py
```

## Output
- Dataset exploration
- Baseline model evaluation
- Tuned model evaluation
- Best hyperparameters
- Confusion Matrix
- Baseline vs Tuned comparison graph