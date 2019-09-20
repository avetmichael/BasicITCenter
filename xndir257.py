arr = [5, 6, 10, 8, 9, 7]
k = 0
for i in range(len(arr)):
    if arr[k] < arr[i]:
        k = i
print(k)
