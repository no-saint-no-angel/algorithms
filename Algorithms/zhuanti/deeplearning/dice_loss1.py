import torch
import numpy as np


def dice_coe(pred, gt, eps):
    N = gt.size(0)
    pred_flat = pred.view(N, -1)
    gt_flat = gt.view(N, -1)

    tp = torch.sum(gt_flat*pred_flat, dim=1)
    fp = torch.sum(pred_flat, dim=1) - tp
    fn = torch.sum(gt_flat, dim=1) - tp

    dice = (2*tp + eps)/(2*tp + fp + fn + eps)
    iou = (tp + eps)/(tp + fp + fn + eps)
    return dice

def dice_loss_np(pred, gt, eps):
    N = gt.shape[0]
    pred_flat = pred.reshape(N, gt.shape[1]*gt.shape[2])
    gt_flat = gt.reshape(N, gt.shape[1]*gt.shape[2])

    tp = np.sum(pred_flat*gt_flat, axis=1)
    fp = np.sum(pred_flat, axis=1) - tp
    fn = np.sum(gt_flat, axis=1) - tp

    dice = (2*tp + eps)/(2*tp + fp + fn + eps)
    iou = (tp + eps)/(tp + fp + fn + eps)
    return dice

if __name__ == '__main__':
    pred = [[[1,0,1,0],[0,0,1,0]],
            [[1,0,1,0],[1,0,1,0]]]

    gt = [[[0,0,0,0],[1,1,1,1]],
            [[1,0,1,0],[1,1,1,0]]]
    eps = 1e-5
    # # torch
    # pred_tensor = torch.from_numpy(np.array(pred))
    # gt_tensor = torch.from_numpy(np.array(gt))
    # print(gt_tensor.shape)
    #
    # dice = dice_coe(pred_tensor.to(torch.float), gt_tensor.to(torch.float), eps)
    # print(dice)

    # np
    pred_array = np.array(pred)
    gt_array = np.array(gt)

    dice = dice_loss_np(pred_array, gt_array, eps)
    print(dice)

