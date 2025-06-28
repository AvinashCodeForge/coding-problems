def secondLargest(lst):
    largest = float("-inf")
    second_largest = float("-inf")
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    print(second_largest)


lst = [1, 3, 4, 9, 8]
secondLargest(lst)
