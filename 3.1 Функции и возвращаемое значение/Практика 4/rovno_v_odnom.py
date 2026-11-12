def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False

    count = 0
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            count += 1

    if count == 1:
        return True
    else:
        return False
