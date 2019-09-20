n = int(input("tarreri tivy: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

b = 0
for k in arr:
    if k % 7 == 0:
        b = b + 1
print(b)
