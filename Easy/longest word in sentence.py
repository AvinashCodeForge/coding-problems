def longestWord(sentence):
    lst_sentence = sentence.split()
    word_length = 0
    highest_word = ""
    for word in lst_sentence:
        if len(word) > word_length:
            highest_word = highest_word.replace(highest_word, word)
            word_length += len(word)
    print(highest_word)


sentence = "Coding makes you think differently"
longestWord(sentence)