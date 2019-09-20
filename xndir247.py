import math
n = int(input("tarreri tivy: "))
arr = []
for i in range(n):
    arr.append(int(input("mutqagreq: ")))
print(arr)

a = 0
b = 0
for k in range(len(arr)):
    if arr[k] > k:
        a = a + arr[k] ** 2
        b = b + 1

print(math.sqrt(b + a))
