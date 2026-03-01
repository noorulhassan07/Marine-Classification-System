import requests

BACKEND_URL = "http://backend:5000/predict"

def classify_image(uploaded_file):
    files = {
        "image": uploaded_file.getvalue()
    }

    response = requests.post(BACKEND_URL, files=files, timeout=10)

    if response.status_code != 200:
        raise Exception("Backend error")

    return response.json()
