#51
n = int(input("mutqagreq n: "))
t = True

a = int(n / 100) #1in tivy
b = n % 10 #3rd tivy
c = int(n / 10)
d = c % 10 #2rd tivy

if b == a + d:
    print(t)

else:
    print(not t)