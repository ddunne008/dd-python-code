miles = input("Enter the miles value: ")
miles = int(miles)
if miles < 0:
    print("The number should not be a negative number")

kilometers = miles * 1.609

print(f"{miles} is equivalent to {kilometers} kilometers")