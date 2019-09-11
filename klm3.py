#11
import math
a = int(input("mutqagreq a: "))
b = int(input("mutqagreq b: "))
x = int(input("mutqagreq x: "))

if a**2 + b**2 > 5:
    print("Y =", 3*math.pow(math.e, a - x))

elif  a**2 + b**2 < 1:
    print("Y =", math.pow(math.tan(a + b), 4))

else:
    print("Y =", -3)


