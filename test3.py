#53
n = int(input("mutqagreq n: "))
k = int(input("mutqagreq k: "))

a = int(n / 100) #1in tivy
b = n % 10 #3rd tivy
c = int(n / 10)
d = c % 10 #2rd tivy

if n > k:
    print(n / (a + b + c))

else:
    print(c / n)
