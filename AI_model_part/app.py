# 해당 코드는 API를 뜻합니다.
import os
import cv2
import torch
import torchvision.transforms as transforms
import pandas as pd
from deepface import DeepFace
from model import *
import shutil
import tempfile
from flask import Flask, request, jsonify, send_file
import urllib.parse

# Suppress TensorFlow warnings
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)

app = Flask(__name__)

def load_trained_model(model_path):
    model = Face_Emotion_CNN()
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')), strict=False)
    return model

def FER_image(img_path, results):
    model = load_trained_model('FER_trained_model.pt')
    emotion_dict = {'anger': 0, 'anxiety': 1, 'happy': 2, 'sadness': 3, 'neutral': 4}

    val_transform = transforms.Compose([
        transforms.ToTensor()])

    # Convert to absolute path and encode the path
    abs_img_path = os.path.abspath(img_path)
    encoded_img_path = urllib.parse.quote(abs_img_path)
    if not os.path.exists(abs_img_path):
        print(f"Image {abs_img_path} not found.")
        return

    print(f"Processing image: {abs_img_path}")  # Print the image path

    img = cv2.imread(abs_img_path)
    if img is None:
        print(f"Image {abs_img_path} not found or could not be opened.")
        return

    # Using DeepFace to detect and extract faces
    detected_faces = DeepFace.extract_faces(abs_img_path, detector_backend='opencv', enforce_detection=False)
    
    if len(detected_faces) == 0:
        print(f"No faces detected in {abs_img_path}")
        return

    for face in detected_faces:
        face_img = face['face']
        face_img = (face_img * 255).astype('uint8')  # Convert to uint8

        # Check the number of channels
        if len(face_img.shape) == 2 or face_img.shape[2] == 1:
            # Convert 1-channel image to 3-channel
            face_img = cv2.cvtColor(face_img, cv2.COLOR_GRAY2RGB)
        else:
            # Ensure the image is in RGB format
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

        resized_face = cv2.resize(face_img, (224, 224))
        tensor_image = val_transform(resized_face).unsqueeze(0)

        with torch.no_grad():
            model.eval()
            predictions = model(tensor_image)
            top_p, top_class = predictions.topk(1, dim=1)
            predicted_emotion = [key for key, value in emotion_dict.items() if value == int(top_class.numpy())][0]
            results.append({"Image": os.path.basename(img_path), "Emotion": predicted_emotion})

@app.route('/')
def index():
    return "Face Emotion Recognition API"

@app.route('/process_directory', methods=['POST'])
def process_directory():
    if 'directory' not in request.form:
        return jsonify({"error": "No directory path part"}), 400
    directory_path = request.form['directory']
    abs_directory_path = os.path.abspath(directory_path)  # Convert to absolute path
    if not os.path.isdir(abs_directory_path):
        return jsonify({"error": "Invalid directory path"}), 400

    temp_dir = tempfile.mkdtemp()

    results = []
    for img_name in os.listdir(abs_directory_path):
        img_path = os.path.join(abs_directory_path, img_name)
        if img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            FER_image(img_path, results)
    
    # Save results to CSV
    csv_path = os.path.join(temp_dir, 'emotion_results.csv')
    df = pd.DataFrame(results)
    df.to_csv(csv_path, index=False)

    return send_file(csv_path, as_attachment=True, download_name='emotion_results.csv')

if __name__ == '__main__':
    app.run(debug=True)
