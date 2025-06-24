def is_prime(number):
    """
    This function checks the given user input number is prime or non-prime.
    :param number: int
    :return: None
    """
    count = 0
    for num in range(2, number):
        if number % num == 0:
            count += 1
    if count == 0:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


number = int(input("Enter the number: "))
is_prime(number)