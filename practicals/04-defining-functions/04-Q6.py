def celcius_fahrenheit(temperature):
    if (temperature) == 'C':
        celcius = (temperature[:-1])
        float(celcius)
        celcius * (9/5) + 32
    elif (temperature) != 'C':
        print("The temperature must be formatted with a C")




temperature = input(str("Enter the temperature in Celcius: "))
celcius = celcius_fahrenheit(temperature)
print(temperature, "Translates to the temperature in fahrenheit as:", celcius )