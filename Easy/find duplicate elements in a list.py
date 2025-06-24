def duplicateNums(list):
    """
    This function extract the duplicate elements from the list.
    :param list: list
    :return: list
    """
    result = [list[index] for index in range(len(lst)) if list[index] not in list[:index]]
    print(result)


lst = [1, 2, 3, 2, 4, 5, 1]
duplicateNums(lst)