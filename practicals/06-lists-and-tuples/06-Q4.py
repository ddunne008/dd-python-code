
message = input("Enter a message to encrypt: ")
message = list(message)
message.append(message)


while " " in message:
    message.remove(" ")

message.reverse()
print("Encrypted Message: ", message)
