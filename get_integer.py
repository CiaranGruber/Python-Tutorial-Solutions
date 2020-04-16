def get_integer(prompt, error_prompt, limits_prompt, min_num=-float('inf'), max_num=float('inf')):
    while True:
        try:
            integer = int(input(prompt))
            if max_num >= integer >= min_num:
                return integer
            print(limits_prompt)
        except ValueError:
            print(error_prompt)


def main():
    get_integer("Try to give an invalid integer (3-10): ", "Nope can't do the wrong type\n",
                "Can't be outside limits\n", 3, 10)


if __name__ == "__main__":
    main()
