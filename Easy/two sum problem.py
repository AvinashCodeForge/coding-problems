def twoSum(lst, target):
    pointer_1 = 0
    pointer_2 = 1
    while pointer_2 <= len(lst):
        if lst[pointer_1] + lst[pointer_2] == target:
            print([pointer_1, pointer_2])
            break
        pointer_1 += 1
        pointer_2 += 1


lst = [11, 15, 1, 3, 2, 7]
target = 9
twoSum(lst, target)