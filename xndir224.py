import math
arr = [1, 43, 32, 12, 163, -432, -2382]
a = 0
k = 123
for i in arr:
    if math.fabs(i) > k:
        a = a + i ** 3
print(a)