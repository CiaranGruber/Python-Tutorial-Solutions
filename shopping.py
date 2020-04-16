def main():
    item = " "
    shopping_list = []
    while item != "":
        item = input("Next item: ")
        if item != "":
            shopping_list.append(item)
    print("Number of items:", len(shopping_list))
    shopping_list.sort()
    for shopping_item in shopping_list:
        print("-", shopping_item)


if __name__ == "__main__":
    main()
