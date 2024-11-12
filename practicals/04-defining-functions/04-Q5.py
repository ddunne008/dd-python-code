
print("***Celcius to Fahrenheit convert program***")
def menu():
    print("Option 1 - Celcius to Fahrenheit")
    print("Option 2 - Fahrenheit to Celcius")
    option = int(input("Which option would you like to open? "))
    if option == 1:
        convert_celcius(C)
    elif option == 2:
        convert_fahrenheit(F)
    else:
        print("No option displayed is selected")
def convert_fahrenheit(F):
    F = input("Enter the Celcius Temperature: ")
    fahrenheit = (F - 32) * 5/9
    print("Degrees in fahrenheit are", (convert_fahrenheit(F)))

def convert_celcius(C):
    C = input("Enter the Celcius Temperature: ")
    celcius = C * (9/5) + 32
    print("Degrees in Celcius are", (convert_celcius(C)))








