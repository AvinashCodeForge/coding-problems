def rotateArray(lst, rotate):
    for i in range(rotate):
        left = lst.pop(0)
        lst.append(left)
    print(lst)


lst = [1, 2, 3, 4, 5]
rotate = int(input("Enter number to rotate: "))
rotateArray(lst, rotate)