# import torch
# import torch.nn as nn

# class Bottleneck(nn.Module):
#     expansion = 4

#     def __init__(self, in_channels, out_channels, stride=1, downsample=None, dropout_prob=0.0):
#         super(Bottleneck, self).__init__()
#         self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False)
#         self.bn1 = nn.BatchNorm2d(out_channels)
#         self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
#         self.bn2 = nn.BatchNorm2d(out_channels)
#         self.conv3 = nn.Conv2d(out_channels, out_channels * self.expansion, kernel_size=1, bias=False)
#         self.bn3 = nn.BatchNorm2d(out_channels * self.expansion)
#         self.relu = nn.ReLU(inplace=True)
#         self.downsample = downsample
#         self.dropout = nn.Dropout2d(dropout_prob)

#     def forward(self, x):
#         identity = x
#         out = self.conv1(x)
#         out = self.bn1(out)
#         out = self.relu(out)
#         out = self.conv2(out)
#         out = self.bn2(out)
#         out = self.relu(out)
#         out = self.dropout(out)
#         out = self.conv3(out)
#         out = self.bn3(out)
#         if self.downsample is not None:
#             identity = self.downsample(x)
#         out += identity
#         out = self.relu(out)
#         return out

# class ResNet50(nn.Module):
#     def __init__(self, num_classes=5, input_channels=1, dropout_prob=0.3):
#         super(ResNet50, self).__init__()
#         self.in_channels = 64
#         self.conv1 = nn.Conv2d(input_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
#         self.bn1 = nn.BatchNorm2d(64)
#         self.relu = nn.ReLU(inplace=True)
#         self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
#         self.layer1 = self._make_layer(64, 3, stride=1, dropout_prob=dropout_prob)
#         self.layer2 = self._make_layer(128, 4, stride=2, dropout_prob=dropout_prob)
#         self.layer3 = self._make_layer(256, 6, stride=2, dropout_prob=dropout_prob)
#         self.layer4 = self._make_layer(512, 3, stride=2, dropout_prob=dropout_prob)
#         self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
#         self.fc = nn.Linear(512 * Bottleneck.expansion, num_classes)  # num_classes를 5로 설정

#     def _make_layer(self, out_channels, blocks, stride, dropout_prob):
#         downsample = None
#         if stride != 1 or self.in_channels != out_channels * Bottleneck.expansion:
#             downsample = nn.Sequential(
#                 nn.Conv2d(self.in_channels, out_channels * Bottleneck.expansion, kernel_size=1, stride=stride, bias=False),
#                 nn.BatchNorm2d(out_channels * Bottleneck.expansion),
#             )
#         layers = []
#         layers.append(Bottleneck(self.in_channels, out_channels, stride, downsample, dropout_prob))
#         self.in_channels = out_channels * Bottleneck.expansion
#         for _ in range(1, blocks):
#             layers.append(Bottleneck(self.in_channels, out_channels, dropout_prob=dropout_prob))
#         return nn.Sequential(*layers)

#     def forward(self, x):
#         x = self.conv1(x)
#         x = self.bn1(x)
#         x = self.relu(x)
#         x = self.maxpool(x)
#         x = self.layer1(x)
#         x = self.layer2(x)
#         x = self.layer3(x)
#         x = self.layer4(x)
#         x = self.avgpool(x)
#         x = torch.flatten(x, 1)
#         x = self.fc(x)
#         return x

#     def adjust_dropout(self, new_dropout_prob):
#         max_dropout_prob = 0.5  # 드롭아웃 확률의 상한 설정
#         min_dropout_prob = 0.1  # 드롭아웃 확률의 하한 설정
#         if new_dropout_prob > max_dropout_prob:
#             new_dropout_prob = max_dropout_prob
#         elif new_dropout_prob < min_dropout_prob:
#             new_dropout_prob = min_dropout_prob
#         for layer in [self.layer1, self.layer2, self.layer3, self.layer4]:
#             for block in layer:
#                 block.dropout.p = new_dropout_prob

import torch.nn as nn
import torch

class Face_Emotion_CNN(nn.Module):
  def __init__(self):
    super(Face_Emotion_CNN, self).__init__()
    self.cnn1 = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3)
    self.cnn2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3)
    self.cnn3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3)
    self.cnn4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
    self.cnn5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)
    self.cnn6 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3)
    self.cnn7 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3)
    self.relu = nn.ReLU()
    self.pool1 = nn.MaxPool2d(2, 1)
    self.pool2 = nn.MaxPool2d(2, 2)
    self.cnn1_bn = nn.BatchNorm2d(8)
    self.cnn2_bn = nn.BatchNorm2d(16)
    self.cnn3_bn = nn.BatchNorm2d(32)
    self.cnn4_bn = nn.BatchNorm2d(64)
    self.cnn5_bn = nn.BatchNorm2d(128)
    self.cnn6_bn = nn.BatchNorm2d(256)
    self.cnn7_bn = nn.BatchNorm2d(256)
    self.fc1 = nn.Linear(147456, 512)
    self.fc2 = nn.Linear(512, 256)
    self.fc3 = nn.Linear(256, 5)  # Changed to 5 classes
    self.dropout = nn.Dropout(0.3)
    self.log_softmax = nn.LogSoftmax(dim=1)
    
  def forward(self, x):
    x = self.relu(self.pool1(self.cnn1_bn(self.cnn1(x))))
    x = self.relu(self.pool1(self.cnn2_bn(self.dropout(self.cnn2(x)))))
    x = self.relu(self.pool1(self.cnn3_bn(self.cnn3(x))))
    x = self.relu(self.pool1(self.cnn4_bn(self.dropout(self.cnn4(x)))))
    x = self.relu(self.pool2(self.cnn5_bn(self.cnn5(x))))
    x = self.relu(self.pool2(self.cnn6_bn(self.dropout(self.cnn6(x)))))
    x = self.relu(self.pool2(self.cnn7_bn(self.dropout(self.cnn7(x)))))
    
    x = x.view(x.size(0), -1)
    
    x = self.relu(self.dropout(self.fc1(x)))
    x = self.relu(self.dropout(self.fc2(x)))
    x = self.log_softmax(self.fc3(x))
    return x

  def count_parameters(self):
    return sum(p.numel() for p in self.parameters() if p.requires_grad)

if __name__ == '__main__':
    bn_model = Face_Emotion_CNN()
    x = torch.randn(1, 3, 48, 48)
    print('Shape of output = ', bn_model(x).shape)
    print('No of Parameters of the BatchNorm-CNN Model =', bn_model.count_parameters())
