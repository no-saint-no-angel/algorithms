import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class Net(nn.Module):
    def __init__(self, input_ch, output_ch):
        super(Net, self).__init__()
        self.conv_down1 = nn.Conv2d(input_ch, 32, kernel_size=3, stride=2, padding=1)
        self.conv_down2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.conv_up1 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.conv_up2 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.conv_out = nn.Conv2d(35, output_ch, kernel_size=3, stride=1, padding=1)
    def forward(self, x):
        print(x.shape)
        # downsample
        down1 = F.relu(self.conv_down1(x))
        print(down1.shape)
        down2 = F.relu(self.conv_down2(down1))
        # upsample
        up1 = F.relu(self.conv_up1(down2))
        print(up1.shape)
        up2 = F.relu(self.conv_up2(torch.cat([up1, down1], dim=1)))
        print(up2.shape)
        # output
        output = torch.softmax(self.conv_out(torch.cat([up2, x], dim=1)), dim=1)

        return output


if __name__ == '__main__':
    input = torch.from_numpy(np.random.rand(2, 3, 32, 32))
    # print(input.shape)
    net = Net(input_ch=3, output_ch=2)
    print(net)
    output = net(input.to(torch.float))
    print(output)
    print(output.shape)


