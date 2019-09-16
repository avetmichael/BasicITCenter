#5
import math
x = int(input("mutqagreq x: "))
y = int(input("mutqagreq y: "))

print('f(x, y) =', (2**x - 5) / (3**y + 2) + math.log((math.fabs(x) + 1)**4 + y**2, 2))