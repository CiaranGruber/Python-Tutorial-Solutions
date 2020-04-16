def main()  # Syntax error
    a = 5
    print("Sum:", a + a)
    print("Tripled:", a / 3)  # Semantic error. Meant to be a * 3
    a *= a
    print("To the power of itself:", a)
    print("Doubled", a * 2)  # Logic error, a has been changed to be to the power of itself - this is (a^2)*2 not a*2


if __name__ == "__main__":
    main()