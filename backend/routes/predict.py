from flask import Blueprint, request, jsonify
from services.inference import predict

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict_route():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_bytes = request.files["image"].read()
    result = predict(image_bytes)
    return jsonify(result)
