
def s_s_a(nums):
    n = len(nums)
    negtive = -1
    for i, num in enumerate(nums):
        if num < 0:
            negtive = i
        else:
            break
    i, j = negtive, negtive + 1
    ans = []
    while i >= 0 or j < n:
        if i < 0:
            ans.append(nums[j]*nums[j])
            j += 1
        elif j > n:
            ans.append(nums[i]*nums[i])
            i -= 1
        elif nums[i]*nums[i] < nums[j]*nums[j]:
            ans.append(nums[i]*nums[i])
            i -= 1
        else:
            ans.append(nums[j]*nums[j])
            j += 1
    return ans

nums_ = [-4,-1,0,3,10]
print(s_s_a(nums_))
