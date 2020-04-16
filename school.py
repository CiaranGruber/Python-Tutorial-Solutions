def main():
    age = int(input("Age: "))
    if age > 17 or age < 5:
        print("Not in school")
    elif age >= 15:
        print("High school")
    elif age >= 11:
        print("Middle school")
    else:
        print("Junior school")


if __name__ == "__main__":
    main()
