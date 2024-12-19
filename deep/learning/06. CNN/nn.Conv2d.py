import torch
import torch.nn as nn

# conv1 레이어: 6개의 특징 맵 출력
conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=0)

# pool1 레이어: 6개의 특징 맵 출력
pool1 = nn.Conv2d(in_channels=6, out_channels=6, kernel_size=2, stride=2, padding=0)

# conv2 레이어: 16개의 특징 맵 출력
conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0)

# pool2 레이어: 16개의 특징 맵 출력
pool2 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=2, stride=2, padding=0)

# conv3 레이어: 120개의 특징 맵 출력
conv3 = nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5, stride=1, padding=0)

# 입력 텐서 생성 (예: 1개의 채널을 가진 32x32 이미지)
input_tensor = torch.randn(size=(1, 1, 32, 32))

# 연산 수행
output_tensor1 = conv1(input_tensor)
output_tensor2 = pool1(output_tensor1)
output_tensor3 = conv2(output_tensor2)
output_tensor4 = pool2(output_tensor3)
output_tensor5 = conv3(output_tensor4)

print(f"conv1 Output Size: {output_tensor1.shape}")  # conv1 출력 크기
print(f"pool1 Output Size: {output_tensor2.shape}")  # pool1 출력 크기
print(f"conv2 Output Size: {output_tensor3.shape}")  # conv2 출력 크기
print(f"pool2 Output Size: {output_tensor4.shape}")  # pool2 출력 크기
print(f"conv3 Output Size: {output_tensor5.shape}")  # conv3 출력 크기