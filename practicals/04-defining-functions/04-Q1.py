def validate(number):
    if number <= 0 and number >= 100:
        return bool(number)

print(validate(int(input("Enter a number: "))))