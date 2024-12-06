temperatures = []
def enter_temp(a):
    while True:
        temperatures = input("Enter temperatures: ")
        if temperatures == "":
            return temperatures
        else:
            break

def max_calc():
    max_temp = max(temperatures)
    return

def min_calc():
    min_temp = min(temperatures)
    return

def mean_calc():
    mean_temp = int(sum(temperatures) / len(temperatures))
    return

if temperature:
    a = max_calc()
    b = min_calc()
    c = mean_calc()

temperatures = enter_temp(temperatures)


print("The Minimum Temperature is: ", b, "C")
print("The Maximum temperature is: ", a, "C")
print("The Mean Temperature is: ", c, "C")