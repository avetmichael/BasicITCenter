#42
x = int(input("mutqagreq x: "))
y = int(input("mutqagreq y: "))

if x >= 0 and y >=0 and x**2 + y**2 >= 1 and y <= 2 - x:
    print("z =", x + y**2)

else:
    print("z =", 5*x)