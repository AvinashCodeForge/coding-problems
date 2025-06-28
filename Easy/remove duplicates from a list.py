def removeDuplicates(lst):
    result = [lst[num] for num in range(len(lst)) if lst[num] not in lst[:num]]
    print(result)


lst = [1, 2, 3, 1, 2, 4]
removeDuplicates(lst)