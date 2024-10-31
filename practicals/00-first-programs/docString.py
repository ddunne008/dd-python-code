def find_min(a, b):
    return a if a < b else b


no1 = input("Enter a number: ")
no2 = input("Enter a second number: ")
answer = find_min(no1, no2)

print("The smallest number is", answer)

