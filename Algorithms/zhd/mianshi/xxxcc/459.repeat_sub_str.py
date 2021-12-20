
def reapet_s_s(str):
    n = len(str)
    ans = False
    for i in range(1, n):
        sub_str = str[:i]
        n_sub = len(sub_str)
        if n%n_sub == 0:
            count = 0
            for j in range(i, n):
                if str[j*n_sub:j*n_sub+n_sub] == sub_str:
                    count += 1
                else:
                    break
            if count == n/n_sub:
                ans = True
    return ans

str = "ababa"
print(reapet_s_s(str))


