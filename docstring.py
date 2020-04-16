def main():
    text = input('Text: ').split()
    word_to_count = count_words(text)
    max_word_length = find_longest_word(word_to_count)
    print()

    words = [[word, count] for word, count in word_to_count.items()]
    words.sort()
    max_count_length = len(str(max(word_to_count.values())))

    for word, count in words:
        print('{:{}}: {:{}}'.format(word, max_word_length, count, max_count_length))


def count_words(string):
    word_to_count = {}
    for word in string:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def find_longest_word(dictionary):
    max_word_length = 0
    for word in dictionary:
        if max_word_length < len(word):
            max_word_length = len(word)
    return max_word_length


main()
