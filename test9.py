#211
abc = [5, 4, 7, -2, 9, -3, -7, -9]
gumar = 0
b = 0
for x in abc:
    if x > 0:
        b = b + 1
        gumar = gumar + x
print(gumar / b)
