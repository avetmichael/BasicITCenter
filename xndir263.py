import random
def func1(n = 5, a = -7, b = 7):
    arr_1 = []
    for i in range(n):
        c = random.randint(a, b)
        arr_1.append(c)
    return arr_1
arr_1 = func1()
m = 0
for i in arr_1:
    if i > 0:
        m = m + 1
def func2(n = 5, a = -7, b = 7):
    arr_2 = []
    for i in range(n):
        c = random.randint(a, b)
        arr_2.append(c)
    return arr_2
arr_2 = func2()
h = 0
for j in arr_2:
    if j > 0:
        h = h + 1
print(arr_1)
print(arr_2)
print(h + m)

