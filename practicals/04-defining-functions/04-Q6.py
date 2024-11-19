def celcius_fahrenheit(temperature):
    celcius = (temperature[:-1])
    int(celcius)
    celcius * (9/5) + 32
    return celcius





a = input("Enter the temperature in Celcius: ")
answer = celcius_fahrenheit(a)
print(a, "Translates to the temperature in fahrenheit as:", answer)