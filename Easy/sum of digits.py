def digitsSum(digit):
    """
    This function sum up the digits.
    :param digit: int
    :return: int
    """
    result = 0
    while digit > 0:
        mod = digit % 10
        result += mod
        digit = digit // 10
    print(f"Final result: {result}")


digit = int(input("Enter the number: "))
digitsSum(digit)