# SecurePay - Unsupervised Credit Card Fraud Detection

## Project Overview

SecurePay is an unsupervised anomaly detection system designed to identify potentially fraudulent credit card transactions.

Financial fraud is highly imbalanced, with fraudulent transactions representing a very small percentage of total transactions. Traditional supervised classification can therefore be misleading when evaluated using accuracy alone.

This project focuses on identifying unusual transactions by learning the characteristics of normal transaction behavior.

## Algorithms Used

### 1. Isolation Forest

Isolation Forest detects anomalies by isolating observations using randomly selected features and split values.

### 2. Local Outlier Factor (LOF)

LOF identifies observations that exist in regions with significantly lower local density than their neighboring observations.

## Data Preprocessing

The credit card transaction dataset contains PCA-transformed features along with:

- Time
- Amount
- Class

The `Amount` feature was scaled using `RobustScaler` because it is less sensitive to extreme outliers.

## Exploratory Data Analysis

The project analyzes:

- Normal vs fraudulent transaction distribution
- Transaction Amount distribution
- Transaction Time distribution
- PCA feature space

## Evaluation Metrics

Because the dataset is highly imbalanced, the following metrics are used:

- Precision
- Recall
- F1-Score
- Confusion Matrix

Accuracy is not used as the primary evaluation metric.

## Results

### Isolation Forest

Precision: 0.0879  
Recall: 0.5569  
F1-Score: 0.1518

### LOF

Precision: 0.0575  
Recall: 0.3171  
F1-Score: 0.0973

## Contamination Tuning

Several contamination values were tested using Isolation Forest.

The best tested configuration was:

- Model: Isolation Forest
- Contamination: 0.005
- Precision: 0.1276
- Recall: 0.4228
- F1-Score: 0.1960

The contamination value of 0.005 produced the highest F1-score among the tested configurations.

## Visualizations

The project includes:

- Class imbalance visualization
- Transaction Amount distribution
- Transaction Time distribution
- PCA visualization
- Isolation Forest anomaly visualization
- LOF anomaly visualization
- Precision-Recall curve
- Contamination tuning graph
- Confusion matrices

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Project Structure

```text
SecurePay_Fraud_Detection/
│
├── data/
│   └── creditcard.csv
│
├── models/
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── results/
│   ├── metrics/
│   └── plots/
│
├── src/
│
├── requirements.txt
├── README.md
└── .gitignore