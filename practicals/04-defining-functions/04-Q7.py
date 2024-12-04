

temp_1 = input("Enter a temperature: ")
temp_2 = input("Enter a temperature: ")
temp_3 = input("Enter a temperature: ")
temp_4 = input("Enter a temperature: ")
temp_5 = input("Enter a temperature: ")
temp_6 = input("Enter a temperature: ")


max_temp = max(float(temp_1, temp_2, temp_3, temp_4, temp_5, temp_6))
min_temp = min(float(temp_1, temp_2, temp_3, temp_4, temp_5, temp_6))
mean_temp = (temp_1, temp_2, temp_3, temp_4, temp_5, temp_6) / 6

if temp_1 == str(temp_1) and temp_2 == str(temp_2) and temp_3 == str(temp_3) and temp_4 == str(temp_4) and temp_5 == str(temp_5) and temp_6 == str(temp_6):
    print("The minimum Temperature is: ", min_temp)
    print("The Maximum temperature is: ", max_temp)
    print("The mean Temperature is: ", mean_temp)
else:
    print("The temperature does not have a c after it (E.g. 24C)")