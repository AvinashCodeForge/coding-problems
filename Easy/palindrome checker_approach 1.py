def is_palindrome(word):
    """
    This function verifies the given word is palindrome or not.
    :param word: str
    :return: str
    """
    result = ""
    for character in word:
        result = character + result
    if result == word:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not a palindrome")
        

word = input("Enter the word: ")
is_palindrome(word)