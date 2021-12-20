
def findContentChildren(g, s):
    g.sort(reverse=True)
    # s.sort()
    num = 0
    for i, val in enumerate(g):
        for j in enumerate(s):
            if j[1] >= val:
                num += 1
                s.remove(j[1])
                break
    return num
    # while g or s:
    #     if max(s) >= max(g):
    #         num += 1
    #         g.remove(max(g))
    #         s.remove(max(s))


g = [1, 2, 3]
s = [1, 1, 1]
print(findContentChildren(g, s))