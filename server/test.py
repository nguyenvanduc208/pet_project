

arr = [4,2,5,12,7,33,14,6]

while True:
    count = 0
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp

            count = count+ 1
    
    if count == 0:
        break
        



print(arr)