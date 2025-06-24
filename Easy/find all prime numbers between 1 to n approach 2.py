def primeNumbers(endNum):
    """
    This function prints the prime numbers from 1 to N numbers.
    :param endNum: int
    :return: int
    """
    for num in range(2, endNum+1):
        count = 0
        for num_1 in range(2, int(num**0.5)+1):
            if num % num_1 == 0:
                count += 1
        if count == 0:
            print(f"{num}", end=" ")


endNum = int(input("Enter number: "))
primeNumbers(endNum)