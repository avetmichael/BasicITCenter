#57
n = int(input("mutqagreq n: "))

a = int(n / 10)
a = a % 10
b = n % 10

if n > 300:
    print(a / b)

else:
    print(int(n / 10) / b)
