def main():
    number = -1
    total = 0
    iterations = 0
    while number != 0:
        number = int(input("Number: "))
        total += number
        if number != 0:
            iterations += 1
    print("Average:", total / iterations)


if __name__ == "__main__":
    main()
