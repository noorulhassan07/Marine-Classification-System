import json
import numpy as np
import tensorflow as tf
from config import MODEL_PATH, LABEL_PATH
from utils.image_utils import preprocess_image

model = tf.keras.models.load_model(MODEL_PATH)

with open(LABEL_PATH, "r") as f:
    class_labels = json.load(f)

class_names = [class_labels[str(i)] for i in range(len(class_labels))]

def predict(image_bytes):
    img = preprocess_image(image_bytes)
    preds = model.predict(img)
    idx = np.argmax(preds)

    return {
        "class": class_names[idx],           
        "confidence": float(np.max(preds))  
    }
