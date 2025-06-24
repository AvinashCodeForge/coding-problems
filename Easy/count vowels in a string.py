def count_vowels(sentence):
    """
    This function counts the vowels in a given string.
    :param sentence: str
    :return: str
    """
    count = 0
    vowels = "aeiouAEIOU"
    for character in sentence:
        if character in vowels:
            count += 1
    return f"vowels in a sentence: {count}"


sentence = input("Enter the sentence: ")
print(count_vowels(sentence))