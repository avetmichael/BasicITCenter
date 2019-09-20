X = [1, 2, 3, 42, 3214, 421]
Y = [4, 5, 6, 321343, 421343, 34221, 123, 4312]
a = 0
b = 0
for i in range(len(X)):
    if i % 2 == 0:
        a = a + 1
for k in range(len(Y)):
    if k % 2 == 1:
        b = b + 1

print(a + b)

