#72
import math
x = -5.4

while x <= 1.2:
    y = 1 / math.pow(math.tan(x**2), 2)
    print(x, y)
    x = x + 0.4