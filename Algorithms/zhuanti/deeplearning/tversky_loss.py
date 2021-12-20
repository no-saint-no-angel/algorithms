import torch


def diceCoeff_tversky(pred, gt, eps=1e-5, activation='sigmoid'):
    r""" computational formula：
        dice = (2 * (pred ∩ gt)) / (pred ∪ gt)
    """
    alpha = 0.3
    N = gt.size(0)
    pred_flat = pred.view(N, -1)
    gt_flat = gt.view(N, -1)

    tp = torch.sum(gt_flat * pred_flat, dim=1)
    fp = torch.sum(pred_flat, dim=1) - tp
    fn = torch.sum(gt_flat, dim=1) - tp

    tversky = (tp + eps) / (tp + alpha * fp + (1 - alpha) * fn + eps)
    # intersection = (pred_flat * gt_flat).sum(1)
    # unionset = pred_flat.sum(1) + gt_flat.sum(1)  # 这里的并集是直接相加的，那应该是dice = (2 * (pred ∩ gt)) / (pred + gt)
    # loss = (2 * intersection + eps) / (unionset + eps)

    return tversky.sum() / N