

def permuta(arr,pos, end):
    if pos == end:
        print(arr)
    else:
        for index in range(pos, end):
            arr[index], arr[pos] = arr[pos],arr[index]
            permuta(arr, pos+1, end)
            arr[index], arr[pos] = arr[pos], arr[index]

arr = ["1", "2", "3"]
permuta(arr, 0, len(arr))