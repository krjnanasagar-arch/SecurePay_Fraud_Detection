# SecurePay - Unsupervised Credit Card Fraud Detection

## Project Overview

SecurePay is an unsupervised anomaly detection system designed to identify potentially fraudulent credit card transactions.

Financial fraud detection is a highly imbalanced problem, where fraudulent transactions represent a very small percentage of total transactions. Therefore, accuracy alone is not an appropriate primary evaluation metric.

This project focuses on detecting unusual transaction patterns by learning the characteristics of normal transaction behavior.

## Algorithms Used

### 1. Isolation Forest

Isolation Forest is an anomaly detection algorithm that identifies unusual observations by isolating them using randomly selected features and split values.

### 2. Local Outlier Factor (LOF)

Local Outlier Factor identifies observations that exist in regions with significantly lower local density compared with their neighboring observations.

## Data Preprocessing

The dataset contains PCA-transformed transaction features along with:

- Time
- Amount
- Class

The `Amount` feature was scaled using `RobustScaler`, which is less sensitive to extreme values and outliers.

The original dataset is not included in the GitHub repository because of its large file size.

## Exploratory Data Analysis

The project includes analysis of:

- Normal vs fraudulent transaction distribution
- Transaction Amount distribution
- Transaction Time distribution
- PCA feature space
- Detected anomalies

## Evaluation Metrics

Because the dataset is highly imbalanced, the following metrics are used:

- Precision
- Recall
- F1-Score
- Confusion Matrix

Accuracy is not used as the primary evaluation metric.

## Results

### Isolation Forest

- Precision: 0.0879
- Recall: 0.5569
- F1-Score: 0.1518

### Local Outlier Factor

- Precision: 0.0575
- Recall: 0.3171
- F1-Score: 0.0973

## Contamination Tuning

Several contamination values were tested using Isolation Forest.

The best tested configuration was:

- Model: Isolation Forest
- Contamination: 0.005
- Precision: 0.1276
- Recall: 0.4228
- F1-Score: 0.1960

The contamination value of `0.005` produced the highest F1-score among the tested configurations.

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
│   └── creditcard.csv          # Local dataset, not uploaded to GitHub
│
├── models/                     # Saved trained models
│
├── notebooks/
│   └── fraud_detection.ipynb   # Complete analysis and experiments
│
├── results/
│   ├── metrics/                # Evaluation results
│   └── plots/                  # Generated visualizations
│
├── src/                        # Project source code
│
├── requirements.txt
├── README.md
└── .gitignore