#1
import math
x = int(input("mutqagreq x: "))
y = int(input("mutqagreq y: "))

print("f(x, y) = ", (y + 1)*(x + math.pow(x**2 + 1, 6) * math.sin(x**2 - 3) - math.tan(y)))