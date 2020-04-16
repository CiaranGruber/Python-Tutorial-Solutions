def main():
    word_dictionary = {}
    string = input("Enter string: ")
    string = string.lower()
    string_list = string.split(" ")
    for word in string_list:
        word_dictionary[word] = word_dictionary.setdefault(word, 0) + 1
    for word, count in word_dictionary.items():
        print(word, "×", count)


if __name__ == "__main__":
    main()
