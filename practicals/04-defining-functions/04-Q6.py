def celcius_fahrenheit(temperature):
    celcius = (temperature[:-1])
    int(celcius)
    celcius * (9/5) + 32
    return celcius





temperature = input("Enter the temperature in Celcius: ")
answer = celcius_fahrenheit(temperature)
print(temperature, "Translates to the temperature in fahrenheit as:", answer)