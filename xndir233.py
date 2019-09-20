n = int(input("tarreri tivy: "))
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

b = 0
c = 1
for k in arr:
    if k % 2 == 0:
        b = b + k
        c = c * k

print(b, "gumar", c, "artadryal")
