#157
def gumar():
    b = 0
    for i in range(1, 1001):
        if i % 5 != 0:
            b = b + i
    print(b)

gumar()