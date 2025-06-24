def print_even_numbers(number):
    """
    This function prints the even numbers from 1 to 100.
    :param
        int: number
    :return: None
    """
    for num in range(1, number+1):
        if num % 2 == 0:
            print(num, end=" ")


number = int(input("Enter the number: "))
print_even_numbers(number)
