def main():
    string = input("String: ")
    print("Lowercase:", string.lower())
    print("Is in title case:", string.istitle())
    # Note for below: position is zero-based, essentially the first letter is position 0
    print("Is the third letter 'a'?", string[2] == 'a')
    position = string.find('e') + 1  # By storing the string.find() result, the code only has to find the position once
    print("Letter 'e' position", "Not present" if position == 0 else position)  # Print position if present


if __name__ == "__main__":
    main()
