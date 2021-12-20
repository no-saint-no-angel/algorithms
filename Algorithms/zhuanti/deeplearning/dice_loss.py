import numpy as np
import torch


def dice_coe(pred, gt, eps):
    N = gt.size(0)
    # N = 10
    print(N)
    pred_flat = pred.view(N, -1)
    gt_flat = gt.view(N, -1)
    # gt_flat_ = gt.view(-1)

    tp = torch.sum(gt_flat*pred_flat, dim=1)
    fp = torch.sum(pred_flat, dim=1) - tp
    fn = torch.sum(gt_flat, dim=1) - tp

    dice = (2*tp + eps)/(2*tp + fp + fn)
    iou = (tp + eps)/(tp + fp + fn)

    return dice

def dice_coe_np(pred, gt, eps):
    N = gt.shape[0]
    # N = 10
    print(N)
    # pred_flat = pred.flatten(order='A')
    # gt_flat = gt.flatten()
    pred_flat = pred.reshape(N, gt.shape[1]*gt.shape[2])
    gt_flat = gt.reshape(N, gt.shape[1]*gt.shape[2])

    # gt_flat_ = gt.view(-1)

    tp = np.sum(gt_flat*pred_flat, axis=1)
    fp = np.sum(pred_flat, axis=1) - tp
    fn = np.sum(gt_flat, axis=1) - tp

    dice = (2*tp + eps)/(2*tp + fp + fn)
    iou = (tp + eps)/(tp + fp + fn)

    return dice

if __name__ == '__main__':
    pred = [[[1,0,1,1,1],
            [1,1,1,1,1]],[[1,0,1,1,1],
            [1,1,1,1,1]]]
    gt = [[[1,0,0,1,1],
          [0,0,0,1,0]],[[1,0,1,1,1],
            [1,1,1,1,1]]]
    eps = 1e-6
    # np方法
    print(dice_coe_np(np.array(pred), np.array(gt), eps))
    # # torch方法
    pred = torch.from_numpy(np.array(pred))
    gt = torch.from_numpy(np.array(gt))
    print(dice_coe(pred.to(torch.float), gt.to(torch.float), eps))