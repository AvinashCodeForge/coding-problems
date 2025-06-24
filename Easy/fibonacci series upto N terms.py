def fibonacciSeries(number):
    """
    This function prints the first n numbers in fibonacci sequence
    :param number: int
    :return: int
    """
    a, b = 0, 1
    for _ in range(number):
        print(a, end=" ")
        a, b = b, a+b


num = int(input("Enter number: "))
fibonacciSeries(num)