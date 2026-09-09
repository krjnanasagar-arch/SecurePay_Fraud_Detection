import streamlit as st
import requests

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SecurePay - Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="title">💳 SecurePay</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Credit Card Fraud Detection System</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# API configuration
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000/predict"

# --------------------------------------------------
# Transaction inputs
# --------------------------------------------------

st.subheader("🔍 Transaction Details")

st.info(
    "Enter the transaction features below. "
    "The AI model will analyze the transaction and classify it as Normal or Fraud."
)

col1, col2, col3 = st.columns(3)

with col1:
    Time = st.number_input("Time", value=0.0)
    V1 = st.number_input("V1", value=0.0)
    V2 = st.number_input("V2", value=0.0)
    V3 = st.number_input("V3", value=0.0)
    V4 = st.number_input("V4", value=0.0)
    V5 = st.number_input("V5", value=0.0)
    V6 = st.number_input("V6", value=0.0)
    V7 = st.number_input("V7", value=0.0)
    V8 = st.number_input("V8", value=0.0)
    V9 = st.number_input("V9", value=0.0)

with col2:
    V10 = st.number_input("V10", value=0.0)
    V11 = st.number_input("V11", value=0.0)
    V12 = st.number_input("V12", value=0.0)
    V13 = st.number_input("V13", value=0.0)
    V14 = st.number_input("V14", value=0.0)
    V15 = st.number_input("V15", value=0.0)
    V16 = st.number_input("V16", value=0.0)
    V17 = st.number_input("V17", value=0.0)
    V18 = st.number_input("V18", value=0.0)
    V19 = st.number_input("V19", value=0.0)

with col3:
    V20 = st.number_input("V20", value=0.0)
    V21 = st.number_input("V21", value=0.0)
    V22 = st.number_input("V22", value=0.0)
    V23 = st.number_input("V23", value=0.0)
    V24 = st.number_input("V24", value=0.0)
    V25 = st.number_input("V25", value=0.0)
    V26 = st.number_input("V26", value=0.0)
    V27 = st.number_input("V27", value=0.0)
    V28 = st.number_input("V28", value=0.0)

st.divider()

amount = st.number_input(
    "💰 Transaction Amount",
    min_value=0.0,
    value=100.0,
    step=10.0
)

# --------------------------------------------------
# Prediction button
# --------------------------------------------------

if st.button("🔎 Check Transaction", use_container_width=True):

    transaction = {
        "Time": Time,
        "V1": V1,
        "V2": V2,
        "V3": V3,
        "V4": V4,
        "V5": V5,
        "V6": V6,
        "V7": V7,
        "V8": V8,
        "V9": V9,
        "V10": V10,
        "V11": V11,
        "V12": V12,
        "V13": V13,
        "V14": V14,
        "V15": V15,
        "V16": V16,
        "V17": V17,
        "V18": V18,
        "V19": V19,
        "V20": V20,
        "V21": V21,
        "V22": V22,
        "V23": V23,
        "V24": V24,
        "V25": V25,
        "V26": V26,
        "V27": V27,
        "V28": V28,
        "Amount": amount
    }

    try:

        with st.spinner("🤖 AI is analyzing the transaction..."):

            response = requests.post(
                API_URL,
                json=transaction
            )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]

            st.divider()

            if prediction == "Fraud":

                st.error(
                    "🚨 FRAUDULENT TRANSACTION DETECTED"
                )

                st.warning(
                    "This transaction has been identified as anomalous "
                    "by the Isolation Forest model."
                )

            else:

                st.success(
                    "✅ TRANSACTION APPEARS NORMAL"
                )

                st.info(
                    "The AI model did not detect an unusual pattern "
                    "in this transaction."
                )

            st.write(
                f"**Model Used:** {result['model']}"
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to the FastAPI server."
        )

        st.info(
            "Make sure FastAPI is running on "
            "http://127.0.0.1:8000"
        )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "SecurePay | AI-Based Credit Card Fraud Detection | "
    "Isolation Forest"
)