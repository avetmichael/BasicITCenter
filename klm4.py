#12
import math

x = int(input("mutqagreq x: "))
a = int(input("mutqagreq a: "))

if -5 <= x <= 5:
    print("Y =", (1 + a**2)**6)

elif x > 5:
    print("Y =", math.cos(math.pow(math.log(math.sqrt(x), 10), 2)) + x**8)

else:
    print("Y =", a)