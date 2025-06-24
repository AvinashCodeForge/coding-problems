def frequencyOfCharacters(sentence):
    """
    This function counts the characters
    :param sentence: str
    :return: dict
    """
    result = {}
    for character in sentence:
        if character != " ":
            result[character] = result.get(character, 0) + 1
    print("Final Result :", result)


sentence = "python is a good programming language"
frequencyOfCharacters(sentence)