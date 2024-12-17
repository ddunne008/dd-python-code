message_list = []

message = input("Enter a message to encrypt: ")
message_list.append(message)

if message == "":
    message_list.remove(" ")

message_list.reverse()

print(message_list)
