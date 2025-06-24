def fizzBuzz(number):
    """
    This function takes a number and if it is divisible by 3 prints 'Fizz', if divisible by 5 print 'Buzz', if divisible by both, print 'FizzBuzz'
    :param number: int
    :return: int
    """

    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"{num} is not divisible by 3 or 5")


num = int(input("Enter a number: "))
fizzBuzz(num)


