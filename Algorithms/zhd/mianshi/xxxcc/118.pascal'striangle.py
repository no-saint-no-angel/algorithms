

def generate(numRows):
    ans = list()
    for i in range(numRows):
        tmp_3 = list()
        for j in range(i+1):
            if j == 0 or j == i:
                tmp_3.append(1)
            else:
                tmp_3.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(tmp_3)
    return ans

print(generate(5))


