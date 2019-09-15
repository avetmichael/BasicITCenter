#75
import math
x = -math.pi

while x <= math.pi:
    y = math.pow(math.sin(x), 2) + math.cos(x)
    print(x, y)
    x = x + math.pi / 8
