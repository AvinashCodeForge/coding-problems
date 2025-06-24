def is_palindrome(word):
    """
    This function verifies the given word is palindrome or not.
    :param word: str
    :return: str
    """
    length = len(word)
    mid = int(length // 2)
    if length % 2 == 0:
        first_half = word[:mid]
        second_half = word[mid:]
        if first_half == second_half[::-1]:
            print(f"{word} is palindrome.")
        else:
            print(f"{word} is not palindrome.")
    else:
        first_half = word[:mid+1]
        second_half = word[mid:]
        if first_half == second_half[::-1]:
            print(f"{word} is palindrome.")
        else:
            print(f"{word} is not palindrome.")


word = input("Enter the word: ")
is_palindrome(word)