def reverse_string(word):
    """
    This function reverse the given string.
    :param word: str
    :return: str
    """
    result = ""
    for character in word:
        result = character + result
    return result


word = input("Enter the word: ")
print(reverse_string(word))