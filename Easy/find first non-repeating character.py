def nonRepeatingChr(word):
    for chr in word:
        if word.count(chr) == 1:
            print(chr)
            break


word = "aabbcddeff"
nonRepeatingChr(word)
