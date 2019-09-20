arr = [1, 2, 3, 4, 5, 6, 7, 8]
b = 0
k = 3
for i in range(len(arr)):
    if i % k == 0:
        b = b + arr[i]
print(b)



