def convert_binary(n):
    if n <= 0:
        print("The number must be a positive number")
    else:
        return bin(n)[2:]

print(convert_binary(192))