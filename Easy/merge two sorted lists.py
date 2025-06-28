def mergeTwoSortedLst(lst1, lst2):

    pointer_lst_1 = 0 # 0, 1, 2, 3
    pointer_lst_2 = 0 # 0, 1, 2,
    result = [] # [1, 2, 3, 4, 5, 6]
    while pointer_lst_1 < len(lst1) and pointer_lst_2 < len(lst2):
        if lst1[pointer_lst_1] < lst2[pointer_lst_2]:
            result.append(lst1[pointer_lst_1])
            pointer_lst_1 += 1
        else:
            result.append(lst2[pointer_lst_2])
            pointer_lst_2 += 1
    if lst1:
        result.extend(lst1[pointer_lst_1:])
    if lst2:
        result.extend(lst2[pointer_lst_2:])

    print(result)


lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
mergeTwoSortedLst(lst1, lst2)