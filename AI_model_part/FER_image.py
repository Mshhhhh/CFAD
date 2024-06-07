import os
import cv2
import torch
import torchvision.transforms as transforms
import pandas as pd
from deepface import DeepFace
from model import *
import shutil
import tempfile

def load_trained_model(model_path):
    model = Face_Emotion_CNN()
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')), strict=False)
    return model

def FER_image(img_path, results):
    model = load_trained_model('FER_trained_model.pt')
    emotion_dict = {'anger': 0, 'anxiety': 1, 'happy': 2, 'sadness': 3, 'neutral': 4}

    val_transform = transforms.Compose([
        transforms.ToTensor()])

    img = cv2.imread(img_path)
    if img is None:
        print(f"Image {img_path} not found.")
        return

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary path within the directory
        temp_img_path = os.path.join(temp_dir, 'temp_img.png')
        shutil.copy(img_path, temp_img_path)
        
        # Using DeepFace to detect and extract faces
        detected_faces = DeepFace.extract_faces(temp_img_path, detector_backend='opencv', enforce_detection=False)
    
    if len(detected_faces) == 0:
        print(f"No faces detected in {img_path}")
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

def process_images(directory_path):
    results = []
    for img_name in os.listdir(directory_path):
        img_path = os.path.join(directory_path, img_name)
        if img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            FER_image(img_path, results)

    df = pd.DataFrame(results)
    df.to_csv("emotion_results.csv", index=False)
    print("Results saved to emotion_results.csv")

directory_path = 'D:\\다운로드\\com_capstone\\de_gray1\\검증'

if os.path.isfile(directory_path):
    results = []
    FER_image(directory_path, results)
    df = pd.DataFrame(results)
    df.to_csv("emotion_results.csv", index=False)
    print("Results saved to emotion_results.csv")
elif os.path.isdir(directory_path):
    process_images(directory_path)
else:
    print('The provided path does not exist.')


# import cv2
# import torch
# import torchvision.transforms as transforms
# from PIL import Image
# import matplotlib.pyplot as plt
# import argparse
# import os
# from model import *


# def load_trained_model(model_path):
#     model = Face_Emotion_CNN()
#     model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
#     return model

# def FER_image(img_path):

#     model = load_trained_model('./models/FER_trained_model.pt')
    
#     emotion_dict = {0: 'anger', 1: 'anxiety', 2: 'happy', 3: 'sadness', 4: 'neutral'}

#     val_transform = transforms.Compose([
#         transforms.ToTensor()])


#     img = cv2.imread(img_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
#     faces = face_cascade.detectMultiScale(img)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
#         resize_frame = cv2.resize(gray[y:y + h, x:x + w], (48, 48))
#         X = resize_frame/256
#         X = Image.fromarray((resize_frame))
#         X = val_transform(X).unsqueeze(0)
#         with torch.no_grad():
#             model.eval()
#             log_ps = model.cpu()(X)
#             ps = torch.exp(log_ps)
#             top_p, top_class = ps.topk(1, dim=1)
#             pred = emotion_dict[int(top_class.numpy())]
#         cv2.putText(img, pred, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1)

#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     plt.grid(False)
#     plt.axis('off')
#     plt.show()


# if __name__ == "__main__":

#     ap = argparse.ArgumentParser()
#     ap.add_argument("-p", "--path", required=True,
#         help="path of image")
#     args = vars(ap.parse_args())
    
#     if not os.path.isfile(args['path']):
#         print('The image path does not exists!!')
#     else:
#         print(args['path'])
#         FER_image(args['path'])