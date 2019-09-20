import math
n = int(input("tarreri tivy: "))
arr = []
for i in range(n):
    arr.append(int(input("mutqagreq: ")))
print(arr)
k = 7
a = 0
for b in range(len(arr)):
    if math.fabs(arr[b] - b) > k:
        a = a + 1
print(a)