import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "resnet50_ocean_life.h5")
LABEL_PATH = os.path.join(BASE_DIR, "models", "class_labels.json")

IMG_SIZE = 224
