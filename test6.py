#69
n = int(input("mutqagreq n: "))

a = int(n / 1000) #1in tivy
b = n % 10 #4rd tivy
c = int(n / 100)
d = c % 10 #2rd tivy
e = int(n / 10)
f = e % 10 #3rd tivy

if a + d + f + b > 20:
    print("y =", 1)

else:
    print("y =", 0)