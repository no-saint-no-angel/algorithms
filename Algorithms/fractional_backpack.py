

goods = [(60, 10), (100, 20), (120, 30)]  # 每个商品元组表示（价格，重量）
goods.sort(key=lambda x: x[0] / x[1], reverse=True)  # 按照单位价格排序，


def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w/weight
            w = 0
            break
        total_v += m[i]*prize
        # w -= m[i]*prize
    return m, total_v


print(fractional_backpack(goods, 50))

