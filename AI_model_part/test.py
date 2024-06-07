import torch
import argparse
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import transforms
from model2 import *
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.nn import CrossEntropyLoss
from dataset import *
def train_model(model, trainloader, validloader, criterion, optimizer, scheduler,device, epochs=100, save_path='FER_trained_model.pt', save_best_only=True):
    best_val_loss = float('inf')

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for images, labels in trainloader:            
            images = images.to(device)
            labels = labels.to(device)  # 데이터를 GPU로 전송
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        val_loss = 0
        model.eval()
        with torch.no_grad():
            for images, labels in validloader:           
                images = images.to(device)
                labels = labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
        
        print(f'Epoch {epoch+1}, Train Loss: {total_loss / len(trainloader)}, Val Loss: {val_loss / len(validloader)}')
        scheduler.step(val_loss)  # 학습률 스케줄러 업데이트

        if save_best_only and val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), save_path)
            print(f'Model improved and saved to {save_path}')

# 위에서 정의한 get_sample_dataloaders 함수를 사용

def get_sample_dataloaders(base_dir, batch_size=32, sample_size=100):
    # transform = transforms.Compose([
    #     transforms.Resize((224, 224)),
    #     transforms.ToTensor(),
    #     transforms.Normalize(mean=[0.5], std=[0.5])  # Adjust this if you are using grayscale or RGB images
    # ])
    train_transforms = transforms.Compose([
    transforms.RandomResizedCrop(224),  # 랜덤 크롭 후 224x224로 크기 조정
    transforms.ToTensor(),  # 이미지를 텐서로 변환
    transforms.Normalize(mean=[0.5], std=[0.5])  # 정규화 (흑백 이미지용 평균 및 표준편차)
])
    test_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),  # 테스트 이미지는 중앙에서 224x224로 크롭
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])  # 정규화 (흑백 이미지용 평균 및 표준편차)
])

    train_dataset = EmotionDataset('Training', base_dir, transform=train_transforms)
    val_dataset = EmotionDataset('Validation', base_dir, transform=test_transforms)

    # 데이터셋에서 첫 sample_size 개의 샘플을 선택
    indices = range(sample_size)  # 상위 100개 샘플의 인덱스
    train_subset = torch.utils.data.Subset(train_dataset, indices=indices)
    val_subset = torch.utils.data.Subset(val_dataset, indices=indices)

    train_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_subset, batch_size=batch_size, shuffle=False, num_workers=4)

    return train_loader, val_loader

def main():
    # 매개변수 설정
    parser = argparse.ArgumentParser(description="Train a face emotion recognition model on a sample of the data.")
    parser.add_argument('--epochs', type=int, default=5, help='Number of epochs to train')
    parser.add_argument('--lr', type=float, default=0.001, help='Learning rate')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    parser.add_argument('--save_path', type=str, default='FER_trained_model.pt', help='Path to save the trained model')
    parser.add_argument('--save_best_only', type=bool, default=True, help='Save only when the model improves')
    parser.add_argument('--base_dir', type=str, default=r'C:\Users\User\Desktop\Testdataset', help='Base directory where the data is stored')
    parser.add_argument('--sample_size', type=int, default=100, help='Sample size of the data to train on')
    
    args = parser.parse_args()

    # 데이터 로더 준비
    train_loader, val_loader = get_sample_dataloaders(args.base_dir, args.batch_size, args.sample_size)

    # GPU 사용 가능 여부를 확인하고, 가능하면 GPU를 사용하도록 설정
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print('Using {} device'.format(device))

    # 모델 초기화
    model = ResNet50().to(device)

    # 손실 함수 및 최적화 알고리즘 설정
    criterion = CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=args.lr)
    scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10)

    # 훈련 시작
    train_model(model, train_loader, val_loader, criterion, optimizer, scheduler, device, args.epochs, args.save_path, args.save_best_only)

if __name__ == '__main__':
    main()



