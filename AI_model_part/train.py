import torch
import torch.nn as nn
from torch.optim import Adam
import argparse
from dataset import *
from model import Face_Emotion_CNN  # Importing the Face_Emotion_CNN model
from torch.optim.lr_scheduler import ReduceLROnPlateau

def train_model(model, trainloader, validloader, criterion, optimizer, scheduler, device, epochs=100, save_path='FER_trained_model.pt', save_best_only=True):
    best_val_loss = float('inf')

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for images, labels in trainloader:
            images = images.to(device)
            labels = labels.to(device)
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
        scheduler.step(val_loss)

        if save_best_only and val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), save_path)
            print(f'Model improved and saved to {save_path}')

def get_dataloaders(base_dir, batch_size=32):
    train_dataset = EmotionDataset('Training', base_dir, transform=transform)
    val_dataset = EmotionDataset('Validation', base_dir, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    
    return train_loader, val_loader

def main():
    parser = argparse.ArgumentParser(description="Train a face emotion recognition model.")
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs to train')
    parser.add_argument('--lr', type=float, default=0.001, help='Learning rate')
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size for training')
    parser.add_argument('--save_path', type=str, default='FER_trained_model.pt', help='Path to save the trained model')
    parser.add_argument('--save_best_only', type=bool, default=True, help='Save only when the model improves')
    parser.add_argument('--base_dir', type=str, default=r'D:\다운로드\com_capstone\de_gray1', help='Base directory where the data is stored')
    args = parser.parse_args()
    train_loader, val_loader = get_dataloaders(args.base_dir, args.batch_size)
    
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print('Using {} device'.format(device))
    model = Face_Emotion_CNN().to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=args.lr)
    scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10)

    train_model(model, train_loader, val_loader, criterion, optimizer, scheduler, device, epochs=args.epochs, save_path=args.save_path, save_best_only=args.save_best_only)

if __name__ == '__main__':
    main()
