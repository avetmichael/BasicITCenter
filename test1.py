#55
n = int(input("mutqagreq n: "))

a = int(n / 10)
c = a % 10
b = n % 10
d = int(n / 100)

if c > d and b > d:
    print(d)

elif d > c and b > c:
    print(c)

elif b < d and b < c:
    print(b)