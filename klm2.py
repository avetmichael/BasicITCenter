#3
import math
x = int(input("mutqagreq x: "))
y = int(input("mutqagreq y: "))

print("f(x, y) = ", 1 / math.tan((math.fabs(x**2 - y)) / (x**2 + y**2)) + math.log(x**2 + 1, 10))