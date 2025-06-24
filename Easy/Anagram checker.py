def anagramChecker(word1, word2):
    """
    This function verifies the given word is anagram or not.
    :param word: str
    :return: str
    """
    if len(word1) == len(word2):
        for character in word1:
            if character not in word2:
                print(f"Not an anagram")
                break
        else:
            print("Yes, Anagram")
    else:
        print("Given words are not anagram.")


word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
anagramChecker(word1, word2)