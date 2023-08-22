def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    age = int(input("Enter your age: "))

    if age < 18:
        print("You're still a minor!")
    elif 18 <= age < 30:
        print("You're a young adult!")
    else:
        print("You're an adult!")


if __name__ == "__main__":
    main()
