#63
n = int(input("mutqagreq n: "))

a = int(n / 1000) #1in tivy
b = n % 10 #4rd tivy
c = int(n / 100)
d = c % 10 #2rd tivy
e = int(n / 10)
f = e % 10 #3rd tivy

if a == 1 or d == 1 or f == 1 or b == 1:
    print(1)

else:
    print(0)