import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Net(nn.Module):
    def __init__(self, input_size, num_class):
        super(Net, self).__init__()
        self.input_ch = input_size
        self.conv1 = nn.Conv2d(self.input_ch, 64, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(64, 8, kernel_size=3, stride=2, padding=1)
        self.fc1 = nn.Linear(512, 256)
        self.fc2 = nn.Linear(256, num_class)
    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = x.view(-1, 512)
        x = torch.relu(self.fc1(x))
        y_hat = self.fc2(x)
        return torch.softmax(y_hat, dim=1)

if __name__ == '__main__':

    # input_array = np.random.randint(0, 5,size=(1, 3, 32, 32))
    input_array = np.random.rand(1, 3, 32, 32)
    input_array = torch.from_numpy(input_array)
    net = Net(input_size=3, num_class=3)
    print(net)
    output = net(input_array.to(torch.float))
    print(output)
    # loss_function = nn.CrossEntropyLoss()
    # optimizer = torch.optim.Adam(net.parameters(), lr=0.0001)

