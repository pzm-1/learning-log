camel = input("camelCase: ")
for char in camel:
    if char.isupper():
        print("_", end="")
        print(char.lower(), end="")
    else:
        print(char, end="")
print()