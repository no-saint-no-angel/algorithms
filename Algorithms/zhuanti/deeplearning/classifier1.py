import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Net(nn.Module):
    def __init__(self, input_ch, num_classes):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(input_ch, 32, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.fc1 = nn.Linear(1024, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 1024)
        x = F.relu(self.fc1(x))
        y_hat = nn.Softmax(self.fc2(x))
        return y_hat


if __name__ == '__main__':
    a = torch.from_numpy(np.random.rand(2, 3, 16, 16))
    net = Net(input_ch=3, num_classes=3)
    print(net)
    output = net(a.to(torch.float))
    print(output)