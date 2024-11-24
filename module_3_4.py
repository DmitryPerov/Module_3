def single_root_words(root_word, *other_words):
    same_words = []
    list_other_words = list(other_words)
    for i in range(len(list_other_words)):
        if root_word.lower() in list_other_words[i-1].lower():
            same_words.append(list_other_words[i-1])
        else:
            if list_other_words[i-1].lower() in root_word.lower():
                    same_words.append(list_other_words[i-1])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)