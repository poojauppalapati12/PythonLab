def split(arr, k):

    arr = arr[k:] + arr[:k]

    return arr

   

k = 3

arr = [10, 13, 5, 17, 8, 9]

print("Output array is", split(arr, k))
