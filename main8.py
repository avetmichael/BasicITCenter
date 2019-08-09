#84
import math

x = -6.4

while x < 2.4 and math.cos(x) != 0:
    y = math.pow(math.e, math.pow(math.tan(x), -1))
    print(x, y)
    x = x + 0.2