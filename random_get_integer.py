from get_integer import get_integer
import random


def main():
    number1 = random.randint(30, 100)
    number2 = random.randint(30, 100)
    min_number = min(number1, number2)
    max_number = max(number1, number2)
    get_integer("Choose a number (" + str(min_number) + "-" + str(max_number) + "): ", "Input must be an integer\n",
                "Number must be between " + str(min_number) + " and " + str(max_number) + "\n", min_number, max_number)


if __name__ == "__main__":
    main()
