def get_score(name_and_score):
    return name_and_score[1]


def main():
    name = " "
    music_results = []
    while name != "":
        name = input("Name: ")
        if name != "":
            score = int(input("Score: "))
            music_results.append((name, score))
    music_results.sort(reverse=True, key=get_score)
    print()
    print("Scores:")
    for i, result in enumerate(music_results):
        print(str(i + 1) + ".", result[0], "(" + str(result[1]) + ")")


if __name__ == "__main__":
    main()
