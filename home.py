import streamlit as st

def home():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .centered-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown("<div class='subtitle'>Protecting transactions with real-time fraud analysis</div>", unsafe_allow_html=True)

    # Optional: Add a logo (uncomment and provide the path if needed)
    # st.image("your_logo.png", width=150)

    # Description section
    st.markdown("### 🔍 About the Project")
    st.write("""
    This project uses machine learning algorithms to detect fraudulent credit card transactions in real-time.
    The model has been trained on anonymized credit card transaction data to identify patterns of fraud.

    **Features:**
    - Real-time transaction CSV data
    - Detect fraud predictions
    - Visualizations of fraudulent vs non-fraudulent patterns
    - Login page for Users
    """)
