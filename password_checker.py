SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    is_valid = False
    print("Password must have at least 1 capital, special character and number")
    while not is_valid:
        password = input("Enter Password: ")
        is_valid = is_password_valid(password)
        if not is_valid:
            print("Password is not valid")
    print("Password is valid")


def is_password_valid(password):
    return contains_capital(password) and contains_special(password) and contains_number(password)


def contains_capital(password):
    for letter in password:
        if letter.isupper():
            return True
    return False


def contains_special(password):
    for letter in password:
        if letter in SPECIAL_CHARACTERS:
            return True


def contains_number(password):
    for letter in password:
        if letter.isnumeric():
            return True
    return False


if __name__ == "__main__":
    main()
