# 💳 SecurePay - AI-Based Credit Card Fraud Detection

## 🚀 Live Demo

**Streamlit Application:**
https://securepayfrauddetection-kzgdjgjgwx8e7we92a9uk.streamlit.app

**FastAPI Backend:**
https://securepay-fraud-api.onrender.com

**API Documentation:**
https://securepay-fraud-api.onrender.com/docs

---

## 📌 Project Overview

SecurePay is an AI-based credit card fraud detection system that uses **unsupervised anomaly detection** to identify potentially fraudulent transactions.

Credit card fraud detection is a highly imbalanced problem, where fraudulent transactions represent only a very small percentage of all transactions. Therefore, traditional accuracy is not sufficient as the primary evaluation metric.

SecurePay learns patterns from transaction data and identifies transactions that appear significantly different from normal transaction behavior.

The system provides a complete end-to-end pipeline:

**Transaction Input → Streamlit Frontend → FastAPI Backend → Preprocessing → Isolation Forest → Fraud/Normal Prediction**

---

## 🎯 Objectives

* Detect potentially fraudulent credit card transactions
* Handle highly imbalanced transaction data
* Compare multiple anomaly detection techniques
* Tune the Isolation Forest contamination parameter
* Serialize the trained model and preprocessing scaler
* Build a REST API for real-time predictions
* Build an interactive Streamlit frontend
* Deploy the application to the cloud
* Provide a complete end-to-end AI deployment workflow

---

## 🧠 Machine Learning Approach

### 1. Isolation Forest

Isolation Forest is an unsupervised anomaly detection algorithm.

It identifies unusual observations by isolating them using randomly selected features and split values.

The final deployed configuration is:

* **Algorithm:** Isolation Forest
* **Number of estimators:** 100
* **Contamination:** 0.005
* **Random state:** 42

The model predicts:

* `1` → Normal transaction
* `-1` → Anomalous/Fraud transaction

---

### 2. Local Outlier Factor (LOF)

Local Outlier Factor was also evaluated as an alternative anomaly detection method.

LOF identifies observations located in regions with significantly lower local density compared with their neighboring observations.

---

## 🔧 Data Preprocessing

The dataset contains:

* `Time`
* `V1` to `V28`
* `Amount`
* `Class`

`V1` to `V28` are anonymized numerical features obtained from a PCA transformation of the original transaction data.

The `Class` column represents the original target:

* `0` → Normal
* `1` → Fraud

The `Class` column is used for evaluation and is **not provided to the model during prediction**.

### Robust Scaling

The `Amount` feature is transformed using `RobustScaler`.

RobustScaler was selected because it is less sensitive to extreme values and outliers.

The trained scaler is saved as:

```text
models/robust_scaler.pkl
```

---

## 📊 Dataset

The project uses the classic Credit Card Fraud Detection dataset.

Dataset characteristics:

* **Transactions:** 284,807
* **Features:** 30 input features
* **Fraudulent transactions:** 492
* **Normal transactions:** 284,315

The dataset is highly imbalanced, making Precision, Recall and F1-Score important evaluation metrics.

The original dataset is **not included in this GitHub repository** because of its large file size.

It should be placed locally at:

```text
data/creditcard.csv
```

---

## 📈 Model Evaluation

### Initial Model Comparison

| Model                | Precision | Recall | F1-Score |
| -------------------- | --------: | -----: | -------: |
| Isolation Forest     |    0.0879 | 0.5569 |   0.1518 |
| Local Outlier Factor |    0.0575 | 0.3171 |   0.0973 |

These results were obtained during the initial model comparison.

---

## 🎛️ Contamination Tuning

Several contamination values were tested using Isolation Forest.

The final selected configuration from the tested values was:

| Parameter            | Value            |
| -------------------- | ---------------- |
| Model                | Isolation Forest |
| Contamination        | 0.005            |
| Precision            | 0.1276           |
| Recall               | 0.4228           |
| F1-Score             | 0.1960           |
| Number of estimators | 100              |
| Random state         | 42               |

The `0.005` contamination configuration produced the highest F1-score among the tested configurations.

This configuration is the one used by the deployed application.

---

## 🌐 Application Architecture

```text
                    ┌──────────────────────┐
                    │   Streamlit Frontend │
                    │     User Interface   │
                    └──────────┬───────────┘
                               │
                               │ HTTP POST
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │      /predict        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    RobustScaler      │
                    │  Amount Preprocessing │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Isolation Forest   │
                    │   Fraud Detection    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Fraud / Normal     │
                    │      Prediction      │
                    └──────────────────────┘
```

---

## 🖥️ Frontend

The frontend is built using **Streamlit**.

Users can enter the transaction features:

* Time
* V1–V28
* Transaction Amount

The frontend sends the transaction data to the FastAPI backend and displays the prediction.

Possible results:

### Normal

```text
✅ TRANSACTION APPEARS NORMAL
```

### Fraud

```text
🚨 FRAUDULENT TRANSACTION DETECTED
```

---

## ⚡ Backend API

The backend is implemented using **FastAPI**.

### Health Check

```http
GET /health
```

Returns the API health status and deployed model configuration.

### Prediction

```http
POST /predict
```

Accepts transaction features and returns the model prediction.

Example response:

```json
{
    "prediction": "Fraud",
    "model": "Isolation Forest"
}
```

Interactive API documentation is available at:

https://securepay-fraud-api.onrender.com/docs

---

## 💾 Model Serialization

The trained machine learning components are serialized using `joblib`.

### Saved Model

```text
models/isolation_forest_model.pkl
```

### Saved Scaler

```text
models/robust_scaler.pkl
```

The FastAPI application loads these files when the API starts.

---

## 🐳 Docker Deployment

The FastAPI backend is containerized using Docker.

The Docker image:

* Uses Python 3.11
* Installs dependencies from `requirements.txt`
* Copies the API source code
* Copies the trained model and scaler
* Runs the FastAPI application using Uvicorn

---

## ☁️ Cloud Deployment

### Backend

The FastAPI backend is deployed using **Render**.

Live API:

https://securepay-fraud-api.onrender.com

### Frontend

The Streamlit frontend is deployed using **Streamlit Community Cloud**.

Live application:

https://securepayfrauddetection-kzgdjgjgwx8e7we92a9uk.streamlit.app

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Jupyter Notebook
* FastAPI
* Uvicorn
* Pydantic
* Streamlit
* Requests
* Docker
* Git
* GitHub
* Render
* Streamlit Community Cloud

---

## 📁 Project Structure

```text
SecurePay_Fraud_Detection/
│
├── data/
│   └── creditcard.csv
│
├── models/
│   ├── isolation_forest_model.pkl
│   └── robust_scaler.pkl
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── results/
│   ├── metrics/
│   └── plots/
│
├── src/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── SecurePay_Fraud_Detection_Presentation.pptx
└── SecurePay_Fraud_Detection_Project_Report.docx
```

> **Note:** `data/creditcard.csv` is excluded from GitHub because of its large size.

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/krjnanasagar-arch/SecurePay_Fraud_Detection.git
cd SecurePay_Fraud_Detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start FastAPI

```bash
python -m uvicorn src.main:app --reload
```

FastAPI will run at:

```text
http://127.0.0.1:8000
```

### 6. Start Streamlit

Open another terminal with the virtual environment activated:

```bash
python -m streamlit run frontend/app.py
```

Streamlit will run at:

```text
http://localhost:8501
```

---

## 🔬 Testing

The deployed application was tested using both normal and fraudulent transaction examples from the dataset.

### Normal Transaction

The system returned:

```text
✅ TRANSACTION APPEARS NORMAL
```

### Fraudulent Transaction

A known fraudulent transaction detected as an anomaly by the final Isolation Forest model returned:

```text
🚨 FRAUDULENT TRANSACTION DETECTED
```

This confirms that the complete frontend-to-backend prediction pipeline is functioning.

---

## 📌 Important Note

SecurePay is an academic/project demonstration of anomaly-based fraud detection.

The model's predictions should not be treated as definitive proof that a real-world transaction is fraudulent. Production financial systems would typically require additional validation, monitoring, threshold tuning, and domain-specific security controls.

---

## 👨‍💻 Project

**SecurePay – AI-Based Credit Card Fraud Detection**

Built as an end-to-end machine learning deployment project covering:

**Data → EDA → Preprocessing → Model Training → Evaluation → Model Serialization → API → Frontend → Docker → Cloud Deployment**
