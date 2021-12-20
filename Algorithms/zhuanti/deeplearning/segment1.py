import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Net(nn.Module):
    def __init__(self, input_ch, output_ch):
        super(Net, self).__init__()
        self.conv_down1 = nn.Conv2d(input_ch, 16, kernel_size=3, stride=2, padding=1)
        self.bn_down1 = nn.BatchNorm2d(16)
        self.conv_down2 = nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1)
        self.bn_down2 = nn.BatchNorm2d(32)
        self.conv_up1 = nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.bn_up1 = nn.BatchNorm2d(16+16)
        self.conv_up2 = nn.ConvTranspose2d(16+16, 8, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.bn_up2 = nn.BatchNorm2d(8+3)
        self.output = nn.Conv2d(8+3, output_ch, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        down1 = F.relu(self.conv_down1(x))
        down2 = F.relu(self.conv_down2(self.bn_down1(down1)))
        up1 = F.relu(self.conv_up1(self.bn_down2(down2)))
        print(up1.shape, down2.shape)
        up2 = F.relu(self.conv_up2(self.bn_up1(torch.cat([up1, down1], dim=1))))
        output = self.output(self.bn_up2(torch.cat([up2, x], dim=1)))
        return output

if __name__ == '__main__':
    a = torch.from_numpy(np.random.rand(2, 3, 32, 32))
    print(a.shape)
    net = Net(input_ch=3, output_ch=2)
    output = net(a.to(torch.float))
    print(output.shape)
