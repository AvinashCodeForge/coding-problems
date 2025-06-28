def primeNumbers(endNum):
    """
    This function prints the prime numbers from 1 to N numbers.
    :param endNum: int
    :return: int
    """
    for num in range(2, endNum+1):
        for num_1 in range(2, num):
            if num % num_1 == 0:
                break
        else:
            print(num, end=" ")


endNum = int(input("Enter number: "))
primeNumbers(endNum)