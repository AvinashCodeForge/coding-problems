def largest_of_three_numbers(lst):
    """
    This function finds the largest number from 3 numbers and returns the list of largest numbers.
    :param lst: int
    :return: list
    """
    pointer_1 = 0
    pointer_2 = 2
    result = []
    while pointer_2 < len(lst):
        max_number = max(lst[pointer_1:pointer_2+1])
        result.append(max_number)
        pointer_1 += 1
        pointer_2 += 1

    return result


lst = [9, 5, 1, 3, 5, 7, 7, 4, 1, 8, 5, 2, 9, 6, 3]
print(largest_of_three_numbers(lst))
