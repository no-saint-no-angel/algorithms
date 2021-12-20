
def rotate_array(list, k):
    n = k%len(list)
    list[:n], list[n:] = list[len(list)-n:], list[:len(list)-n]
    return list

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(nums, k))