text = input("Input: ")
for char in text:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
        print(char, end="")
print()