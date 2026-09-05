# Forest Fire Detection 🔥

A beginner-friendly machine-learning pipeline that predicts forest-fire risk from environmental measurements.

## Features
- Generates a demo dataset when no real dataset is supplied
- Cleans numeric data and handles missing values
- Compares SVM and Random Forest classifiers
- Reports accuracy and a classification report
- Saves the best model with Joblib

## Input columns
`temperature`, `humidity`, `wind`, `rain`, `risk`

## Run
```bash
pip install -r requirements.txt
python train.py
```

The trained model is saved to `models/fire_risk_model.joblib`.

> This is an educational ML project, not a real fire-safety system.
