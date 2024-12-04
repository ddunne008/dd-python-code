def celcius_fahrenheit(temp):
    temp = float(temp)
    F = temp * 1.8 + 32
    return F



a = input("Enter the temperature in Celcius: ")
if "c" not in a:
    print("The temperature should have a C after the number")
else:
    a = a[:2]
    a = float(a)
    temp = float(celcius_fahrenheit(a))
    print(a,"C", "Translates to the temperature in fahrenheit as:", temp, "F")