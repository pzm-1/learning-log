def main():
    while True:
        try:
            fraction = input("Fraction:")
            parts = fraction.split("/")
            x = int(parts[0])
            y = int(parts[1])
            if y == 0:
                raise ZeroDivisionError
            if x > y or x < 0 or y < 0:
                raise ValueError
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            pass
main()