#데이터베이스 파일입니다. 아래 보이는 수많은 흔적들이 있습니다. 주석은 지우셔도 무방합니다.
import os
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

class EmotionDataset(Dataset):
    def __init__(self, category, base_dir, transform=None):
        self.category = category
        self.base_dir = base_dir
        self.transform = transform
        self.data = []
        self.label_map = {'anger': 0, 'anxiety': 1, 'happy': 2, 'sadness': 3, 'neutral': 4}
        self.load_data()

    def load_data(self):
        emotions = ['anger', 'anxiety', 'happy', 'sadness', 'neutral']
        for emotion in emotions:
            path = os.path.join(self.base_dir, self.category, emotion)
            print(f"Loading data from: {path}")  # 디버깅 정보 출력
            if not os.path.exists(path):
                print(f"Path does not exist: {path}")
                continue  # 해당 경로가 없으면 다음 감정으로 넘어갑니다.
            for filename in os.listdir(path):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    image_path = os.path.join(path, filename)
                    image = Image.open(image_path)
                    label = self.label_map[emotion]
                    if self.transform:
                        image = self.transform(image)
                    self.data.append((image, label))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
    
# 사용 예시
base_dir = r"C:\Users\User\Desktop\detect_gray"  # 경로 수정
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])



# ver3.0
# import json
# import os
# import cv2
# import numpy as np
# import torch
# from sklearn.model_selection import train_test_split
# from torch.utils.data import Dataset, DataLoader
# from torchvision import transforms
# from PIL import Image

# emotion_dict = {0: 'anger', 1: 'anxiety', 2: 'happy', 3: 'sadness', 4: 'neutral'}
# base_dir = r"D:\다운로드\com_capstone"
# categories = ['Training', 'Validation']

# def load_data(category, emotion):
#     if category == 'Training':
#         json_filename = 'img_emotion_training_data.json'
#     elif category == 'Validation':
#         json_filename = 'img_emotion_validation_data.json'
#     else:
#         raise ValueError("Unknown category: " + category)

#     json_path = os.path.join(str(base_dir), str(category), str(emotion), str(json_filename))  # 모든 인자를 문자열로 변환
#     with open(json_path, 'r') as file:
#         data = json.load(file)

#     faces = []
#     labels = []

#     for item in data:
#         image_path = os.path.join(base_dir, category, emotion, item['filename'])
#         image = cv2.imread(image_path)
#         if image is None:
#             print(f"Warning: Image {image_path} not found.")
#             continue

#         box = item['annot_A']['boxes']
#         face = image[int(box['minY']):int(box['maxY']), int(box['minX']):int(box['maxX'])]
#         face = cv2.resize(face, (48, 48))

#         faces.append(face.astype('float32'))
#         labels.append(emotion)
#     return np.array(faces), np.array(labels)

# class EmotionDataset(Dataset):
#     def __init__(self, data, labels, transform=None):
#         self.data = data
#         self.labels = labels
#         self.transform = transform

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         x = self.data[idx]
#         x = Image.fromarray(x)
#         if self.transform:
#             x = self.transform(x)
#         y = self.labels[idx]
#         return x, y

# def get_dataloaders(base_dir, categories, batch_size=32):
#     all_data = {}
#     for category in categories:
#         data, labels = [], []
#         for emotion_name in emotion_dict.values():  # 감정 이름을 직접 사용
#             faces, label = load_data(category, emotion_name)
#             data.extend(faces)
#             labels.extend(label)
#         data, labels = np.array(data), np.array(labels)
#         X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

#         train_transform = transforms.Compose([
#             transforms.RandomHorizontalFlip(),
#             transforms.RandomRotation(30),
#             transforms.ToTensor(),
#             transforms.Normalize(mean=[0.485], std=[0.229])
#         ])
#         val_transform = transforms.Compose([
#             transforms.ToTensor(),
#             transforms.Normalize(mean=[0.485], std=[0.229])
#         ])

#         train_dataset = EmotionDataset(X_train, y_train, train_transform)
#         val_dataset = EmotionDataset(X_val, y_val, val_transform)

#         train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
#         val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

#     return train_loader, val_loader

# ver2.0
# def load_all_data(base_dir, categories):
#     all_data = {}
#     for category in categories:
#         category_data = {}
#         for emotion in emotion_dict.values():
#             faces, labels = load_data(category, emotion)
#             category_data[emotion] = (faces, labels)
#         all_data[category] = category_data
#     return all_data

# class EmotionDataset(Dataset):
#     def __init__(self, data, labels, transform=None):
#         self.data = data
#         self.labels = labels
#         self.transform = transform

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         x = self.data[idx]
#         x = Image.fromarray(x)
#         if self.transform:
#             x = self.transform(x)
#         y = self.labels[idx]
#         return x, y

# # 데이터 변환
# transform = transforms.Compose([
#     transforms.ToPILImage(),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# ])

# # 데이터셋과 DataLoader 생성
# all_data = load_all_data(base_dir, categories)
# train_dataset = EmotionDataset(all_data['Training'][0], all_data['Training'][1], transform=transform)
# val_dataset = EmotionDataset(all_data['Validation'][0], all_data['Validation'][1], transform=transform)
# train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
# val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)


# import cv2
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# import torch.utils.data as utils
# import torch
# import torch.nn as nn
# from torchvision import transforms
# from PIL import Image


# emotion_dict = {0: 'angry', 1: 'anxiety', 2: 'happy',
#                 3: 'sadness', 4: 'neutral'}


# def load_fer2013(path_to_fer_csv):
#     data = pd.read_csv(path_to_fer_csv)
#     pixels = data['pixels'].tolist()
#     width, height = 48, 48
#     faces = []
#     for pixel_sequence in pixels:
#         face = [int(pixel) for pixel in pixel_sequence.split(' ')]
#         face = np.asarray(face).reshape(width, height)
#         face = cv2.resize(face.astype('uint8'), (48,48))
#         faces.append(face.astype('float32'))
#     faces = np.asarray(faces)
#     faces = np.expand_dims(faces, -1)
#     emotions = data['emotion'].values
#     return faces, emotions


# def show_random_data(faces, emotions):
#   idx = np.random.randint(len(faces))
#   print(emotion_dict[emotions[idx]])
#   plt.imshow(faces[idx].reshape(48,48), cmap='gray')
#   plt.show()

# class EmotionDataset(utils.Dataset):
#     def __init__(self, X, y, transform=None):
#         self.X = X
#         self.y = y
#         self.transform = transform
        
#     def __len__(self):
#         return len(self.X)
    
#     def __getitem__(self, index):
#         x = self.X[index].reshape(48,48)
#         x = Image.fromarray((x))
#         if self.transform is not None:
#             x = self.transform(x)
#         y = self.y[index]
#         return x, y


# def get_dataloaders(path_to_fer_csv='', tr_batch_sz=3000, val_batch_sz=500):
#     faces, emotions = load_fer2013(path_to_fer_csv)
#     train_X, val_X, train_y, val_y = train_test_split(faces, emotions, test_size=0.2,
#                                                 random_state = 1, shuffle=True)
#     train_transform = transforms.Compose([
#                         transforms.RandomHorizontalFlip(),
#                         transforms.RandomRotation(30),
#                         transforms.ToTensor(),
#                         transforms.Normalize((0.507395516207, ),(0.255128989415, )) 
#                         ])
#     val_transform = transforms.Compose([
#                     transforms.ToTensor(),
#                     transforms.Normalize((0.507395516207, ),(0.255128989415, ))
#                     ])  

#     train_dataset = EmotionDataset(train_X, train_y, train_transform)
#     val_dataset = EmotionDataset(val_X, val_y, val_transform)

#     trainloader = utils.DataLoader(train_dataset, tr_batch_sz)
#     validloader = utils.DataLoader(val_dataset, val_batch_sz)
