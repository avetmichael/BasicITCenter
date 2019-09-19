a = "anna"
for i in range(len(a) // 2):
    if a[i] == a[len(a) - 1 - i]:
        print("True")
    else:
        print("False")