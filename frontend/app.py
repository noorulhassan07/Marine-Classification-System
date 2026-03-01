import streamlit as st
import requests
from PIL import Image

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Ocean Life Classification",
    page_icon="🌊",
    layout="centered"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #f5f9fc;
    }
    .main-title {
        text-align: center;
        color: #0b3c5d;
        font-size: 40px;
        font-weight: 700;
    }
    .subtitle {
        text-align: center;
        color: #3282b8;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .upload-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        color: #6c757d;
        font-size: 14px;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Title
# -------------------------------------------------
st.markdown("<div class='main-title'>🌊 Ocean Life Classification</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Powered Marine Species Recognition System</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Upload Section
# -------------------------------------------------
st.markdown("<div class='upload-box'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 Upload an image of a sea animal",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=400)

    if st.button("🔍 Classify Image"):
        with st.spinner("Analyzing marine species..."):
            try:
                # ✅ Send image bytes with key "image" to match backend
                files = {
                    "image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                }

                response = requests.post(
                    "http://backend:5000/predict",  # Docker backend service
                    files=files,
                    timeout=20
                )

                if response.status_code == 200:
                    result = response.json()
                    predicted_class = result["class"]
                    confidence = result["confidence"] * 100  # %
                    st.success("✅ Prediction Successful")
                    st.markdown(
                        f"""
                        ### 🐠 Predicted Species  
                        **{predicted_class}**

                        ### 📊 Confidence  
                        **{confidence:.2f}%**
                        """
                    )
                else:
                    st.error(f"❌ Prediction failed. Backend returned status {response.status_code}")

            except requests.exceptions.RequestException:
                st.error("🚫 Backend is not responding. Please check the Docker container or URL.")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown(
    "<div class='footer'>© 2025 Ocean Life Classification System | AI & Deep Learning</div>",
    unsafe_allow_html=True
)
