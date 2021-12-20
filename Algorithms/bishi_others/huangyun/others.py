import re

it = re.finditer(r"\d+", "0a12b3cD")
for match in it:
    print(match.group())


def fu(arr):
    arr.append([4,5,6])
    print(arr)
    return
arr = [1,2,3]
fu(arr)
print(arr)